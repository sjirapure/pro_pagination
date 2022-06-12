from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.views import View
from django.core.paginator import Paginator,EmptyPage



# Create your views here.


class AddStudent(View):
    template_name = 'app1/addstu.html'
    form  = StudentForm
    
    def get(self,request):
        form = self.form()
        context={'form':form}
        return render(request,self.template_name,context)
    def post(self,request):
        form = self.form(request.POST)
        if form.is_valid():
            form .save()
            return redirect('show_url')
        context={'form':form}
        return render(request,self.template_name,context)
'''   
class ShowStudent(View):
    template_name = 'app1/showstu.html'
    def get(self,request):
        obj = Student.objects.all()
        paginator = Paginator(obj,5)
        try:
            if request.GET.get('page'):
                user = paginator.page(request.GET.get('page'))
            else:
                user = paginator.page(1)
        except EmptyPage:
            user = paginator.page(paginator.num_pages)
        
        context={'obj':user}
        return render(request,self.template_name,context)
''' 

def ShowStudent(request):
    obj = Student.objects.all()
    template_name = 'app1/showstu.html'
    paginator = Paginator(obj,5)
    try:
        if request.GET.get('page'):
            user = paginator.page(request.GET.get('page'))
        else:
            user = paginator.page(1)
    except EmptyPage:
        user = paginator.page(paginator.num_pages)
        
    context={'obj':user}
    return render(request,template_name,context)
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
class UpdateStudent(View):
    template_name = 'app1/addstu.html'
    form  = StudentForm
    def get(self,request,id):
        obj = Student.objects.get(id=id)
        form = self.form(instance=obj)
        context={'form':form}
        return render(request,self.template_name,context)
    def post(self,request,id):
        obj = Student.objects.get(id=id)
        form = self.form(request.POST,instance=obj)
        if form.is_valid():
            form .save()
            return redirect('show_url')
        context={'form':form}
        return render(request,self.template_name,context)
    
class DeleteStudent(View):
    template_name = 'app1/delete.html'
    def get(self,request,id):
        obj = Student.objects.get(id=id)
        context = {'obj':obj}
        return render(request,self.template_name,context)
    
    def post(self,request,id):
         obj = Student.objects.get(id=id)
         obj.delete()
         return redirect('show_url')
         context = {'obj':obj}
         return render(request,self.template_name,context)
       
