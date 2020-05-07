from django.views import View
from django.http  import JsonResponse
from django.db.models import Prefetch

from django.db import connection, reset_queries
import time
import functools

from .models      import (
    Category,
    Drink,
)

def query_debugger(func):

    @functools.wraps(func)
    def inner_func(*args, **kwargs):

        reset_queries()
        
        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func

# Create your views here.
class ProductView(View):
    @query_debugger
    def get(self, request, category_id):
        prefetch_qs = Category.objects.prefetch_related('drink_set')
        drinks = []
        for item in prefetch_qs:
            data = [ drink.name for drink in item.drink_set.filter(category__id=category_id)]
            drinks.append({'category_id':item.id, 'category_name':item.name, 'drinks':data})

        return JsonResponse({'data':drinks}, status=200)

class ProductPrefetchView(View):
    @query_debugger
    def get(self, request, category_id):
        prefetch_qs = Category.objects.prefetch_related(
            Prefetch('drink_set',queryset=Drink.objects.filter(category__id=category_id))    
        )
        drinks = []
        for item in prefetch_qs:
            data = [ drink.name for drink in item.drink_set.all()]
            drinks.append({'category_id':item.id, 'category_name':item.name, 'drinks':data})

        return JsonResponse({'data':drinks}, status=200)

