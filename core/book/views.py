from django.shortcuts import render,redirect
from .models import Book
from .forms import BookForm

def index_name(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'index.html',context)

def detail_name(request):
    return render(request, 'detail.html')

def create_name(request):
    form=BookForm()
    

    if request.method == "POST":
        form = BookForm(request.POST)
        # print(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index.html')

    context = {
        "form":form
    }

    return render(request, 'template/create.html', context)

   