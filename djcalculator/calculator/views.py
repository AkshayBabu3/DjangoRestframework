from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads


@method_decorator(csrf_exempt, name='dispatch')
class CalculatorView(View):

    def post(self, request):
        request_body = request.body
        form_data = loads(request_body)
        n1 =form_data.get("num1")
        n2 =form_data.get("num2")
        result = n1+n2
        data = {
            "Addition:",result
        }

        return JsonResponse(data)
    
@method_decorator(csrf_exempt, name='dispatch')
class SubstractionView(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        res = n1 - n2
        data = {
            "Difference":res
        }
        return JsonResponse(data)
    
@method_decorator(csrf_exempt, name='dispatch')
class MultiplicationView(View):
    def post(self,request):
        request_body=request.body
        form_data = loads(request_body)
        n1 = form_data.get("num1")
        n2 = form_data.get("num2")
        result = n1 * n2
        data = {
            "Multiplication":result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class DivisionView(View):
    def post(self,request):
        request_body = request.body
        form = loads(request_body)
        n1 = form.get("num1")
        n2 = form.get("num2")
        res = n1 / n2
        data = {
            "Division":res
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name="dispatch")
class ModulusView(View):
    def post(self,request):
        request_body = request.body
        form = loads(request_body)
        n2 = form.get("num2")
        n1 = form.get("num1")
        res = n1 % n2
        data = {
            "Operation":"Modulus",
            "result" : res
        }
        return JsonResponse(data)
    
@method_decorator(csrf_exempt,name = "dispatch")
class BmiView(View):
    def post(self,request):
        request_body = request.body
        form = loads(request_body)
        weight = form.get("weight")            
        height = form.get("height")/100

        res = weight/height**2

        data = {
                "height":height,
                "weight":weight,
                "BMI":res
              
         }
        return JsonResponse(data)


@method_decorator(csrf_exempt,name = "dispatch")
class AgeView(View):
    def post(self,request):
        req = request.body
        form = loads(req)
        y1 = form.get("current")
        y2 = form.get("birth")
        res = y1 - y2
        data = {
            "Age":res
        }
        return JsonResponse(data)