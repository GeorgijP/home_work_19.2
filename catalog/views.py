from django.shortcuts import render

from catalog.models import Category


# Create your views here.

def home(request):
    category_list = Category.objects.all()

    context = {
        'object_list': category_list
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')
