from django.shortcuts import render
from django.http import HttpResponse

filled_forms = [
    {
        'from': 'Joe',
        'to': 'Josh',
        'date': '2020-05-20',
        'subject': 'purchase'

    },
    {
        'from': 'Joe',
        'to': 'Will',
        'date': '2020-05-21',
        'subject': 'purchase 1'

    }
]

def home(request):
    context = {
        'filled_forms': filled_forms
    }
    return render(request, 'form/home.html', context)

def form(request):
    return render(request, 'form/form.html')