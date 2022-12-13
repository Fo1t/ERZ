import asyncio
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Object.models import Date, General, Object, Apartment
from Areal.models import Region, District, Settlement, Street
from Developer.models import Developer
from django.core.paginator import Paginator
from Developer.forms import SearchDeveloperForm, SearchGeneralForm

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from fake_useragent import UserAgent
from tqdm import tqdm
import random
import time
from threading import Thread


def MainPage(request):
    data = {}
    developer_list = []
    if request.method == 'GET':
        form = SearchDeveloperForm()
        for developer in Developer.objects.all():
            if General.objects.filter(brand=developer).exists():
                obj_count = len(General.objects.filter(brand=developer))
            developer_list.append(
                {
                    'developer': developer,
                    'obj_count': obj_count
                }
            )
        data['form'] = form
    else:
        form = SearchDeveloperForm(request.POST)
        #form.name.initial = 123
        #dict_request = dict(request.POST)
        #print(f'{form=}')
        #print(f'{request.POST.get("developer_name")=}') 
        dev_name = request.POST.get('developer_name')
        dev_address = request.POST.get('developer_address')
        dev_website = request.POST.get('developer_site')
        #print(f'{dev_name=}\n{dev_address=}\n{dev_website=}\n')
        if dev_name == '' and dev_address == '' and dev_website == '':
            return redirect('./')
        if Developer.objects.filter(name__icontains=dev_name).exists():
            if dev_name != '':
                for developer in Developer.objects.filter(name__icontains=dev_name):
                   obj_count = 0
                   if General.objects.filter(brand=developer).exists():
                        obj_count = len(General.objects.filter(brand=developer))
                   developer_list.append(
                        {
                            'developer': developer,
                            'obj_count': obj_count
                        }
                    )
        if Developer.objects.filter(address__icontains=dev_address).exists():
            if dev_address != '':
                for developer in Developer.objects.filter(address__icontains=dev_address):
                   obj_count = 0
                   if General.objects.filter(brand=developer).exists():
                        obj_count = len(General.objects.filter(brand=developer))
                   developer_list.append(
                        {
                            'developer': developer,
                            'obj_count': obj_count
                        }
                    )
        if Developer.objects.filter(website__icontains=dev_website).exists():
            if dev_website != '':
                for developer in Developer.objects.filter(website__icontains=dev_website):
                   obj_count = 0
                   if General.objects.filter(brand=developer).exists():
                        obj_count = len(General.objects.filter(brand=developer))
                   developer_list.append(
                        {
                            'developer': developer,
                            'obj_count': obj_count
                        }
                    )
        print(f'{dev_name=}\n{dev_address=}\n{dev_website=}')
        data['form'] = form
    paginator = Paginator(developer_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    return render(request, 'index.html', data)


def DeveloperPage(request, developer_id):
    data = {}
    genegal_list = []
    if request.method == 'GET':
        data['form'] = SearchGeneralForm()
        if Developer.objects.filter(id=developer_id).exists():
            developer = Developer.objects.get(id=developer_id)
            data['developer'] = developer
            if General.objects.filter(brand=developer).exists():
                genegal_list = General.objects.filter(brand=developer)
    else:
        data['form'] = SearchGeneralForm(request.POST)
        general_name = request.POST.get('name')
        general_address = request.POST.get('address')
        if Developer.objects.filter(id=developer_id).exists():
            developer = Developer.objects.get(id=developer_id)
            data['developer'] = developer
            general_name_list = []
            general_address_list = []
            if general_name == '' and general_address == '':
                genegal_list = General.objects.filter(brand=developer)
            else:
                if general_name != '':
                    general_name_list = list(General.objects.filter(brand=developer, name__icontains=general_name))
                if general_address != '':
                    general_address_list = list(General.objects.filter(brand=developer, address__icontains=general_address))
                genegal_list = general_name_list + general_address_list
    paginator = Paginator(genegal_list, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    return render(request, 'developer.html', data)


def ObjectPage(request, general_id):
    data = {}
    if General.objects.filter(id=general_id).exists():
        general = General.objects.get(id=general_id)
        data['general'] = general
        data['objects'] = Object.objects.filter(general=general)
    return render(request, 'object.html', data)


def ApargPage(request, object_id):
    data = {}
    if Object.objects.filter(id=object_id).exists():
        object = Object.objects.get(id=object_id)
        data['object'] = object
        data['apartments'] = Apartment.objects.filter(object=object)
    return render(request, 'apartment.html', data)


    # for dev in tqdm(Developer.objects.all()):
    #     if General.objects.filter(brand=dev).exists():
    #         for general in General.objects.filter(brand=dev):
    #             if Object.objects.filter(general=general).exists():
    #                 for obj in Object.objects.filter(general=general):
    #                     if Apartment.objects.filter(object=obj).exists():
    #                         pass
    #                     else:
    #                         obj.delete()
    # for dev in tqdm(Developer.objects.all()):
    #     if General.objects.filter(brand=dev).exists():
    #         for general in General.objects.filter(brand=dev):
    #             if Object.objects.filter(general=general).exists():
    #                 pass
    #             else:
    #                 general.delete()
    # for dev in tqdm(Developer.objects.all()):
    #     if General.objects.filter(brand=dev).exists():
    #         pass
    #     else:
    #         dev.delete() 