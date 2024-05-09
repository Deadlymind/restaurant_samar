from django.urls import path


from . import views

urlpatterns = [
    path('passer_commande/', views.order_meal, name='passer_commande'), 
    path('confirmation/', views.confirmation_page, name='page_de_confirmation'),
    path('panier/', views.view_cart, name='afficher_panier'),  

    path('Liste_commandes/', views.Liste_commandes, name='Liste_commandes'),
        path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),




]