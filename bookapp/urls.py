from django.contrib import admin
from django.urls import path,include
from bookapp import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='home'),  # Home page
    path('about/', views.about_us, name='about_us'),  # About Us page
    path('classics/', views.classics, name='classics'),  # Classics page
    path('contactus/', views.contactus, name='contactus'),  # Contact Us page
    path('dystopian/', views.dystopian, name='dystopian'),
    path('fantasy/', views.fantasy, name='fantasy'),
    path('mystery/', views.mystery, name='mystery'),
    path('non_fiction/', views.non_fiction, name='non_fiction'),
    path('signup/', views.signup, name='signup'),
    path('sci_fic/', views.sci_fic, name='sci_fic'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/updatebookstatus/', views.update_book_status, name='update_book_status'),
    path('get_user_books/', views.get_user_books, name='get_user_books'),
    path('search_books/', views.search_books, name='search_books'),
     
    

]