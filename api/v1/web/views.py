

from api.v1.web.serializers import  AddAboutSerializer, AddEnquiriesSerializer, AddGallerySerializer, AddServiceSerializer, GalleryViewSerializer, ViewAboutSerializer, ViewServiceSerializer
from general.functions import generate_serializer_errors
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from web.models import About, Enquiry, Gallery, Services

@api_view(['GET'])
@permission_classes([AllowAny])
def abouts(request):
    if (abouts := About.objects.filter(is_deleted=False)).exists():
        serialized_data = ViewAboutSerializer(
            abouts,
            context = {
                "request" : request,
            },
            many=True
        ).data

        response_data = {
            "StatusCode" : 6000,
            "data" : {
                "title" : "Success",
                "data" : serialized_data
            }
        }
    else:
        response_data = {
            "StatusCode" : 6001,
            "data" : {
                "title" : "Failed",
                "data" : "About not found"
            }
        }
    
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def add_abouts(request):
    serializer = AddAboutSerializer(data = request.data)

    if serializer.is_valid():
        name = request.data['name']
        description = request.data['description']
        photo = request.data['photo']

        abouts = About.objects.create(
            name = name,
            description = description,
            photo = photo
        )

        response_data = {
            "StatusCode" : 6000,
            "data" : {
                "title" : "Success",
                "message" : "About created successfully"
            }
        }
    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Validation Error",
                "message": generate_serializer_errors(serializer._errors)
            }
        }
    
    return Response(response_data, status=status.HTTP_200_OK)

        
@api_view(['POST'])
@permission_classes([AllowAny])
def edit_abouts(request, pk):
    name = request.data.get('name')
    description = request.data.get('description')
    photo = request.data.get('photo')

    if (abouts := About.objects.filter(pk=pk, is_deleted=False)).exists():
        abouts = abouts.latest('id')

        if name:
            abouts.name = name
        if description:
            abouts.description = description
        if photo:
            abouts.photo = photo
        abouts.save()

        response_data = {
            "StatusCode": 6000,
            "data": {
                "title": "Success",
                "message": "Edit successfully completed"
            }
        }

    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Failed",
                "message": "Enquiry not found"
            }
        }

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def delete_abouts(request, pk):
    if (abouts := About.objects.filter(pk=pk, is_deleted=False)).exists():
        abouts = abouts.latest('id')

        abouts.is_deleted = True
        abouts.save()

        response_data = {
            "StatusCode": 6000,
            "data": {
                "title": "Success",
                "message": "delete successfully completed"
            }
        }


    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Failed",
                "message": "Enquiry not found"
            }
        }

    return Response(response_data, status=status.HTTP_200_OK)
    
    
@api_view(['GET'])
@permission_classes([AllowAny])
def services(request):
    if (services := Services.objects.filter(is_deleted=False)).exists():
        serialized_data = ViewServiceSerializer(
            services,
            context = {
                "request" : request,
            },
            many=True
        ).data

        response_data = {
            "StatusCode" : 6000,
            "data" : {
                "title" : "Success",
                "data" : serialized_data
            }
        }
    else:
        response_data = {
            "StatusCode" : 6001,
            "data" : {
                "title" : "Failed",
                "data" : "Services  not found"
            }
        }
    
    return Response(response_data, status=status.HTTP_200_OK)

    
@api_view(['POST'])
@permission_classes([AllowAny])
def add_services(request):
    serializer = AddServiceSerializer(data = request.data)

    if serializer.is_valid():
        name = request.data['name']
        description = request.data['description']
        photo = request.data['photo']

        services = Services.objects.create(
            name = name,
            description = description,
            photo = photo
        )

        response_data = {
            "StatusCode" : 6000,
            "data" : {
                "title" : "Success",
                "message" : "Service created successfully"
            }
        }
    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Validation Error",
                "message": generate_serializer_errors(serializer._errors)
            }
        }
    
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def delete_services(request, pk):
    if (services := Services.objects.filter(pk=pk, is_deleted=False)).exists():
        service = services.latest('id')

        service.is_deleted = True
        service.save()

        response_data = {
            "StatusCode": 6000,
            "data": {
                "title": "Success",
                "message": "delete successfully completed"
            }
        }
    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Failed",
                "message": "Service not found"
            }
        }

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def edit_services(request, pk):
    name = request.data.get('name')
    description = request.data.get('description')
    photo = request.data.get('phtot')

    if (services := Services.objects.filter(pk=pk, is_deleted=False)).exists():
        service = services.latest('id')

        if name:
            service.name = name
        if description:
            service.description = description
        if photo:
            service.photo = photo
        service.save()

        response_data = {
            "StatusCode": 6000,
            "data": {
                "title": "Success",
                "message": "Edit successfully completed"
            }
        }

    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Failed",
                "message": "Service not found"
            }
        }

    return Response(response_data, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([AllowAny])
def galleries(request):
    if (galleries := Gallery.objects.filter(is_deleted=False)).exists():
        serialized_data = GalleryViewSerializer(
            galleries,
            context = {
                "request" : request,
            },
            many=True,
        ).data

        response_data = {
            "StatusCode" : 6000,
            "data" : {
                "title" : "Success",
                "data" : serialized_data
            }
        }
    else:
        response_data = {
            "StatusCode" : 6001,
            "data" : {
                "title" : "Failed",
                "data" : "Gallery not found"
            }
        }
    
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def add_enquiries(request):
    serializer = AddEnquiriesSerializer(data = request.data)
    if serializer.is_valid():
        name = request.data['name']
        phone = request.data['phone']
        email = request.data.get('email')

        enquiry = Enquiry.objects.create(
            name = name,
            phone = phone,
            email = email
        )

        response_data = {
            "StatusCode" : 6000,
            "data" : {
                "title" : "Success",
                "message" : "Enquiry created successfully"
            }
        }
    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Validation Error",
                "message": generate_serializer_errors(serializer._errors)
            }
        }

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def add_galleries(request):
    serializer = AddGallerySerializer(data = request.data)

    if serializer.is_valid():
        photo = request.data['photo']

        abouts = Gallery.objects.create(
            photo = photo
        )

        response_data = {
            "StatusCode" : 6000,
            "data" : {
                "title" : "Success",
                "message" : "Gallery created successfully"
            }
        }
    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Validation Error",
                "message": generate_serializer_errors(serializer._errors)
            }
        }
    
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def edit_galleries(request, pk):
    photo = request.data.get('photo')

    if (galleries := Gallery.objects.filter(pk=pk, is_deleted=False)).exists():
        gallery = galleries.latest('id')

        if photo:
            gallery.photo = photo
        gallery.save()

        response_data = {
            "StatusCode": 6000,
            "data": {
                "title": "Success",
                "message": "Edit successfully completed"
            }
        }

    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Failed",
                "message": "Enquiry not found"
            }
        }

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def delete_galleries(request, pk):
    if (galleries := Gallery.objects.filter(pk=pk, is_deleted=False)).exists():
        gallery = galleries.latest('id')

        gallery.is_deleted = True
        gallery.save()

        response_data = {
            "StatusCode": 6000,
            "data": {
                "title": "Success",
                "message": "delete successfully completed"
            }
        }


    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Failed",
                "message": "Enquiry not found"
            }
        }

    return Response(response_data, status=status.HTTP_200_OK)
    
