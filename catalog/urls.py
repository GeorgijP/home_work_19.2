from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ContactsListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='index'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
]