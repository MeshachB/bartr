from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('signup/', views.signup, name='signup'),
    
    path('create/', views.create_listing, name='create'),
   
    path(
    'listings/<int:listing_id>/update/',
    views.update_listing,
    name='update_listing'
),

path(
    'listings/<int:listing_id>/delete/',
    views.delete_listing,
    name='delete_listing'
),
]