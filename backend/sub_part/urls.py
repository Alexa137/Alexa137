from django.urls import path
from . views import *

urlpatterns = [

    # Accounts

    path('account_list',account_list,name='account_list'),
    path('account_detail/<int:id>/',account_detail,name='account_detail'),
    path('account_create',account_create,name='account_create'),
    path('account_update/<int:id>/',account_update,name='account_update'),
    path('account_delete/<int:id>/',account_delete,name='account_delete'),

    # Destinations

    path('destination_list/<int:account_id>/',destination_list,name='destination_list'),
    path('destination_detail/<int:id>',destination_detail,name='destination_detail'),
    path('destination_create/<int:account_id>/destinations/',destination_create,name='destination_create'),
    path('account_update/<int:account_id>/destinations/<int:id>/',account_update,name='account_update'),
    path('destination_delete/<int:id>',destination_delete,name='destination_delete'),

    path('accounts/<int:id>/destinations/',get_destinations_for_account,name='get_destinations_for_account'),


]