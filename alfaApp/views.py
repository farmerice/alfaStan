from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Defect
from .forms import PostForm

def defect_list(request):
    defects = Defect.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'alfaApp/defect_list.html', {'defects':defects})

def defect_detail(request, pk):
    defect = get_object_or_404(Defect, pk=pk)
    return render(request, 'alfaApp/defect_detail.html', {'defect': defect})

def defect_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            defect = form.save(commit=False)
            defect.author = request.user
            defect.published_date = timezone.now()
            defect.save()
            return redirect('defect_detail', pk=defect.pk)
    else:
        form = PostForm()
    return render(request, 'alfaApp/defect_edit.html', {'form': form})


def defect_edit(request, pk):
    defect = get_object_or_404(Defect, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=defect)
        if form.is_valid():
            defect = form.save(commit=False)
            defect.author = request.user
            defect.published_date = timezone.now()
            defect.save()
            return redirect('defect_detail', pk=defect.pk)
    else:
        form = PostForm(instance=defect)
    return render(request, 'alfaApp/defect_edit.html', {'form': form})
