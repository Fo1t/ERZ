# import asyncio
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from Object.models import Date, General, Object, Apartment
# from Areal.models import Region, District, Settlement, Street
# from Developer.models import Developer
# from django.core.paginator import Paginator
# from Developer.forms import SearchDeveloperForm

# import requests
# from bs4 import BeautifulSoup as bs
# import pandas as pd
# from fake_useragent import UserAgent
# from tqdm import tqdm
# import random
# import time
# from threading import Thread


# def MainPage(request):
#     data = {}
#     developer_list = []
#     if request.method == 'GET':
#         form = SearchDeveloperForm()
#         for developer in Developer.objects.all():
#             if General.objects.filter(brand=developer).exists():
#                 obj_count = len(General.objects.filter(brand=developer))
#             developer_list.append(
#                 {
#                     'developer': developer,
#                     'obj_count': obj_count
#                 }
#             )
#         data['form'] = form
#     else:
#         form = SearchDeveloperForm(request.POST)
#         #form.name.initial = 123
#         dict_request = dict(request.POST)
#         #print(f'{form=}')
#         #print(f'{request.POST=}') 
#         dev_name = dict_request['developer_name'][0]
#         dev_address = dict_request['developer_address'][0]
#         dev_website = dict_request['developer_site'][0]
#         if dev_website == '' and dev_address == '' and dev_website == '':
#             return redirect('./')
#         if Developer.objects.filter(name__icontains=dev_name).exists():
#             if dev_name != '':
#                 for developer in Developer.objects.filter(name__icontains=dev_name):
#                    obj_count = 0
#                    if General.objects.filter(brand=developer).exists():
#                         obj_count = len(General.objects.filter(brand=developer))
#                    developer_list.append(
#                         {
#                             'developer': developer,
#                             'obj_count': obj_count
#                         }
#                     )
#         if Developer.objects.filter(address__icontains=dev_address).exists():
#             if dev_address != '':
#                 for developer in Developer.objects.filter(address__icontains=dev_address):
#                    obj_count = 0
#                    if General.objects.filter(brand=developer).exists():
#                         obj_count = len(General.objects.filter(brand=developer))
#                    developer_list.append(
#                         {
#                             'developer': developer,
#                             'obj_count': obj_count
#                         }
#                     )
#         if Developer.objects.filter(website__icontains=dev_website).exists():
#             if dev_website != '':
#                 for developer in Developer.objects.filter(website__icontains=dev_website):
#                    obj_count = 0
#                    if General.objects.filter(brand=developer).exists():
#                         obj_count = len(General.objects.filter(brand=developer))
#                    developer_list.append(
#                         {
#                             'developer': developer,
#                             'obj_count': obj_count
#                         }
#                     )
#         print(f'{dev_name=}\n{dev_address=}\n{dev_website=}')
#         data['form'] = form
#     paginator = Paginator(developer_list, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     data['page_obj'] = page_obj
#     return render(request, 'index.html', data)

# # def parce(request):
# #     # MAIN_URL = 'https://erzrf.ru/top-zastroyshchikov/rf?topType=0&date=221201'
# #     Object.objects.all().delete()
# #     Apartment.objects.all().delete()
# #     data = []
# #     for general in tqdm(General.objects.all()):
# #         Thread(target=thr, args=[general, data]).start()
# #         #asyncio.run(thr(general))
# #         time.sleep(random.random()/2)
        
# #     time.sleep(60)
# #     for dt in tqdm(data):
# #         if len(dt) == 3:
# #             if type(dt[1]) is not list:
# #                 dt[1].save()
# #             if len(dt[2]) == 4:
# #                 if type(dt[2][0]) is not list:
# #                     dt[2][0].save()
# #                 if type(dt[2][1]) is not list:
# #                     dt[2][1].save()
# #                 if type(dt[2][2]) is not list:
# #                     dt[2][2].save()
# #                 if type(dt[2][3]) is not list:
# #                     dt[2][3].save()
        
#         #for apt in dt[2]:
#         #    apt.save()
#     pass
#     # r = requests.get(MAIN_URL, headers=headers)
#     # soup = bs(r.text, "html.parser")
#     # last_page = int(soup.find_all('a', class_='page-link')[-1]['href'].split('&page=')[-1])
#     # url = 'https://erzrf.ru/erz-rest/api/v1/top-developers/developers'
#     # for index in tqdm(range(1, (last_page*20)+1, 20)):
#     #     raw = r'{"formDeveloper":{"_region":{"id":"rf","text":"РФ","additional":"0"},"_topType":{"id":"0","text":""},"_houseType":{"id":null,"text":""},"_date":{"id":"221201","text":"221201"},"_min":'+ str(index) + r',"_max":'+ str(index + 19) + r',"_buildVolume":{"text":""},"_ratingErz":null}}'
#     #     time.sleep(random.random()*3)
#     #     response = requests.post(url, data=raw.encode('utf8'), headers=headers)
#     #     response.raise_for_status()
#     #     jsonResponse = response.json()
#     #     for item in jsonResponse:
#     #         name = item['organizationName']
#     #         region = item['regionName']
#     #         if not Region.objects.filter(name=region).exists():
#     #             Region(name=region).save()
            
