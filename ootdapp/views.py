from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from ootdapp.models import Write

# Create your views here.
def main(request):
    ootdapps=Write.objects
    return render(request, 'main.html', {'ootdapps':ootdapps})

def create(request):
    if request.method == 'POST':
        ootdapp=Write()
        ootdapp.title=request.POST['title']
        ootdapp.body=request.POST['body']
        ootdapp.image=request.FILES['image']
        ootdapp.pub_date=timezone.datetime.now()
        ootdapp.save()
        return redirect('main')
    else:
        return render(request, 'new.html')


def detail(request, pk):
    ootds = get_object_or_404(Write, pk=pk)
    return render(request, 'detail.html', {'ootds':ootds})