from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .forms import ProfileForm,ProjectForm,RatingForm
from .models import Profile,Project,Rating
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def home(request):
    project = Project.objects.all()
    profile = Profile.objects.all()
    
    return render(request,'index.html',{"project":project,"profile":profile})

@login_required(login_url='/accounts/login/')
def myProfile(request,id):
    user = User.objects.get(id = id)
    profiles = Profile.objects.get(user = user)
   
    return render(request,'view_profile.html',{"profiles":profiles,"user":user,})

def profile(request):
    current_user = request.user
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect(home)

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

def project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()

        return redirect(home)

    else:
        form = ProjectForm()
    return render(request, 'project.html', {"form": form})

def view_Project(request,id):
    user = User.objects.get(id = id)
    projects = Project.objects.get(user = user)
    images = Image.objects.filter(user = user).all()
   
    return render(request,'view_project.html',{"user":user,"images":images})

def rating(request):
    current_user = request.user
    if request.method == 'POST':
        form = RatingForm(request.POST, request.FILES)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = current_user
            rating.save()

            return redirect(home)

    else:
        form = RatingForm()
    return render(request, 'comment.html', {"form": form})

# def comments(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = CommentsForm(request.POST, request.FILES)
#         if form.is_valid():
#             comments = form.save(commit=False)
#             comments.user = current_user
#             comments.save()

#             return redirect(home)

#     else:
#         form = CommentsForm()
#     return render(request, 'comment.html', {"form": form})


# def like(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = LikeForm(request.POST, request.FILES)
#         if form.is_valid():
#             likes = form.save(commit=False)
#             likes.user = current_user
#             likes.save()

#             return redirect(home)

#     else:
#         form = LikeForm()
#     return render(request, 'like.html', {"form": form})

# @login_required(login_url='/accounts/login/')

