from django.urls import path
from . import views


urlpatterns = [
path("", views.home, name="homePage"),
path('produktet/', views.produktet, name='produktetPage'),
path('detajet/<int:pk>/', views.detajet, name='detajetPage'),

]
