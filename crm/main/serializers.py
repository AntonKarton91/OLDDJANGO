from rest_framework import serializers

from main.models import *

#
# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = '__all__'
#
#
# class CatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EquipmentCat
#         fields = '__all__'
#
#
# class ColumnSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Columns
#         fields = '__all__'
#
# class TasksSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tasks
#         fields = '__all__'
#
# class ParticipantsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('first_name', 'id', 'sur_name', 'img',)