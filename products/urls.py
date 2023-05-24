from django.urls import path
from .import views
urlpatterns = [ 
path('order',views.orderpage,name='orderpage'),
path('order2',views.orderpage2,name='orderpage2'),


]