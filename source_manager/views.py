from django.http import HttpRequest, HttpResponse


def greetings(request: HttpRequest): -> HttpResponse
    name = 'Sergio'
    return HttpResponse(f"Hello, {name}!")
