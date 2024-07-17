from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import book
from .models import take

# Create your views here.
def index(request):
    pag = items = book.objects.all()

    itname = request.GET.get('sr')
    if (itname != '' and itname is not None):
        pag = items.filter(name__contains=itname)

    context = {
        'items': pag
    }
    return render(request, "osn/main.html", context)


def infbook(request, my_id):
    item = book.objects.get(id=my_id)

    context = {
        'item': item
    }
    return render(request, "osn/inf.html", context)


def add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        a = request.POST.get("au")
        des = request.POST.get("des")
        ko = request.POST.get("col")
        img = request.FILES['fi']

        item = book(name=name, author=a, col=ko, img=img, description=des)
        item.save()
        return redirect('/main')

    return render(request, "osn/add.html")


def upd(request, my_id):
    item = book.objects.get(id=my_id)
    if request.method == "POST":
        item.col = request.POST.get("col")
        item.name = request.POST.get("name")
        item.author = request.POST.get("au")
        item.description = request.POST.get("des")
        if(request.FILES.get('fi',item.img)):
            item.img = request.FILES.get('fi',item.img)



        item.save()
        q=item.id
        return redirect("/main/"+str(q))

    context = {
        'item': item
    }
    return render(request, "osn/upd.html", context)



def deli(request, my_id):
    item = book.objects.get(id=my_id)
    if request.method == "POST":
        item.delete()
        return redirect('/main')

    context = {
        'item': item
    }
    return render(request, "osn/del.html", context)
def te(request,my_id):
    if request.method == "POST":
        who1= request.user
        time = request.POST.get("time")
        kom1 = request.POST.get("kom")
        ch=book.objects.get(id=my_id)
        item = take(who=who1, when=time, kom=kom1,what=ch)
        item.save()
        return redirect('/main')

    return render(request, "osn/t.html")

def bookq(request):
    pag = items = take.objects.all()

    itname = request.GET.get('sr')
    if (itname != '' and itname is not None):
        pag = items.filter(name__contains=itname)

    context = {
        'items': pag
    }
    return render(request, "osn/book.html", context)
