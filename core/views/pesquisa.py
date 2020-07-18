from django.shortcuts import render

def pesquisa(request):
    current_string = request.POST.get('current_string') if request.POST.get('current_string') else ''
    context = {
        'current_string': current_string
    }
    return render(request, 'pesquisa.html', context)