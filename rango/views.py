from django.shortcuts import render
from rango.models import Category, Page


def index(request):
    context_dict = {}
    category = Category.objects.order_by('-likes')[:5]
    pages = Page.objects.order_by('-views')[:5]
    context_dict['categories'] = category
    context_dict['pages'] = pages
    return render(request, 'rango/index.html', context_dict)


def about(request):
    about_text = {'shorttext': "Rango says here is the about page."}
    return render(request, 'rango/about.html', about_text)


def category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request, 'rango/category.html', context_dict)
