from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
import random, json, sqlite3
from .models import data

def forms_request(request):
    return render(request, "index.html")

def api_response(request):
        if request.method == 'POST':
            data_api_to_DB = json.loads(request.body)

            lines = data_api_to_DB.split(',\n')
            data_dict = {}
            for line in lines:
                key, value = line.split(': ')
                key = key.strip()
                value = value.strip()
                data_dict[key] = value
            manager = data_dict['Менеджер']
            lastName = data_dict['Фамилия']
            firstName = data_dict['Имя']
            middleName = data_dict['Отчество']
            measurements = data_dict['Измерения']
            fabricType = data_dict['Тип ткани']
            deliveryOption = data_dict['Способ доставки']

            data_to = data()
            data_to.manager = manager
            data_to.lastName = lastName
            data_to.firstName = firstName
            data_to.middleName = middleName
            data_to.measurements = measurements
            data_to.fabricType = fabricType
            data_to.deliveryOption = deliveryOption
            data_to.save()

        return HttpResponseRedirect('/')
