from django.urls import path
from boss import views

urlpatterns = [
    path('shops/', views.time_input, name="timeinput"),
    # path('menus/<int:shop>', views.menu, name="menu"),
    # path('order/', views.order, name="order"),
]