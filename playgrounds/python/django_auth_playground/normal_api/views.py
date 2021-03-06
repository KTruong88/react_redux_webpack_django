from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework import status, generics, permissions, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# import normal_api
from normal_api.models import Unit
from normal_api.authentications import CsrfExemptAuthentication
from normal_api.custom_permissions import IsOwnerOrReadOnly, HasUserAndAuthOnRequest
from normal_api.serializers import UnitSerializer, UserSerializer


# @NOTE: Using CBVs with generic API Views
# Using generic views has built in BrowsableRenderer implemented
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'units': reverse('unit-list', request=request, format=format),
    })


class UnitList(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    authentication_classes = (JSONWebTokenAuthentication, CsrfExemptAuthentication, )
    permission_classes = (IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (CsrfExemptAuthentication, JSONWebTokenAuthentication)
    permission_classes = (HasUserAndAuthOnRequest, )


class UnitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    authentication_classes = (CsrfExemptAuthentication, JSONWebTokenAuthentication, )
    permission_classes = (HasUserAndAuthOnRequest, )


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (CsrfExemptAuthentication, JSONWebTokenAuthentication)
    permission_classes = (HasUserAndAuthOnRequest, )


# @NOTE: Using Class-based views with normal API View
# class UnitList(APIView):
#     def get(self, request, format=None):
#         units = Unit.objects.all()
#         serializer = UnitSerializer(units, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = UnitSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
#
#
# class UnitDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Unit.objects.get(pk=pk)
#         except Unit.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         unit = self.get_object(pk)
#         serializer = UnitSerializer(unit)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         unit = self.get_object(pk)
#         serializer = UnitSerializer(unit, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         unit = self.get_object(pk)
#         unit.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @NOTE: (1) Basic 'GET' APIs with function-based views and @api_view... as simple as you can get with DRF

#
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser


# @api_view(['GET', 'POST'])
# def unit_list(request, format=None):
#     if request.method == 'GET':
#         units = Unit.objects.all()
#         serializer = UnitSerializer(units, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = UnitSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def unit_detail(request, pk, format=None):
#     try:
#         unit = Unit.objects.get(pk=pk)
#     except Unit.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = UnitSerializer(unit)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = UnitSerializer(unit, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         unit.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @NOTE: ViewSets
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     # This viewset provides 'list' and 'detail' actions
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UnitViewSet(viewsets.ModelViewSet):
#     # This viewset provides 'list', 'create', 'retrieve', 'update', 'destroy' actions
#     queryset = Unit.objects.all()
#     serializer_class = UnitSerializer
#     permission_clases = (permissions.IsAuthenticatedOrReadOnly,
#                          IsOwnerOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#     detail_route is used to create custom actions, adding
#     any custom endpoints that don't fit into standard CRUD style
#     @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
#     def highlight(Self, request, *args, **kwargs):
#         snippet = self.get_object()
#         REturn Response(snippet.highlighted)
