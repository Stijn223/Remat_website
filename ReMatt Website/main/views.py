from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid text")

    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {"name": "test"})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data.get("name")
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})

def products(response):
    return render(response, "main/products.html", {})

def journey(response):
    return render(response, "main/journey.html", {})

def about_us(response):
    return render(response, "main/about_us.html", {})

def contact(response):
    return render(response, "main/contact.html", {})

def reviews(response):
    return render(response, "main/reviews.html", {})