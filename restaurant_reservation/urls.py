from django.urls import path

from restaurant_reservation.views import (
    index,
    RestaurantListView,
    RestaurantCreateView,
    RestaurantDetailView,
    RestaurantUpdateView,
    RestaurantDeleteView,
    my_reservations,
    ReservationCreateView,
    ReservationUpdateView,
    ReservationDeleteView,
    UsersListView,
    UsersCreateView,
    UsersDetailView,
    UserUpdateView,
    UserDeleteView, TableCreateView, TableUpdateView, TableDeleteView, TableListView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "users/",
        UsersListView.as_view(),
        name="users-list",
    ),
    path(
        "users/craete",
        UsersCreateView.as_view(),
        name="user-create",
    ),
    path(
        "user/<int:pk>/detail",
        UsersDetailView.as_view(),
        name="user-detail",
    ),
    path(
        "user/<int:pk>/update",
        UserUpdateView.as_view(),
        name="user-update",
    ),
    path(
        "user/<int:pk>/delete",
        UserDeleteView.as_view(),
        name="user-delete",
    ),
    path(
        "restaurants/",
        RestaurantListView.as_view(),
        name="restaurant-list",
    ),
    path(
        "restaurants/create/",
        RestaurantCreateView.as_view(),
        name="restaurant-create",
    ),
    path(
        "restaurants/<int:pk>/",
        RestaurantDetailView.as_view(),
        name="restaurant-detail",
    ),
    path(
        "restaurants/<int:pk>/update/",
        RestaurantUpdateView.as_view(),
        name="restaurant-update",
    ),
    path(
        "restaurants/<int:pk>/delete/",
        RestaurantDeleteView.as_view(),
        name="restaurant-delete",
    ),
    path(
        "reservation/create/",
        ReservationCreateView.as_view(),
        name="reservation-create",
    ),
    path(
        "reservation/<int:pk>/update/",
        ReservationUpdateView.as_view(),
        name="reservation-update",
    ),
    path(
        "reservation/<int:pk>/delete/",
        ReservationDeleteView.as_view(),
        name="reservation-delete",
    ),
    path(
        "my-reservations/<int:pk>/",
        my_reservations,
        name="my-reservations",
    ),
    path("table/create/", TableCreateView.as_view(), name="table-create", ),
    path("table/<int:pk>/update/", TableUpdateView.as_view(), name="table-update", ),
    path("table/<int:pk>/delete/", TableDeleteView.as_view(), name="table-delete", ),
    path("tables/", TableListView.as_view(), name="table-list", ),
]


app_name = "restaurant_reservation"
