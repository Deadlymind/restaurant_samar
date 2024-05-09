from django.shortcuts import render,redirect
from .forms import ReviewForm
# Create your views here.
from .models import Meals , Category ,Review
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404



def meal_list(request, slug=None):
    meals = Meals.objects.all()

    meal_detail = None
    if slug is not None:
        meal_detail = get_object_or_404(Meals, slug=slug)

    meal_list = Meals.objects.all()
    categories = Category.objects.all()
    context = {
        'meals' : meals ,

        'meal_detail': meal_detail,
        'meal_list': meal_list,
        'categories': categories,
    }
    return render(request, 'list.html', context)



@login_required
def meal_detail(request, slug):
    #meal_detail = Meals.objects.get(slug=slug)
    meal_detail = get_object_or_404(Meals, slug=slug)

    reviews = Review.objects.filter(meals=meal_detail)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.meals = meal_detail
            review.save()
            # Redirect to the same page after submitting the review
            return redirect('meal_detail', slug=slug)
    else:
        form = ReviewForm()  # Instantiate an instance of ReviewForm

    context = {
        'meal_detail': meal_detail,
        'reviews': reviews,
        'form': form
    }

    return render(request, 'detail.html', context)
def reviews(request ):
    reviews = Review.objects.all()

    context = {'reviews' : reviews}

    return render(request , 'reviews.html' , context)






