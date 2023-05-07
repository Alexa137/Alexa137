from . models import Account, Destination
from rest_framework.response import Response
from rest_framework import status
from .serializers import AccountSerializer, DestinationSerializer
from rest_framework.decorators import api_view

# Account CRUD APIs
@api_view(['GET'])
def account_list(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def account_detail(request, id):
    account = Account.objects.get(id=id)
    serializer = AccountSerializer(account)
    return Response(serializer.data)

@api_view(['POST'])
def account_create(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def account_update(request, id):
    account = Account.objects.get(id=id)
    serializer = AccountSerializer(account, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def account_delete(request, id):
    account = Account.objects.get(id=id)
    account.delete()
    return Response(status=204)

# Destination CRUD APIs
@api_view(['GET'])
def destination_list(request, account_id):
    destinations = Destination.objects.filter(account_id=account_id)
    serializer = DestinationSerializer(destinations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def destination_detail(request, id):
    destination = Destination.objects.get(id=id)
    serializer = DestinationSerializer(destination)
    return Response(serializer.data)

@api_view(['POST'])
def destination_create(request, account_id):
    request.data['account'] = account_id
    serializer = DestinationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def destination_update(request, id):
    destination = Destination.objects.get(id=id)
    serializer = DestinationSerializer(destination, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def destination_delete(request, id):
    destination = Destination.objects.get(id=id)
    destination.delete()
    return Response(status=204)



@api_view(['GET'])
def get_destinations_for_account(request, id):
    try:
        account = Account.objects.get(id=id)
        destinations = Destination.objects.filter(account=account)
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
