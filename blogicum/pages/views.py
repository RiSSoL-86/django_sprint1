from django.shortcuts import render


def about(request):
    """О проекте"""
    return render(request, 'pages/about.html')


def rules(request):
    """Наши правила"""
    return render(request, 'pages/rules.html')
