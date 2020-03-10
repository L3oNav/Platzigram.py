# Django
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, UpdateView, DetailView
from django.contrib.auth import views as auth_views

from users.models import Profile
from django.db.utils import IntegrityError
from users.forms import ProfileForm, SignupForm, LoginForm
from posts.models import Post

# Create your views here.
class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class SignUpView(FormView):
    template_name='users/signup.html'
    form_class= SignupForm
    success_url = reverse_lazy('users:login')
    fields = ('username', 'email', 'password', 'password_confirmation', 'first_name', 'last_name')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


class LoginView(auth_views.LoginView):
    """Sign up view."""
    template_name='users/login.html'

@login_required
def LogoutView(request):
    """Logout a user."""
    auth_logout(request)
    return redirect('users:login')

