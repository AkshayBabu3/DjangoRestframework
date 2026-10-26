from django.views.generic import View
from django.http import JsonResponse


class AboutView(View):
    def get(self, request):
        data = {
            "ID": "2",
            "Name": "Akshay",
            "Place": "Kochi",
            "contact": "7645363746",
            "Email": "Akshay@gmail.com",
            "Github": "github/akshayb53",
            "Linkdin": "Linkdin/akshay4444"
        }

        return JsonResponse(data)


class EducationView(View):
    def get(self, request):
        data = {
            "ID": "1",
            "Institution": "GEC Thrissur",
            "Degree": "MCA",
            "University": "APJ",
            "Location": "Thrissur",
            "Start year": "2024",
            "End year": "2026",
            "Grade or CGPA": "9.0",
            "Description": "COMPLETED"
        }

        return JsonResponse(data)
    
class ProjectView(View):
    def get(self,request):
        data = [
            {
            "ID":"101",
            "Title":"Agro",
            "Long decription":"its a agro based project",
            "Technologies":"python Django",
            "Live URL":"https://agro.com",
            "Github URL":"https://Github/akshayb54/agro",
            "Image URL":"https://image.html",
            "Featured":""
        },
        {
            "ID":"102",
            "Title":"Plantleaf",
            "Long decription":"plant leaf disease project",
            "Technologies":"java",
            "Live URL":"http://127.0.0.1:8000/plant/",
            "Github URL":"https://Github/akshayb54/plant",
            "Image URL":"https://image.html",
            "Featured":""
        },
        {"ID":"104",
            "Title":"Doc",
            "Long decription":"",
            "Technologies":"java",
            "Live URL":"http://127.0.0.1:8000/doc/",
            "Github URL":"https://Github/akshayb54/doc",
            "Image URL":"https://image.html",
            "Featured":""}
        ]
        return JsonResponse(data,safe=False)

class SkillView(View):
    def get(self,request):
        data = [
            {
             "ID":"201",
             "Skill name":"Python",
             "Category":"Programming Language",
             "proficiency":"Advanced",
             "Years od experience":"4"
            },
            {
             "ID":"202",
             "Skill name":"React",
             "Category":"Frontend",
             "proficiency":"Advanced",
             "Years od experience":"3"
            },
            {
             "ID":"203",
             "Skill name":"Java",
             "Category":"Programming Language",
             "proficiency":"Advanced",
             "Years od experience":"6"
            }
            ]
        return JsonResponse(data,safe=False)
    
class ExperienceView(View):
    def get(self,request):
        data = [
            {
             "ID":"301",
             "Job title":"HR",
             "Company name":"TCS",
             "Location":"Kochi",
             "Employment type":"Full-time",
             "Start date":"12-02-2012",
             "End date":"12-02-2026",
             "Currently working":"Infosys",
             "Description":""
            },
            {
             "ID":"302",
             "Job title":"Devloper",
             "Company name":"pranav",
             "Location":"Kochi",
             "Employment type":"Full-time",
             "Start date":"12-09-2026",
             "End date":"12-09-2030",
             "Currently working":"Tcs",
             "Description":"niggaa"
            },
            {
             "ID":"303",
             "Job title":"Full stack dev",
             "Company name":"Devanath",
             "Location":"poothotta",
             "Employment type":"Work from home",
             "Start date":"23-10-2026",
             "End date":"23-10-2030",
             "Currently working":"Nil",
             "Description":""
            }
        ]
        return JsonResponse(data,safe=False)
    
class certificateView(View):
    def get(self,Request):
            data =[
                {"ID":"401",
                 "Certificate name":"Python",
                 "Issuing Organization":"Luminar",
                 "Issued date":"12-12-2026"
                },
                {"ID":"401",
                 "Certificate name":"Java",
                 "Issuing Organization":"Quest",
                 "Issued date":"11-10-2026"
                },
                {"ID":"401",
                 "Certificate name":"React",
                 "Issuing Organization":"Luminar",
                 "Issued date":"12-08-2026"
                
                }
            ]
            return JsonResponse(data,safe=False)
    
class ServiceView(View):
    def get(self,Request):
        data = [
            {
            "ID":"501",
            "Service name":"Web Development",
            "description":"Devlopment of Advanced Web pages",
            "Technologies":"python,Django"
            },
            {
            "ID":"501",
            "Service name":"Web Development",
            "description":"Devlopment of Advanced Web pages",
            "Technologies":"python,Django"
            }, 
            {
            "ID":"501",
            "Service name":"Web Development",
            "description":"Devlopment of Advanced Web pages",
            "Technologies":"python,Django"
            }
        ]
        return JsonResponse(data,safe=False)
    
"""class ContactView(View):
    def post(self,)
"""