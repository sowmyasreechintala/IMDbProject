from django.contrib import messages
from django.shortcuts import render,redirect
from mysqlproject.settings import MOVIE_FILE
from adminn.models import AdminModel
import json
import requests
from adminn.models import AdminModel
import base64


def api_data(self):
    # self.get_response=get_response
    # print("I am constructor")
    url = "https://imdb8.p.rapidapi.com/title/get-most-popular-movies"

    querystring = {"purchaseCountry": "India", "homeCountry": "India", "currentCountry": "India"}

    headers = {
        'x-rapidapi-host': "imdb8.p.rapidapi.com",
        'x-rapidapi-key': "2e8a51a7f3msh91114ce328844d3p1642dejsnea93cc678a25"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)

    list_data = []
    for x in data:
        movie_id = x.split('/')[2]
        print(movie_id)

        url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/" + movie_id

        headers = {
            'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
            'x-rapidapi-key': "2e8a51a7f3msh91114ce328844d3p1642dejsnea93cc678a25"
        }

        response = requests.request("GET", url, headers=headers)
        dict_data = json.loads(response.text)
        if dict_data['title'] and dict_data['poster']:
            list_data.append(dict_data)
    print(list_data)
    json.dump(list_data, open('adminn/raw/MovieOnlineMiddle.json', 'w'))
    print('Data Written To File')
    AdminModel.objects.all().delete()
    for x in list_data:
        print(type(x["year"]))
        AdminModel.objects.create(movie_id=x["id"], title=x["title"],poster=x["poster"],year=x["year"],length=x["length"], rating=x["rating"], rating_votes=x["rating_votes"],plot=x['plot'], video_link=x["trailer"]["link"], trailer_id=x["trailer"]["id"])
    return redirect('view_all')

    # def __call__(self,request ,*args, **kwargs):
    #   response=self.get_response(request)
    #   print("Iam call")
    #   return response
def saveData(request):
    data = json.loads(open('adminn/raw/MovieOnlineMiddle.json').read())
    AdminModel.objects.all().delete()
    for x in data:
        print("HI",x['year'])
        AdminModel.objects.create(movie_id=x["id"], title=x["title"], poster=x["poster"], year=x["year"],
                                  length=x["length"], rating=x["rating"], rating_votes=x["rating_votes"],
                                  plot=x['plot'], video_link=x["trailer"]["link"], trailer_id=x["trailer"]["id"])
    return redirect('view_all')
def viewMovie(request):
    res = AdminModel.objects.all()
    return render(request,"index.html",{"data":AdminModel.objects.all()})

def deleteMovie(request):
    idd=request.GET.get("movieid")
    AdminModel.objects.filter(movie_id=idd).delete()
    return redirect('view_all')


# def imdb_data(request):
#     import http.client
#
#     conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")
#
#     headers = {
#         'x-rapidapi-host': "imdb8.p.rapidapi.com",
#         'x-rapidapi-key': "4422ecdd22msh0284eaac7d64721p1d830ejsn5fc033392fd1"
#     }
#
#     conn.request("GET", "/title/auto-complete?q=game%20of%20thr", headers=headers)
#
#     res = conn.getresponse()
#     data = res.read()
#
#     print(data.decode("utf-8"))
def updatemovie(request):
    movie_id = request.GET.get('movieid')
    print(movie_id)
    res = AdminModel.objects.get(movie_id=movie_id)
    return render(request,'update_movie.html',{'data':res})


def saveUpdate(request):
    movie_id = request.POST.get('movie_id')
    title = request.POST.get('title')
    year = request.POST.get('year')
    length = request.POST.get('length')
    rating = request.POST.get('rating')
    rating_votes = request.POST.get('rating_votes')
    image = request.FILES['image']
    plot = request.POST.get('plot')
    trailer = request.POST.get('trailer')
    AdminModel.objects.filter(movie_id=movie_id).update( title=title, poster=image, year=year,length=length, rating=rating, rating_votes=rating_votes, plot=plot, trailer_id=trailer)
    return redirect('view_all')
def newmovie(request):
    return render(request,"newmovie.html")
def save_movie(request):
    movie_id = request.POST.get('id')
    title = request.POST.get('title')
    year = request.POST.get('year')
    length = request.POST.get('length')
    rating = request.POST.get('rating')
    rating_votes = request.POST.get('rating_votes')
    image = request.FILES['image']
    plot = request.POST.get('plot')
    trailer = request.POST.get('trailer')
    AdminModel(movie_id=movie_id,title=title, poster=image, year=year, length=length,rating=rating, rating_votes=rating_votes, plot=plot,trailer_id=trailer).save()
    return redirect('view_all')

def search(request):
    search = request.POST.get('search') # getting movie from search bar
    try:
        movie = AdminModel.objects.get(title=search) #from db
        return render(request,'search.html',{'data':movie}) #
    except:
        messages.error(request,"No Movie Found")
        return redirect('main')