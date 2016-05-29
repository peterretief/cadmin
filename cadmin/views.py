from django.shortcuts import render

def client_list(request):
    return render(request, 'cadmin/client_list.html', {})


# Create your views here.
