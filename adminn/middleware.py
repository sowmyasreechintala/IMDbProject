# import requests
# import json
# class Api_Class:
#     def __init__(self,get_response):
#         self.get_response=get_response
#         print("I am constructor")
#         url = "https://imdb8.p.rapidapi.com/title/get-most-popular-movies"
#
#         querystring = {"purchaseCountry": "India", "homeCountry": "India", "currentCountry": "India"}
#
#         headers = {
#             'x-rapidapi-host': "imdb8.p.rapidapi.com",
#             'x-rapidapi-key': "2e8a51a7f3msh91114ce328844d3p1642dejsnea93cc678a25"
#         }
#
#         response = requests.request("GET", url, headers=headers, params=querystring)
#
#         data = json.loads(response.text)
#         list_data = []
#         count = 0
#         for x in data:
#             movie_id = x.split('/')[2]
#
#             url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/"+movie_id
#
#             headers = {
#                 'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
#                 'x-rapidapi-key': "2e8a51a7f3msh91114ce328844d3p1642dejsnea93cc678a25"
#             }
#
#             response = requests.request("GET", url, headers=headers)
#             dict_data = json.loads(response.text)
#             if dict_data['title'] and dict_data['poster']:
#                 list_data.append(dict_data)
#                 count += 1
#                 if count == 5:
#                     break
#
#         json.dump(list_data,open('adminapp/raw/MovieOnlineMiddle.json','w'))
#         print('Data Written To File')
#
#
#         # for x in dict_data:
#         #     k="https://imdb8.p.rapidapi.com/title/get-most-popular-movies"
#         #     print(k.x)
#             # self.get_response = get_response
#             # url="https://imdb8.p.rapidapi.com/title/get-most-popular-movies/x"
#             # response = requests.request("GET", url, headers=headers, params=querystring)
#             # print(response.text)
#         # print("hi")
#         # json.dump(dict_data,open("adminapp/raw/MovieOnlineMiddle","w"))
#         # print("data is written")
#     def __call__(self,request ,*args, **kwargs):
#         response=self.get_response(request)
#         print("Iam call")
#         return response
