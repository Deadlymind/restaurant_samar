"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),


    path('summernote/', include('django_summernote.urls')),


    path('meals/' , include('meals.urls' , namespace='meals')),

    path('about-us/' , include('about.urls' , namespace='aboutus')),
    path('blog/' , include('blog.urls' , namespace='blog')),
    path('reserve_table/' , include('reservation.urls' , namespace='reservation')),
    path('commande/', include(('commande.urls', 'commande'), namespace='commande')),  # Utiliser un 2-tuple avec le nom de l'application






    path('' , include('home.urls' , namespace='home')),
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Resturant AdminPanel"
admin.site.site_title = "Resturant App Admin "
admin.site.site_index_title = "Welcome To Resturant Admin Panel"




