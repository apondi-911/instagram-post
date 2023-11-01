from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import NewPostForm
from django.contrib.auth.models import User

from .models import Post, Tag, Follow, Likes


# Create your views here.
def NewPost(request):
    user = request.user

    tags_obj = []

    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')
            tag_form = form.cleaned_data.get('tags')
            tag_list = list(tag_form.split(','))

            for tag in tag_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_obj.append(t)
            p, created = Post.objects.get_or_create(picture=picture, caption=caption, user=user)
            p.tags.set(tags_obj)
            p.save()
            return redirect('profile', request.user.username)
    else:
        form = NewPostForm()
    context = {
        'form': form
    }
    return render(request, 'post.html', context)
