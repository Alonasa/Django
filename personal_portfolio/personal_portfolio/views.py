from django.shortcuts import render
from django.http.response import HttpResponse, Http404


def view(request):
    return render(request, 'personal_portfolio/base-template.html')


months = {
    "january":  "Eat all dishes after NY party",
    "february": "Cook pancakes",
    "march":    "Greet Sisters with their birthday"
}


def dynamic(request, month):
    check = month.lower()
    if check in months:
        return HttpResponse(months[check])
    else:
        raise Http404("Page not found")


def raise_404(request, exception):
    return render(request, "404.html", status=404)
