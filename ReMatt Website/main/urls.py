from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>",views.index, name="index"),
    path("",views.home, name="home"),
    path("create/",views.create, name="create"),
    path("products/",views.products, name="products"),
    path("journey/",views.journey, name="journey"),
    path("about_us/",views.about_us, name="about_us"),
    path("contact/",views.contact, name="contact"),
]