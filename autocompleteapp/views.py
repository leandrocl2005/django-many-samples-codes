from django.shortcuts import render
from django.http import JsonResponse
from quotescrud.models import Quote

# Create your views here.
def index(request):
  return render(request, 'autocompleteapp/index.html')

def search_quotes(request):
    """everytime user inputs to search box, this function runs"""
    name = request.GET.get("name")
    name_set = set()
    if name:
        #collect every objects that contains the input text
        quote_objects = Quote.objects.filter(thinker__icontains=name)
        for quote in quote_objects:
            name_set.add(quote.thinker)
    return JsonResponse({'status':200, 'name':list(name_set)})

def result_quotes(request):
    """everytime user inputs to search box, this function runs"""
    name = request.GET.get("name")
    if name:
        #collect every objects that contains the input text
        quote_objects = Quote.objects.filter(thinker__icontains=name)

    return render(request, 'autocompleteapp/index.html', context={"quotes": quote_objects})