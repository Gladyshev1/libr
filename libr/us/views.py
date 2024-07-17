from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Profile
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            us = form.save()
            login(request, us)
            return redirect('/main')
    form = NewUserForm()
    context = {"form": form}
    return render(request, "us/reg.html", context)