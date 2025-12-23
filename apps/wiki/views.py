from django.shortcuts import render


# Create your views here.
def wiki_page_view(request):
    return render(request, "wiki/wiki.html")
