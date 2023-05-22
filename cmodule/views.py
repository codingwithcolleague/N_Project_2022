from django.shortcuts import render
from services.c_service import CService
# Create your views here.
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
from n_project_2022.common.error_response import ErrorResponse
from n_project_2022.common.error_response import StackTraceFormatter
from n_project_2022.custom_log import get_or_create
from rest_framework import status
stack_formater  = StackTraceFormatter()
log = get_or_create("ciq")
from rest_framework import viewsets

class CMappingAPI(APIView):
    @csrf_exempt
    @api_view
    def get_map(request):
        try:
            pass
        except Exception as error:
            stack_formater.exception(error,log)
            return JsonResponse(
            ErrorResponse(code=status.HTTP_400_BAD_REQUEST,message=str(error)).toJson(),
            status=status.HTTP_400_BAD_REQUEST)
        
        
    @api_view('POST','GET')
    def map(request):
        try:
            pass
        except Exception as error:
            stack_formater.exception(error,log)
            return JsonResponse(
            ErrorResponse(code=status.HTTP_400_BAD_REQUEST,message=str(error)).toJson(),
            status=status.HTTP_400_BAD_REQUEST)
        
        
class ServiceAPI(viewsets.ViewSet):
    def parse(self, request):
        try:
            pass
        except:
            pass