from django.shortcuts import render, redirect
from django.urls import reverse

from webapp.models import List, status_choices
# Create your views here.

def index_view(request):
    lists = List.objects.all()
    return render(request, 'index.html', context={'lists': lists})

def list_view(request, pk):

    list = List.objects.get(id=pk)
    return render(request, 'list_view.html', context={'list': list})

def to_do_list(request):
    if request.method == 'GET':
        return render(request, 'to_do_list.html', {'status': status_choices})
    elif request.method == "POST":
        describe = request.POST.get("describe")
        status = request.POST.get('status')
        date_of_completion = request.POST.get('date_of_complection')
        description = request.POST.get('description')

        if not description:
            description=None
        if not date_of_completion:
            date_of_completion=None
        if not describe:
            describe=None
        if not status:
            status=None

        list = List.objects.create(
            describe=describe,
            status=status,
            date_of_completion=date_of_completion,
            description=description

        )

        return redirect('list-view', pk=list.id)