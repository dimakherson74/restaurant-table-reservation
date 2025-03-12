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
