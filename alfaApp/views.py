from django.shortcuts import render

def defect_list(request):
    return render(request, 'alfaApp/defect_list.html', {})
