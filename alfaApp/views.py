from django.shortcuts import render
from django.utils import timezone
from .models import Defect

def defect_list(request):
    defects = Defect.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'alfaApp/defect_list.html', {'defects':defects})
