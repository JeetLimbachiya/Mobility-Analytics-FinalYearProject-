from django.urls import path
from . import views

urlpatterns = [
    path('country/', views.country, name='country'),
    path('countrydelete<int:foo>/', views.countrydelete, name="countrydelete"),
    path('countryedit<int:foo>/', views.countryedit, name="countryedit"),

    path('state/', views.state, name='state'),
    path('statedelete<int:foo>/', views.statedelete, name="statedelete"),
    path('stateedit<int:foo>/', views.stateedit, name="stateedit"),

    path('city/', views.city, name='city'),
    path('citydelete<int:foo>/', views.citydelete, name="citydelete"),
    path('cityedit<int:foo>/', views.cityedit, name="cityedit"),

    path('cartype/', views.cartype, name='cartype'),
    path('cartypedelete<int:foo>/', views.cartypedelete, name="cartypedelete"),
    path('cartypeedit<int:foo>/', views.cartypeedit, name="cartypeedit"),

    path('driver/', views.driver, name='driver'),
    path('driverdelete<int:foo>/', views.driverdelete, name="driverdelete"),
    path('driveredit<int:foo>/', views.driveredit, name="driveredit"),

    path('update-profile/', views.updateProfile, name='update_profile'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard1/', views.dashboard1, name='dashboard1'),
    path('dashboard_static/', views.dashboard_static, name='dashboard_static'),

]
