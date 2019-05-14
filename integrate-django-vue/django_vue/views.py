from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, template_name='index.html')


def simple_api_view(request):
    response = JsonResponse({
        'data': [
            'You get an phrase from the API!',
            'And you get a phrase from the API!',
            'And you get a phrase from the API!',
            'And you get a phrase from the API!',
            'And you get a phrase from the API!',
        ]
    })
    return response
