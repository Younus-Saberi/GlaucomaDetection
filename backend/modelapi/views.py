from rest_framework.views import APIView
from django.http import JsonResponse

# import json
# import numpy as np
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from PIL import Image
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

class HelloWorldView(APIView):
    def get(self, request, format=None):
        return JsonResponse({'message': 'Hello, world!'})


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UploadedImage, UploadedResult
from .serializers import UploadedImageSerializer, UploadedResultSerializer
from rest_framework.views import APIView

class UploadImageView(APIView):
    def post(self,request, *args, **kwargs):
        serializer = UploadedImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UploadedResultAPIView(APIView):
    def get(self,request, image_id):
        try:
            uploaded_image = UploadedImage.objects.get(id = image_id)
            uploaded_result = UploadedResult.objects.get(uploaded_image=uploaded_image)
            serializer = UploadedResultSerializer(uploaded_result)
            return JsonResponse(serializer.data, status = status.HTTP_200_OK)
        except UploadedImage.DoesNotExist:
            return JsonResponse({"error":"Uploaded Image does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except UploadedResult.DoesNotExist:
            return JsonResponse({"error": "Result Not Found for the uploaded image"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({"error occurred: ==>", e})