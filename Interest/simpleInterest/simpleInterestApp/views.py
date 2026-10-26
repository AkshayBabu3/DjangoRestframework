from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads
# Create your views here.


@method_decorator(csrf_exempt,name = "dispatch")
class SimpleInterest(View):
    def post(self,request):
        request = request.body
        data = loads(request)
        principal = data.get("principal")
        rate = data.get("rate")
        time = data.get("time")
        interest = (principal*rate*time)/100
        data = {
            "Simple Interest":interest
        }
        return JsonResponse(data)
    
@method_decorator(csrf_exempt,name="dispatch")
class DiscountView(View):
    def post(self,request):
        request = request.body
        data = loads(request)
        price = data.get("price")
        discount = data.get("discount")
        discount_percent = price * discount/100
        res = price - discount_percent
        data = {
            "Price":price,
            "Discount Percentage":discount,
            "Discount Amount":discount_percent,
            "Final Price":res
        }
        return JsonResponse(data)
    

@method_decorator(csrf_exempt,name ="dispatch")
class profitView(View):
    def post(self,request):
        request = request.body
        data = loads(request)
        cost_price = data.get("cost_price")
        selling_price = data.get("selling_price")
        res = selling_price - cost_price
        data = {
            "Cost Price":cost_price,
            "Selling_Price":selling_price,
            "profit":res
        }
        return JsonResponse(data)
    
@method_decorator(csrf_exempt,name="dispatch")
class salaryView(View):
    def post(self,request):
        request = request.body
        data = loads(request)
        basic_salary = data.get("basic_salary")
        bonus = data.get("bonus")
        deduction = data.get("deduction")
        res = (basic_salary+bonus)-deduction
        data = {
            "Net_Salary":res
        }
        return JsonResponse(data)