from django.shortcuts import render
from django.views.generic import View
from .models import UserModel
from django.http import JsonResponse
# Create your views here.

class GetAllUsersView(View):
    model = UserModel
    def get(self, request, *args, **kwargs):
        data = list(UserModel.objects.values())
        print('data', data)
        return JsonResponse({'data': data})
    
class GetUserView(View):
    model = UserModel
    def get(self, request, *args, **kwargs):
        name = request.GET['name']
        data = list(UserModel.objects.filter(name=name).values())
        return JsonResponse({'data': data})

class CreateUserView(View):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('name', '') 
            email = request.POST.get('email', '')
            UserModel.objects.create(name=name, email=email)
            return JsonResponse({
                'status': 'success',
                'message': 'New User Created'
            })
        return JsonResponse({
                'status': 'error',
                'message': 'Getting error while creating user'
        })
    
class DeleteUserView(View):
    def delete(self, request, *args, **kwargs):
        if request.method == 'DELETE':
            name = request.GET['name']
            UserModel.objects.filter(name=name).delete()
            return JsonResponse({
                'status': 'success',
                'message': 'User is deleted successfully'
            })
        return JsonResponse({
                'status': 'error',
                'message': 'Getting error while creating user'
        })
    
class EditUserView(View):
    model = UserModel

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.GET['name']
            email = request.POST.get('email', '')
            data = UserModel.objects.filter(name=name).first()
            data.email = email
            data.save()
            return JsonResponse({
                'status': 'success',
                'message': 'User data is updated successfully'
            })
        return JsonResponse({
                'status': 'error',
                'message': 'Getting error while updating user'
        })