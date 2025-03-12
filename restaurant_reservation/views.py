from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# from .forms import ReservationForm, CustomerUserCreationForm, CustomerUserUpdateForm
from .models import (
    Restaurant,
    Reservation,
    Table,
    CustomUser,
)


@login_required
def index(request):
    """View function for the home page of the site."""

    num_restaurant = Restaurant.objects.count()
    num_reservation = Reservation.objects.count()
    num_tables = Table.objects.count()
    num_users = CustomUser.objects.count()

    context = {
        "num_restaurant": num_restaurant,
        "num_reservation": num_reservation,
        "num_tables": num_tables,
        "num_users": num_users,
    }

    return render(request, "restaurant_reservation/index.html", context=context)


class RestaurantListView(ListView):
    model = Restaurant


class RestaurantCreateView(CreateView):
    model = Restaurant
    fields = "__all__"
    success_url = reverse_lazy("restaurant_reservation:restaurant-list")


class RestaurantDetailView(DetailView):
    model = Restaurant
    fields = "__all__"


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    fields = "__all__"
    success_url = reverse_lazy("restaurant_reservation:restaurant-list")


class RestaurantDeleteView(LoginRequiredMixin, DeleteView):
    model = Restaurant
    success_url = reverse_lazy("restaurant_reservation:restaurant-list")


def my_reservations(request: HttpRequest, pk: int) -> HttpResponse:
    user = CustomUser.objects.get(pk=pk)
    reservations = Reservation.objects.filter(guest_id=user)
    context = {"user": user, "reservations": reservations}
    return render(request, "restaurant_reservation/my_reservations.html", context=context)


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "restaurant_reservation/reservation_form.html"

    def get_success_url(self):
        return reverse_lazy("restaurant_reservation:my-reservations", kwargs={'pk': self.request.user.pk})


class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "restaurant_reservation/reservation_form.html"

    def get_success_url(self):
        return reverse_lazy("restaurant_reservation:my-reservations", kwargs={'pk': self.request.user.pk})


class ReservationDeleteView(LoginRequiredMixin, DeleteView):
    model = Reservation

    def get_success_url(self):
        return reverse_lazy("restaurant_reservation:my-reservations", kwargs={'pk': self.request.user.pk})


class UsersListView(ListView):
    model = CustomUser
    fields = "__all__"


class UsersCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    form_class = CustomerUserCreationForm

    def get_success_url(self):
        return reverse_lazy("restaurant_reservation:users-list")


class UsersDetailView(DetailView):
    model = CustomUser


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomerUserUpdateForm
    success_url = reverse_lazy("restaurant_reservation:users-list")


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy("restaurant_reservation:users-list")