from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class classik(TemplateView):
    template_name ='class_template.html'
class func(TemplateView):
    template_name = 'func_template.html'

# def classik(request):
#     return render(request, 'class_template.html')
# def func(request):
#     return render(request, 'func_template.html')