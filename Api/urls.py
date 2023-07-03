from django.urls import path
from .views import *


urlpatterns = [
    path("", House_homepage.as_view(), name="home"),
    path("create/", Create_page.as_view(), name="create"),
    path("<int:id>/detail/", house_detailpage.as_view(), name="detail"),
    path("book/", Booking_page.as_view(), name="book"),
]



