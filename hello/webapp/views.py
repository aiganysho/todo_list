from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import List, status_choices
from webapp.form import ListForm, ListDeleteForm
# Create your views here.

def index_view(request):
    lists = List.objects.all()
    return render(request, 'index.html', context={'lists': lists})

def list_view(request, pk):

    list = List.objects.get(id=pk)
    return render(request, 'list_view.html', context={'list': list})

def to_do_list(request):
    if request.method == 'GET':
        form = ListForm()
        return render(request, 'to_do_list.html', {'status': status_choices, 'form': form})
    elif request.method == "POST":
        form = ListForm(data=request.POST)
        if form.is_valid():
            list = List.objects.create(
                describe=form.cleaned_data.get("describe"),
                description=form.cleaned_data.get("description"),
                status=form.cleaned_data.get("status"),
                date_of_completion=form.cleaned_data.get("date_of_completion")
            )
        # describe = request.POST.get("describe")
        # status = request.POST.get('status')
        # date_of_completion = request.POST.get('date_of_complection')
        # description = request.POST.get('description')
        #
        # if not description:
        #     description = None
        # if not date_of_completion:
        #     date_of_completion = None
        # if not describe:
        #     describe = None
        # if not status:
        #     status = None
        #
        # list = List.objects.create(
        #     describe=describe,
        #     status=status,
        #     date_of_completion=date_of_completion,
        #     description=description
        #
        # )

            return redirect('list-view', pk=list.id)
        return render(request, 'to_do_list.html', context={'form': form})

def list_update_view(request, pk):

    list = get_object_or_404(List, id=pk)

    if request.method == 'GET':
        form = ListForm(
            initial={
                'describe': list.describe,
                'description': list.description,
                'status': list.status,
                'date_of_completion': list.date_of_completion
            })
        return render(request, 'list_update.html',
                      context={'form': form, 'list': list})
    elif request.method == 'POST':
        form = ListForm(
            data=request.POST)
        if form.is_valid():
            list.describe = form.cleaned_data.get("describe")
            list.description = form.cleaned_data.get("description")
            list.status = form.cleaned_data.get("status")
            list.date_of_completion = form.cleaned_data.get("date_of_completion")
            list.save()
            return redirect('list-view', pk=list.id)
        return render(request, 'list_update.html', context={'form': form, 'list': list})

def list_delete_view(request, pk):

    list = get_object_or_404(List, id=pk)

    if request.method == 'GET':
        form = ListDeleteForm()
        return render(request, 'list_delete.html', context={'list': list, 'form': form})
    elif request.method == 'POST':
        form = ListDeleteForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['describe'] != list.describe:
                form.errors['describe'] = ["name of task don't match"]
                return render(request, 'list_delete.html', context={'list': list, 'form': form})

            list.delete()
            return redirect('list-lists')
        return render(request, 'list_delete.html', context={'list': list, 'form': form})