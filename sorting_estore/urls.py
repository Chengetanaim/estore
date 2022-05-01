from django.urls import path, include
from . import views

app_name = 'sort_estore'
urlpatterns = [
    path('men_collection/', views.men_collection, name='men_collection'),
    path('ladies_collection/', views.ladies_collection, name='ladies_collection'),
    path('kids_collection/', views.kids_collection, name='kids_collection'),
    path('phones_tablets/', views.phones_tablets, name='phones_tablets'),
    path('laptops/', views.laptops, name='laptops'),
    path('appliances_machinery/', views.appliances_machinery, name='appliances_machinery'),
    path('accessories/', views.accessories, name='accessories'),
    path('dining_lounge/', views.dining_lounge, name='dining_lounge'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('bedroom/', views.bedroom, name='bedroom'),
    path('bathroom/', views.bathroom, name='bathroom'),
    path('skin_care/', views.skin_care, name='skin_care'),
    path('hair_products/', views.hair_products, name='hair_products'),
    path('fragrances/', views.fragrances, name='fragrances'),
    path('cars/', views.cars, name='cars'),
    path('trucks/', views.trucks, name='trucks'),
    path('vehicle_parts/', views.vehicle_parts, name='vehicle_parts'),
    path('event_services/', views.event_services, name='event_services'),
    path('food_services/', views.food_services, name='food_services'),
    path('other_services/', views.other_services, name='other_services'),
    path('other/', views.other, name='other'),
    path('men_collection_hotdeals/', views.men_collection_hotdeals, name='men_collection_hotdeals'),
    path('ladies_collection_hotdeals/', views.ladies_collection_hotdeals, name='ladies_collection_hotdeals'),
    path('kids_collection_hotdeals/', views.kids_collection_hotdeals, name='kids_collection_hotdeals'),
    path('phones_tablets_hotdeals/', views.phones_tablets_hotdeals, name='phones_tablets_hotdeals'),
    path('laptops_hotdeals/', views.laptops_hotdeals, name='laptops_hotdeals'),
    path('appliances_machinery_hotdeals/', views.appliances_machinery_hotdeals, name='appliances_machinery_hotdeals'),
    path('accessories_hotdeals/', views.accessories_hotdeals, name='accessories_hotdeals'),
    path('dining_lounge_hotdeals/', views.dining_lounge_hotdeals, name='dining_lounge_hotdeals'),
    path('kitchen_hotdeals/', views.kitchen_hotdeals, name='kitchen_hotdeals'),
    path('bedroom_hotdeals/', views.bedroom_hotdeals, name='bedroom_hotdeals'),
    path('bathroom_hotdeals/', views.bathroom_hotdeals, name='bathroom_hotdeals'),
    path('skin_care_hotdeals/', views.skin_care_hotdeals, name='skin_care_hotdeals'),
    path('hair_products_hotdeals/', views.hair_products_hotdeals, name='hair_products_hotdeals'),
    path('fragrances_hotdeals/', views.fragrances_hotdeals, name='fragrances_hotdeals'),
    path('cars_hotdeals/', views.cars_hotdeals, name='cars_hotdeals'),
    path('trucks_hotdeals/', views.trucks_hotdeals, name='trucks_hotdeals'),
    path('vehicle_parts_hotdeals/', views.vehicle_parts_hotdeals, name='vehicle_parts_hotdeals'),
    path('event_services_hotdeals/', views.event_services_hotdeals, name='event_services_hotdeals'),
    path('food_services_hotdeals/', views.food_services_hotdeals, name='food_services_hotdeals'),
    path('other_services_hotdeals/', views.other_services_hotdeals, name='other_services_hotdeals'),
    path('other_hotdeals/', views.other_hotdeals, name='other_hotdeals'),
    path('other_electronics/', views.other_electronics, name='other_electronics'),
    path('other_beauty_cosmetics/', views.other_beauty_cosmetics, name='other_beauty_cosmetics'),
    path('other_vehicles/', views.other_vehicles, name='other_vehicles'),
    path('other_homeware/', views.other_homeware, name='other_homeware'),
    path('other_electronics_hotdeals/', views.other_electronics_hotdeals, name='other_electronics_hotdeals'),
    path('other_beauty_cosmetics_hotdeals/', views.other_beauty_cosmetics_hotdeals, name='other_beauty_cosmetics_hotdeals'),
    path('other_vehicles_hotdeals/', views.other_vehicles_hotdeals, name='other_vehicles_hotdeals'),
    path('other_homeware_hotdeals/', views.other_homeware_hotdeals, name='other_homeware_hotdeals'),

]