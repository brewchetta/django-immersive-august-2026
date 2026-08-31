from django.shortcuts import render, redirect, get_object_or_404
from .models import ForumPost
from .forms import ForumPostForm

def home(request):
    context = { "forum_posts": ForumPost.objects.all() }
    return render( request, 'forum_app/home.html', context )

def create_post(request):
    if (request.method == "POST"):
        form = ForumPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum_home')
        context = { "form": form }
        return render(request, 'forum_app/create_post.html', context)

    form = ForumPostForm()
    context = { "form": form }
    return render(request, 'forum_app/create_post.html', context)

def edit_post(request, pk):
    post = get_object_or_404(ForumPost, pk=pk)

    if (request.method == "POST"):
        form = ForumPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('forum_home')
        context = { "form": form }
        return render(request, 'forum_app/edit_post.html', context)

    form = ForumPostForm(instance=post)
    context = { "form": form }
    return render(request, 'forum_app/edit_post.html', context)