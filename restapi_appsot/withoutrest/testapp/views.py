from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# this function gives html response
def emp_data_view(request):
    emp_data = {
        'eno': 100,
        'ename': 'Dip',
        'esal': 10000,
        'eaddr': 'Bhola',
    }
    resp = '<h1>Employee Number:{}<br>Employee Name:{}<br>Employee Salary:{}<br>Employee Address:{}</h1>'.format(
        emp_data['eno'], emp_data['ename'], emp_data['esal'], emp_data['eaddr'])

    return HttpResponse(resp)


import json


# this function gives jason response
def emp_data_jsonview(request):
    emp_data = {
        'eno': 100,
        'ename': 'Dip',
        'esal': 10000,
        'eaddr': 'Bhola',
    }
    json_data = json.dumps(emp_data)

    return HttpResponse(json_data, content_type='application/json')


from django.http import JsonResponse


# this function internally convert python dictionary directly in jason format
def emp_data_jsonview2(request):
    emp_data = {
        'eno': 100,
        'ename': 'Dip',
        'esal': 10000,
        'eaddr': 'Bhola',
    }

    return JsonResponse(emp_data)


# class based view
from django.views.generic import View
from testapp.mixins import HttpResponseMixin


class JasonCBV(HttpResponseMixin, View):
    def get(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from get method'})
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from post method'})
        return self.render_to_http_response(json_data)

    def put(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from put method'})
        return self.render_to_http_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({'msg': 'This is from delete method'})
        return self.render_to_http_response(json_data)
