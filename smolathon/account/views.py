from datetime import datetime, timedelta

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.contenttypes.models import ContentType
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

from posts.utils.travel import generate_travel_route
from .exceptions import TransactionError, CheckInUrlError
from .forms import RegisterUserForm, AuthenticationUserForm
from .models import CheckInURL, TravelRoute
from .utils.point_transaction import add_points_to_user


@login_required
def check_in_place(request: HttpRequest, *args, **kwargs):
    check_url: CheckInURL = get_object_or_404(CheckInURL, id=kwargs.get('id', None))

    model = ContentType.objects.get(model=check_url.content_type.model)
    post = check_url.content_object
    try:
        transaction = add_points_to_user(request.user, check_url)
    except TransactionError as e:
        """Chow transaction error message"""
        print(e)
        return render(request, 'account/check_in_error.html', {'error': e})

    except CheckInUrlError as e:
        """Chow url error message"""
        print(e)
        return render(request, 'account/check_in_error.html', {'error': e})

    return render(request, 'account/check_in_success.html', {'post': post, 'transaction': transaction})

    # return render(request, 'posts/check_in_error.html', {'error': "error"})


def logout_view(request):
    logout(request)
    return redirect("home")


class AccountLoginView(LoginView):
    form_class = AuthenticationUserForm
    template_name = 'account/auth.html'


class RegisterView(CreateView):
    form_class = RegisterUserForm
    model = User
    template_name = 'account/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        _redirect = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        if user is not None and user.is_active:
            # login(self.request, user, backend="mysite.backends.AuthBackend")
            login(self.request, user)
            return _redirect
        return render(self.request, self.template_name, content={"form": form})


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'account/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def create_travel_route(request, *args, **kwargs):
    user = request.user
    if hasattr(user, 'travel'):
        user.travel.delete()

    now = datetime.now().date()
    end = now + timedelta(days=5)
    route = generate_travel_route(user, now, end)

    return redirect('travel_routes')


class UserTravelRoutes(LoginRequiredMixin, DetailView):
    model = TravelRoute
    template_name = 'account/travel_route.html'
    context_object_name = 'route'

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self.request.user, 'travel'):
            return redirect('create_travel_routes')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user.travel



