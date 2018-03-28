from django.shortcuts import render
from api.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# VIEWS
def index(request):
    page="trending"
    query_set_list = Post.objects.order_by("tim")

    paginator = Paginator(query_set_list, 12)

    page = request.GET.get('page')
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        query_set = paginator.page(1)
    except EmptyPage:
        query_set = paginator.page(paginator.num_pages)
    context = {
        "posts":query_set
    }
    return render(request, 'api/index.html', context)



def latest(request):
    page="trending"
    query_set_list = Post.objects.order_by("-tim")

    paginator = Paginator(query_set_list, 12)

    page = request.GET.get('page')
    try:
        query_set = paginator.page(page)
    except PageNotAnInteger:
        query_set = paginator.page(1)
    except EmptyPage:
        query_set = paginator.page(paginator.num_pages)
    context = {
        "posts":query_set
    }
    return render(request, 'api/index.html', context)








#django only load one link away at a time?

#FUTURE IMPROVEMENTS
#Use If-Modified-Since when doing your requests.
#Switch from time to tim
#last_lowest_no secondary check to deal with inaccurate pin timestamps
#add comment limit to lower number of api calls
#hash the thumbnail


