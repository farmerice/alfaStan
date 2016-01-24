from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Defect

def defect_list(request):
    defects = Defect.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'alfaApp/defect_list.html', {'defects':defects})

def defect_detail(request, pk):
    defect = get_object_or_404(Defect, pk=pk)
    return render(request, 'alfaApp/defect_detail.html', {'defect': defect})
