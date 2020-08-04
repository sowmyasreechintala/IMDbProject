from django.shortcuts import render,redirect
from adminn.models import AdminModel
from django.core.paginator import Paginator
from userapp.models import UserModel
from django.contrib import messages
# Create your views here.
def userIndex(request):
    result=AdminModel.objects.all()
    pa = Paginator(result, 5)
    page_no = request.GET.get("page_no", 1)
    page = pa.page(page_no)
    paa = Paginator(result, 3)
    pagee_no2 = request.GET.get("pagee_no2", 1)
    pagee = paa.page(page_no)
    return render(request,"userIndex.html",{"data":AdminModel.objects.all,"page":page,"pagee":pagee})


def user_signin(request):
    return render(request,"user_login.html")


def trailer_play(request):
    idno=request.GET.get("idno")
    res=AdminModel.objects.filter(movie_id=idno)
    print(res)
    return render(request,"trailer_play.html",{"data":res})


def search(request):
    titleee=request.POST.get("search")
    print(titleee)
    res=AdminModel.objects.filter(title=titleee)
    if res:
        print(res)
        return render(request,"search.html",{"data":res})
    else:
        messages.error(request,"Invalid Movie tile")
        return redirect('userhome')


def watch_list_page(request):
    return render(request,"watch_list_page.html",{"data":UserModel.objects.all()})
def add_to_watchlist(request):
    movid=request.GET.get("movieid")
    print(movid,type(movid))
    res=AdminModel.objects.filter(id=movid)
    for x in res:
        print(x.movie_id,x.title)

        UserModel(movie_id=x.movie_id, title=x.title, poster=x.poster, year=x.year, length=x.length, rating=x.rating,
               rating_votes=x.rating_votes, plot=x.plot, video_link=x.video_link, trailer_id=x.trailer_id).save()
    return redirect('userhome')