from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
# Create your views here.
from .models import Post
from .forms import PostForm
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def post_create(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance002 = form.save(commit=False)
#         print form.cleaned_data.get("title")
        instance002.save()
        messages.success(request, "Successfully Created", extra_tags="you_can_have_an_extra_tag_here")
        return HttpResponseRedirect(instance002.get_absolute_url())
    # else:
    #     messages.error(request, "Not Successfully Created")
    # once you open /posts/create/ it will check the form so at first it will turn to error, the else is useless
#     if request.method == "post":
#         title = request.POST.get("title")
#         Post.object.create(title=title)
    context = {
               "form": form,
               }
    return render(request, "post_form.html", context)

def post_detail(request, slug=None):
    instance001 = get_object_or_404(Post, slug=slug)
    
    context = {
        "title": instance001.title,
        "instance": instance001,
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset001_list = Post.objects.all()#.order_by("-timestamp")
#     if request.user.is_authenticated():
#         context = {
#             "title": "My User List"
#         }
#     else:
#         context = {
#             "object_list":queryset,
#             "title": "List"
#         }
    query = request.GET.get("q")
    if query:
    	queryset001_list = queryset001_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)
    		).distinct()
    paginator = Paginator(queryset001_list, 4) # Show 25 contacts per page
    page_name_change_yourself = "blabla"
    page = request.GET.get(page_name_change_yourself)
    #it will show up in url as ?page=xxx
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
            "object_list": queryset,
            "title": "List",
            "page_name_change_yourself": page_name_change_yourself,
        }
    return render(request, "post_list.html", context)
def post_update(request, slug):
    instance003 = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance003)
    if form.is_valid():
        instance003 = form.save(commit=False)
        instance003.save()
        messages.success(request, "<a href="">Item</a> Saved", extra_tags="html_safe")
        return HttpResponseRedirect(instance003.get_absolute_url())

    context = {
        "title": instance003.title,
        "instance": instance003,
        "form": form,
    }
    return render(request, "post_form.html", context)
def post_delete(request, slug=None):
    instance004 = get_object_or_404(Post,slug=slug)
    instance004.delete()
    messages.success(request,"Successfully deleted")
    return redirect('list')