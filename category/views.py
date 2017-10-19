from django.shortcuts import render, get_object_or_404

from .models import Category


def cat_list(request):
    return render(request, 'cat_list.html', {'categories': Category.objects.all})


def category(request, cat_name):
    cat = get_object_or_404(Category, title=cat_name)
    return render(request, 'category.html', {'category': cat})
