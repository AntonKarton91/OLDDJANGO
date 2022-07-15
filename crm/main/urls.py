from django.urls import path, include
from rest_framework import routers
from .views import *

# ____________________________________________________________________________________________
# Создаем класс роутера
taskRouter = routers.DefaultRouter()

# Регистрируем Вьюсет в роутере (r'tasks' - это префикс в маршруте)
taskRouter.register(r'tasks', TaskViewSet)
print(taskRouter.urls)
# /////////////////////////////////////////////////////////////////////////////////////////////



urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('api/v1/clientlist/', ClientListView.as_view()),
    path('api/v1/catlist', CatListView.as_view()),
    path('api/v1/columnlist/', ColumnTaskAPIView.as_view()),

    # ____________________________________________________________________________________________
    # Вьюсет для отображения модели ЗАДАЧИ, в словаре дополнительно указываются разрешенные методы
    # и методы-обработчики, вызываемые к ним
    # path('api/v1/tasklist/', TaskViewSet.as_view({'get':'list'})),
    # path('api/v1/tasklist/<int:pk>/', TaskViewSet.as_view({'put':'update'})),
    # /////////////////////////////////////////////////////////////////////////////////////////////

    # ____________________________________________________________________________________________
    # Вьюсет c использованием роутера.
    path('api/v1/', include(taskRouter.urls)), # http://127.0.0.1:8000/api/v1/tasks/
    # /////////////////////////////////////////////////////////////////////////////////////////////


    # path('register/', RegisterUser.as_view(), name='register'),
    # path('login/', LoginUser.as_view(), name='login'),
    # path('profile/', UserProfile.as_view(), name='profile'),
    # path('supplies/', login, name='supplies'),
    # path('logout/', logout_user, name='logout'),
    # path('dko/', TasksDKO.as_view(), name='dko'),
    # path('trades/', login, name='trades'),
    # path('equipment/', ClientEquipmentList.as_view(), name='clientequip'),
    # path('equipment_cat/<slug:cat_slug>/', CatEquipmentList.as_view(), name='cat_equip'),
]