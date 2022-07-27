import os.path
import re

from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView




from .serializers import *
from .utils import *
from .forms import *


class Main(MainMenuMixin, TemplateView):
    template_name = 'main/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_cont = self.get_user_context(title='Главная')
        return dict(list(context.items()) + list(user_cont.items()))
#
# class ClientListView(generics.ListAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#
# class CatListView(APIView):
#     def get(self, request):
#         pk = request.query_params.get('id',None)
#
#         if pk:
#             query = EquipmentCat.objects.filter(client=pk).order_by('cat_name')
#         else:
#             query = EquipmentCat.objects.all()
#
#         return Response({'category': CatSerializer(query, many=True).data})
#
# class ColumnTaskAPIView(APIView):
#     def get(self, request):
#         columns = Columns.objects.all()
#         tasks = Tasks.objects.all()
#         return Response({'columns': ColumnSerializer(columns, many=True).data,
#                          'tasks': TasksSerializer(tasks, many=True).data,})



# ____________________________________________________________________________________________
# Класс для представления записей из модели TASKS
# class TaskViewSet(viewsets.ModelViewSet):
#     serializer_class = TasksSerializer
#     queryset = Tasks.objects.all()
#
#
#     #_______
#     # Декоратор @action используется для добавления доп методов обработки во Вьюсет
#
#     # methods - список поддерживаемых методов, detail=False - для возвращения списка а не одной записи
#     @action(methods=['get'], detail=False)
#     def participants(self, request):
#         p = request.query_params.get('p', None)
#         if p:
#             print(p)
#
#         else:
#             print(0)
#         parts = CustomUser.objects.all()
#         return Response({'participants': ParticipantsSerializer(parts, many=True).data})

    #///////

# ////////////////////////////////////////////////////////////////////////////////////////////


#
# class RegisterUser(MainMenuMixin, CreateView):
#     form_class = RegisterUserForm
#     template_name = 'main/register.html'
#     success_url = reverse_lazy('login')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user_cont = self.get_user_context(title='Регистрация')
#         return dict(list(context.items()) + list(user_cont.items()))
#
#     def post(self, request, *args, **kwargs):
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             form.instance.initials = (form.instance.first_name[0]).upper() + (form.instance.sur_name[0]).upper()
#             form.instance.username = (form.instance.first_name[0]).upper() + (form.instance.sur_name[0]).upper()
#             form.instance.img = request.FILES['img'] if request.FILES else 'user/default.png'
#
#             user.save()
#             return redirect(reverse_lazy('login'))
#         else:
#             return render(request, 'main/register.html', {'form': form})
#
class RegisterUser(MainMenuMixin, CreateView):
    success_url = reverse_lazy('login')
    def post(self, request, *args, **kwargs):
        req = request.POST


#
# class LoginUser(MainMenuMixin, LoginView):
#     form_class = LoginUserForm
#     template_name = 'main/login.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user_cont = self.get_user_context(title='Авторизация')
#         return dict(list(context.items()) + list(user_cont.items()))
#
#     def get_success_url(self):
#         return reverse_lazy('main')
#
#
# class UserProfile(MainMenuMixin, TemplateView):
#     template_name = 'main/profile.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user_cont = self.get_user_context(title='Профиль')
#         return dict(list(context.items()) + list(user_cont.items()))
#
#
# def logout_user(request):
#     logout(request)
#     return redirect('login')
#
# def _get_form(request, formcls, prefix):
#     data = request.POST if prefix in request.POST else None
#     return formcls(data, prefix=prefix)
#
# class TasksDKO(MainMenuMixin, CreateView):
#     template_name = 'main/task_page.html'
#     form_class = CreateTaskForm
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user'] = CustomUser.objects.filter(stage__stage_name__in=('Конструктор', 'Дизайнер'))
#         context['task'] = CustomUser.objects.all()
#         context['aform'] = CreateTaskForm()
#         context['bform'] = CreateComment()
#         context['comments'] = TaskComments.objects.all()
#
#         user_cont = self.get_user_context(title='ДКО')
#         return dict(list(context.items()) + list(user_cont.items()))
#
#
#
#     def post(self, request, *args, **kwargs):
#         aform = CreateTaskForm(request.POST)
#         bform =CreateComment(request.POST)
#
#         if 'aform' in request.POST:
#             if aform.is_valid():
#                 task = aform.save(commit=False)
#                 task.task_number_init = request.user.initials
#                 task.save()
#                 us = request.POST.getlist('participants1')
#                 for i in us:
#                     task.participants1.add(CustomUser.objects.get(pk=i))
#                 task.save()
#         elif 'bform' in request.POST:
#             if bform.is_valid():
#                 com = bform.save(commit=False)
#                 com.commentator = request.user.first_name + ' ' + request.user.sur_name
#                 com.task=Tasks.objects.get(id=request.POST['11'])
#                 com.save()
#         return redirect(reverse_lazy('dko'))
#
#
# class ClientEquipmentList(MainMenuMixin, ListView):
#     template_name = 'main/clientequipmentlist.html'
#     model = Equipment
#     form_class = CreateClient
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['clients'] = Client.objects.all().order_by('client_name')
#         context['alfabet'] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ'
#         context['clientform'] = CreateClient()
#         # context['eqform'] = CreateEquipment()
#         user_cont = self.get_user_context(title='Оборудование')
#         return dict(list(context.items()) + list(user_cont.items()))
#     #
#     def post(self, request, *args, **kwargs):
#         form = CreateClient(request.POST)
#         if form.is_valid():
#             com = form.save(commit=False)
#             com.client_slug = self.translateForSlug(com.client_name)
#             com.save()
#         return redirect(reverse_lazy('clientequip'))
#
#
#
# class CatEquipmentList(MainMenuMixin, ListView):
#     template_name = 'main/equipmentlist.html'
#     model = EquipmentCat
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['equip'] = EquipmentCat.objects.filter(client__client_slug=self.kwargs['cat_slug']).order_by('cat_name')
#         user_cont = self.get_user_context(title='Оборудование')
#         return dict(list(context.items()) + list(user_cont.items()))
#
#     def post(self, request, *args, **kwargs):
#         form = CreateEquipmentCat(request.POST)
#         cl_id = (Client.objects.filter(client_slug=self.kwargs['cat_slug']))[0]
#         print(cl_id)
#         if form.is_valid():
#             com = form.save(commit=False)
#             com.cat_slug = self.translateForSlug(com.cat_name)
#             com.client_id = cl_id.id
#             com.save()
#         return redirect(reverse_lazy('cat_equip', kwargs={'cat_slug':self.kwargs['cat_slug']}))
#
#
# class EquipmentList(MainMenuMixin, ListView):
#     template_name = 'main/equipmentValueList.html'
#     model = Equipment
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['equip'] = Equipment.objects.filter(client__client_slug=self.kwargs['cat_slug']).order_by('cat_name')
#         user_cont = self.get_user_context(title='Оборудование')
#         return dict(list(context.items()) + list(user_cont.items()))
#
#     def post(self, request, *args, **kwargs):
#         form = CreateEquipmentCat(request.POST)
#         cl_id = (Client.objects.filter(client_slug=self.kwargs['cat_slug']))[0]
#         print(cl_id)
#         if form.is_valid():
#             com = form.save(commit=False)
#             com.cat_slug = self.translateForSlug(com.cat_name)
#             com.client_id = cl_id.id
#             com.save()
#         return redirect(reverse_lazy('cat_equip', kwargs={'cat_slug':self.kwargs['cat_slug']}))
