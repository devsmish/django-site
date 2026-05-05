from django.http import HttpRequest, HttpResponse


def greetings(request: HttpRequest) -> HttpResponse:
    username = 'Sergio'
    return HttpResponse(f"Hello, {username}!")
