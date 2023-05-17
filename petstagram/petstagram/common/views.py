from django.shortcuts import render


def show_index(request):
    return render(request, 'common/home-page.html')
