from django.urls import path
from users import views

urlpatterns = [
    path('', views.LoginView.as_view(), name="login"),
    path('<str:username>/detail/', views.UserDetailView.as_view(), name='detail'),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('update_profile/', views.UpdateProfileView.as_view(), name="update_profile")
]