from django.views.generic import ListView

from catalog.models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/home.html'


class ContactsListView(ListView):
    model = Category
    template_name = 'catalog/contacts.html'
