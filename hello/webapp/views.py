from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from webapp.models import List, status_choices
# Create your views here.

def index_view(request):
    lists = List.objects.all()
    return render(request, 'index.html', context={'lists': lists})

def list_view(request, pk):
    # list_id = request.GET.get('id')
    # list = List.objects.get(id=list_id)
    list = List.objects.get(id=pk)
    return render(request, 'list_view.html', context={'list': list})

def to_do_list(request):
    if request.method == 'GET':
        return render(request, 'to_do_list.html', {'status': status_choices})
    elif request.method == "POST":
        describe = request.POST.get("describe")
        status = request.POST.get('status')
        date_of_completion = request.POST.get('date of complection')

        list = List.objects.create(
            describe=describe,
            status=status,
            date_of_completion=date_of_completion

        )
        # return render(request, 'list_view.html', context={'list': list})
        return redirect('list-view', pk=list.id)