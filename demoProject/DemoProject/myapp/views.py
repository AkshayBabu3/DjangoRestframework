from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads



@method_decorator(csrf_exempt,name = "demo")
class DemoView(View):
    def post(self,request):
        requested_body=request.body
        form = loads(requested_body)
        n = form.get("num")
        fact = 1
        for i in range(n+1):
            fact *= i
        data ={
            "Factorial":fact
        }
        return JsonResponse(data)