from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages



def index(request):
    users = Users.objects.all()
    return render(request, 'index.html', {'users': users})

def about(request):
    return render(request, 'about.html')
def gallery(request):
    return render(request, 'gallery.html')
def register(request):
    if request.method == 'POST':
        name = request.POST.get('jina')
        email = request.POST.get('arafa')
        password = request.POST.get('siri')
        gender = request.POST.get('jinsia')
        user_data = Users(name=name, email=email, password=password, gender=gender)
        user_data.save()
        messages.success(request, 'Your account has been created successfully!')


        return redirect('home-url')

    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')


def delete_user(request, id):
    user = Users.objects.get(id=id)
    user.delete()
    messages.success(request, 'Your account has been deleted successfully!')
    return redirect('home-url')

def update_user(request, id):
    user = Users.objects.get(id=id)
    if request.method == 'POST':
        # receive edited data from the browser
        name = request.POST.get('jina')
        email = request.POST.get('arafa')
        gender = request.POST.get('jinsia')
        password = request.POST.get('siri')
        # update the retrived user data with the edited data

        user.name = name
        user.email = email
        user.gender = gender
        user.password = password
        # return the data back to the database
        user.save()
        messages.success(request, 'Your account has been updated successfully!')
        return redirect('home-url')
    return render(request, 'update.html', {'user': user})
