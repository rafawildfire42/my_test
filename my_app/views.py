import json
from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from .models import Client, Company


class ClientView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        data = json.loads(request.body)
        try:
            client = Client.objects.create(**data)
            client_json = model_to_dict(client)
            return JsonResponse(client_json, status=201)
        except Exception as error:
            return JsonResponse({"error": "falha ao criar", "detail": str(error)}, status=406)
    
    def get(self, request: HttpRequest, pk=None) -> HttpResponse:
        if pk:
            try:
                client = Client.objects.get(pk=pk)
                return JsonResponse(model_to_dict(client))
            except Client.DoesNotExist as error:
                return JsonResponse({"error": "não encontrado", "detail": str(error)}, status=404)
        else:
            clients = Client.objects.all()
            data = []
            for client in clients:
                data.append({**model_to_dict(client)})
        
            return JsonResponse(data, safe=False)

    def put(self, request: HttpRequest, pk=None) -> HttpResponse:
        data = json.loads(request.body)
        try:
            client = Client.objects.get(pk=pk)
            for key, value in data.items():
                setattr(client, key, value)
            client.save()
            return JsonResponse(model_to_dict(client))
        except Client.DoesNotExist as error:
            return JsonResponse({"error": "não encontrado", "detail": str(error)}, status=404)
        except Exception as error:
            return JsonResponse({"error": "falha", "detail": str(error)}, status=406)

class CompanyView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        data = json.loads(request.body)
        try:
            company = Company.objects.create(**data)
            company_json = model_to_dict(company)
            return JsonResponse(company_json, status=201)
        except Exception as error:
            return JsonResponse({"error": "falha ao criar", "detail": str(error)}, status=406)
    
    def get(self, request: HttpRequest, pk=None) -> HttpResponse:
        if pk:
            try:
                company = Company.objects.get(pk=pk)
                return JsonResponse(model_to_dict(company))
            except Company.DoesNotExist as error:
                return JsonResponse({"error": "não encontrado", "detail": str(error)}, status=404)
        else:
            companies = Company.objects.all()
            data = []
            for company in companies:
                data.append({**model_to_dict(company)})
        
            return JsonResponse(data, safe=False)

    def put(self, request: HttpRequest, pk=None) -> HttpResponse:
        data = json.loads(request.body)
        try:
            company = Company.objects.get(pk=pk)
            for key, value in data.items():
                setattr(company, key, value)
            company.save()
            return JsonResponse(model_to_dict(company))
        except Client.DoesNotExist as error:
            return JsonResponse({"error": "não encontrado", "detail": str(error)}, status=404)
        except Exception as error:
            return JsonResponse({"error": "falha", "detail": str(error)}, status=406)
