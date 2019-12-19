from django.shortcuts import render
from django.views.generic import View
from testapp.utils import is_json
import json
from testapp.mixins import HttpResponseMixin,SerializeMixin
from testapp.models import Student
from testapp.forms import StudentForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class StudentCRUDCBV(SerializeMixin, HttpResponseMixin, View):

    def get_object_by_id(self,id):
        try:
            s = Student.objects.get(id=id)
            
        except Student.DoesNotExist:
            s = None
        return s  
        
    def get(self, request, *args, **kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg': 'please provide valid json data only'})
            return self.render_to_http_response(json_data, status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            std = self.get_object_by_id(id)
            if std is None:
                json_data=json.dumps({'msg': 'No matched record found with matched id'})
                return self.render_to_http_response(json_data, status=400)
            json_data=self.serialize([std,])
            return self.render_to_http_response(json_data,status=400)
        qs=Student.objects.all()
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg': 'please provide valid json data only'})
            return self.render_to_http_response(json_data, status=400)
        std_data=json.loads(data)
        form = StudentForm(std_data)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg': 'Resources Created Successfully'})
            return self.render_to_http_response(json_data, status=400)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)
    def put(self, request, *args, **kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg': 'please provide valid json data only'})
            return self.render_to_http_response(json_data, status=400)
        provided_data=json.loads(data)
        id=provided_data.get('id', None)
        if id is None:
            json_data=json.dumps({'msg': 'To perform updation, id is mandatory,plz provide'})
            return self.render_to_http_response(json_data, status=400)
        std=self.get_object_by_id(id)
        if std is None:
            json_data=json.dumps({'msg': 'No matched record found with the given id'})
            return self.render_to_http_response(json_data, status=400)
        orginal_data={
            'name':std.name,
            'rollno':std.rollno,
            'marks':std.marks,
            'gf':std.gf,
            'bf':std.bf
        }
        orginal_data.update(provided_data)
        form=StudentForm(orginal_data,instance=std)
        if form.is_valid():
            form.save()
            json_data=json.dumps({'msg': 'resources update successfully'})
            return self.render_to_http_response(json_data, status=400)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)

    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'please send valid json data only'})
            return self.render_to_http_response(json_data, status=400)
        provided_data=json.loads(data)
        id=provided_data.get('id', None)
        if id is not None:
            std=self.get_object_by_id(id)
            if std is None:
                json_data = json.dumps({'msg': 'The requested resource not available with matched id'})
                return self.render_to_http_response(json_data, status=404)
            status, deleted_item = std.delete()
            if status == 1:
                json_data = json.dumps({'msg': 'Resources Deleted Successfully'})
                return self.render_to_http_response(json_data, status=404)
            json_data = json.dumps({'msg': 'Unable to delete....plz try again'})
            return self.render_to_http_response(json_data) 
        json_data = json.dumps({'msg': ' to perform delation ID is mandatory,please provide'})
        return self.render_to_http_response(json_data, status=400) 