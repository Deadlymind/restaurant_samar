import pyrebase
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from .forms import OrderForm
from datetime import datetime, timedelta
import requests
from django.db.models import Sum
from meals.models import Meals 
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required





firebaseConfig = {
    "apiKey": "AIzaSyA7tdAGvbkTdZvDBJlbbSlZxWGdmedOXuo",
    "authDomain": "test-9c366.firebaseapp.com",
    "databaseURL": "https://test-9c366-default-rtdb.firebaseio.com",
    "projectId": "test-9c366",
    "storageBucket": "test-9c366.appspot.com",
    "messagingSenderId": "299392863833",
    "appId":"1:299392863833:web:ada3cfe52727cdab066b48"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
url = 'https://test-9c366-default-rtdb.firebaseio.com/test/digital.json'
new_value = True

def delete_old_orders():
    # Calculate the cutoff date (orders older than this date will be deleted)
    cutoff_date = datetime.now() - timedelta(minutes=2)  # Change to 2 minutes

    # Get a reference to the "orders" node
    orders_ref = db.child("orders")

    # Get orders from Firebase
    orders = orders_ref.get()

    # Check if orders exist and are not None
    if orders.val():
        # Iterate over orders and delete those older than the cutoff date
        for order_key, order_data in orders.val().items():
            ordered_at_str = order_data.get("ordered_at")
            if ordered_at_str:  # Check if ordered_at_str is not None
                ordered_at = datetime.fromisoformat(str(ordered_at_str))
                # Convert ordered_at to offset-naive datetime
                ordered_at = ordered_at.replace(tzinfo=None)
                if ordered_at < cutoff_date:
                    orders_ref.child(order_key).remove()
        print("Old orders deleted successfully.")
    else:
        print("No orders found in the database.")

@login_required
def order_meal(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = order.Repas.price * order.Quantité
            order.save()
            total_price_float = float(order.total_price)
            ordered_at_str = order.ordered_at.isoformat()
            user_data = {
           'username': order.user.username,
           'email': order.user.email,
           'phone_number': order.Numéro_de_téléphone,  # Ajoutez le numéro de téléphone de l'utilisateur

        # Add more user data fields as needed
    }
            db.child("orders",(order.Quantité ,order.Repas.name  )).push({
              "user_id": user_data,
              "meal_name": order.Repas.name,
               "quantity": order.Quantité,
              "total_price": total_price_float,
                "ordered_at": ordered_at_str
})
            delete_old_orders()

            
# Send a PUT request to update the data
            response = requests.put(url, json=new_value )
            return redirect('commande:page_de_confirmation')
    

# Check if the request was successful
    
        
    else: 
        form = OrderForm()
               
                
           
    return render(request, 'commande/passer_commande.html', {'form': form})



def confirmation_page(request):
    return render(request, 'commande/confirmation_page.html')

@login_required
def view_cart(request):
    orders = Order.objects.filter(user=request.user)
    total_price = sum(order.total_price for order in orders)
    return render(request, 'commande/cart.html', {'orders': orders, 'total_price': total_price})

@login_required
def Liste_commandes(request):
    # Fetch orders from Firebase database
    orders_ref = db.child('orders').get()
    orders = orders_ref.val()
    # Render the template with context data
    return render(request, 'commande/commandes.html', {'orders': orders })
def is_admin(user):
    return user.is_authenticated and user.is_staff
@user_passes_test(is_admin)
def admin_dashboard(request):
    # Récupérer toutes les catégories de repas disponibles
    categories = Meals.objects.values_list('category', flat=True).distinct()

    # Créer un dictionnaire pour stocker les repas par catégorie
    meals_by_category = {}

    # Récupérer les repas pour chaque catégorie
    for category in categories:
        meals = Meals.objects.filter(category=category)
        meals_by_category[category] = meals

    # Récupérer les 10 repas les plus vendus
    top_selling_meals = Order.objects.values('Repas__name').annotate(total_quantity=Sum('Quantité')).order_by('-total_quantity')[:10]
    total_meals_sold = Order.objects.aggregate(total_quantity=Sum('Quantité'))['total_quantity']

    return render(request, 'commande/admin_dashboard.html', {'meals_by_category': meals_by_category, 'total_meals_sold': total_meals_sold,'top_selling_meals': top_selling_meals})
