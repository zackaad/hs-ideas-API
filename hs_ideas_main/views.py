from django.http import JsonResponse
from rest_framework import views


class MyView(views.APIView):
    def get(self, request):
        return JsonResponse({'msg': 'Hello world!'}, status=200)