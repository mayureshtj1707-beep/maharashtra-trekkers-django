from django.urls import path
from . import views 


urlpatterns = [
    path('',views.home, name='home'),
    path('home2/',views.home2, name='home2'),
    path('district/<str:district>/', views.district_treks, name='district_treks'),
    path('trek/<int:trek_id>/', views.trek_detail, name='trek_detail'),
    path('trek/book/<int:trek_id>/', views.book_trek, name='book_trek'),
    
    path('register/', views.register_page , name='register_page'),
    path('login/', views.login_page , name='login_page'),
    path('logout/', views.logout_page , name='logout_page'),
]