#     #         id = item['id']
#     #         if 'urlId' in item:
#     #             urlId = item['urlId']
#     #             parce_brend(urlId, name)
#     # return HttpResponse('Ok!', status=200)
            
# # def thr(general, data):
# #     ua = UserAgent()
# #     headers = {'accept': '*/*', 'user-agent': ua.firefox}
# #     name = general.name.split('ЖК ')[-1]
# #     url = f'https://erzrf.ru/erz-rest/api/v1/globalsearch/gk/{name}?min=1&max=1'
# #     response = requests.get(url, headers=headers)
# #     if response.status_code == 200:
# #         response.raise_for_status()
# #         jsonResponse = response.json()[0]
# #         url = f'https://erzrf.ru/erz-rest/api/v1/gk/full_cost_statistics/{jsonResponse["id"]}'
# #         if response.status_code == 200:
# #             response = requests.get(url, headers=headers)
# #             response.raise_for_status()
# #             jsonResponse2 = response.json()         
# #             for obje in jsonResponse2:
# #                 new_obj = Object(name=obje['objectName'],state=obje['state'],general=general)
# #                 dt = [general, new_obj]
# #                 #ob_temp = []
# #                 #ob_temp.append(new_obj)
# #                 #new_obj.save()
# #                 apart_list = []
# #                 for apart in obje['objectStatistics'][:4]:
# #                     if apart['apartmentsCount'] != '0':
# #                         apart_list.append(Apartment(rooms=apart['rooms'],min_square=apart['minSquare'],max_square=apart['maxSquare'],min_cost=apart['minApartmentCost'],max_cost=apart['maxApartmentCost'],coun=apart['apartmentsCount'],name=apart['objectName'],object=new_obj))
# #                 apart_list.append(apart_list)
# #                 dt.append(apart_list)
# #             data.append(dt)
# # def parce_brend(urlId, name):
# #     ua = UserAgent()
# #     url = f'https://erzrf.ru/erz-rest/api/v1/brand/{urlId}'
# #     headers = {'accept': '*/*', 'user-agent': ua.firefox}
# #     time.sleep(random.random()*3)
# #     response = requests.get(url, headers=headers)
# #     response.raise_for_status()
# #     jsonResponse = response.json()
# #     #new_developer = Developer()
# #     #print(f'{Developer.objects.exists()=}')
# #     if Developer.objects.filter(name=name, address=jsonResponse['address']).exists():
# #         new_developer = Developer.objects.filter(name=name, address=jsonResponse['address'])[0]
# #     else:
# #         new_developer = Developer(name=name,
# #                   address=jsonResponse['address'],
# #                   #phone=jsonResponse['salesDepartmentPhone'],
# #                   website=jsonResponse['site'],
# #                   )
# #         if 'salesDepartmentPhone' in jsonResponse:
# #             new_developer.phone = jsonResponse['salesDepartmentPhone']
# #         new_developer.save()
# #     #print(f'{jsonResponse["id"]=}\n{new_developer=}')
# #     if new_developer is None:
# #         #print(f'{Developer.objects.filter(name=name, address=jsonResponse["address"]).exists()=}')
# #         #print(f'{jsonResponse["id"]=}\n{new_developer=}')
# #         new_developer = Developer.objects.filter(name=name, address=jsonResponse['address'])
# #         #print(f'{new_developer=}')
# #         new_developer = Developer.objects.filter(name=name, address=jsonResponse['address'])[0]
# #         #print(f'{new_developer=}')
# #     gk_parce(jsonResponse['id'], new_developer)
# #     pass



# # def gk_parce(id, developer):
# #     ua = UserAgent()
# #     url = f'https://erzrf.ru/erz-rest/api/v1/gk/lists?region=vse-regiony&regionKey=0&organizationId={id}&min=1&max=-1'
# #     headers = {'accept': '*/*', 'user-agent': ua.firefox}
# #     time.sleep(random.random()*3)
# #     response = requests.get(url, headers=headers)
# #     response.raise_for_status()
# #     jsonResponse = response.json()
# #     for build in jsonResponse['build']:
# #         if not Date.objects.filter(year=build['maxFinishDate'].split(' ')[-1]).exists():
# #             for x in range(4):
# #                 Date(year=build['maxFinishDate'].split(' ')[-1],
# #                      quarter=str(x+1)
# #                      ).save()
# #         quarter = build['maxFinishDate'].split(' ')[0]
# #         quarters = {
# #             'I': '1',
# #             'II': '2',
# #             'III': '3',
# #             'IV': '4',
# #         }
# #         year=build['maxFinishDate'].split(' ')[-1]
# #         date = Date.objects.get(year=year, quarter=quarters[quarter])
# #         new_general = General(
# #             name=build['gkName'],
# #             type_of_development_group=build['complexType'],
# #             brand=developer,
# #             address=build['gkAddress'],
# #             end_of_residential_complex=date
# #         ).save()
#     #MAIN_URL = 'https://erzrf.ru/top-zastroyshchikov/rf?topType=0&date=221201'
#     #r = requests.get(MAIN_URL)
#     #soup = bs(r.text, "html.parser")
#     #last_page = soup.find_all('a', class_='page-link')[-1]
#     # for x in range(1990, 2070, 1):
#     #     for y in range(4):
#     #         Date(year=x, quarter=str(y+1)).save()
    
    
