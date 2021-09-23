from django.shortcuts import render
from .models import *

def show_main_page(request):
    queryset = TestTable.objects.all()
    return render(request, 'test_table/index.html', {'queryset': queryset})
