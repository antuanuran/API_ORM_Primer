from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Phone
from .serializers import PhoneSerializer


@api_view(http_method_names=["post"])
@permission_classes([IsAuthenticated])
def import_data(request):
    name_format = request.query_params.get("file_name", "default")
    list(name_format)
    owner_id = request.user.id

    return Response(data=f"Данные успешно получены. User={owner_id} | file_name={name_format}", status=status.HTTP_201_CREATED)


@api_view(http_method_names=["get", "post"])
@permission_classes([IsAuthenticated])
def show_catalog(request):
    value_sort = request.query_params.get('sort')
    print(value_sort)

    key_value_sort = {
        'model': 'name',
        'min': 'price',
        'max': '-price'
    }

    param = key_value_sort.get(value_sort, 'name')
    all_str = Phone.objects.order_by(param).all()

    return Response(data=f"Сортировка по параметру:{param} успешно выполнена!  Список:{all_str}", status=status.HTTP_201_CREATED)


@api_view(http_method_names=["get"])
@permission_classes([IsAuthenticated])
def show_product(request, item):
    id = request.user.id
    temp = Phone.objects.filter(name=item)
    if temp:
        result = Phone.objects.get(name=item)
    else:
        result = f'Таких моделей нет'

    return Response(data=f"{result} | id = {id}", status=status.HTTP_201_CREATED)


@api_view(http_method_names=["post"])
@permission_classes([IsAuthenticated])
def postman(request):
    phone, _ = Phone.objects.get_or_create(name=request.user.id, price=9999)

    return Response(data=f"Запись успешно загружена в Базу:  name = {phone.name} | id = {request.user.id} | price = {phone.price}", status=status.HTTP_201_CREATED)


class PhoneViewSet(ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
