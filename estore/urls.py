"""estore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store_information.urls')),
    path('accounts/', include('account.urls')),
    path('search/', include('search.urls')),
    path('sort/', include('sorting.urls')),
    path('edit/', include('edit.urls')),
    path('sort_estore/', include('sorting_estore.urls')),
    path('estore_estore_sort/', include('estore_estore_sort.urls')),
    path('payments/', include('payment.urls'))
]