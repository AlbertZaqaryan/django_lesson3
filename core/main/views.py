from django.shortcuts import render
from .models import Category
# Create your views here.

def index(request):
    cateory_list = Category.objects.all()
    product_list = Category.objects.filter()
    return render(request, 'index.html', context={
        'category_list':cateory_list,
        'product_list':product_list
    })