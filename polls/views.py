from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import ExerciseModel
from .forms import ExerciseForm
from django.shortcuts import (get_object_or_404,HttpResponseRedirect)
from django.views import View
from django.views.generic import DeleteView, FormView,ListView

def create_view(request):

    context ={}
 
    form = ExerciseForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    if request.method =="POST":
        return HttpResponseRedirect("/polls/list/")
    context['form']= form
    return render(request, "create_view.html", context)

def list_view(request):
    context ={}

    context["dataset"] = ExerciseModel.objects.all()
         
    return render(request, "list_view.html", context)

def detail_view(request, id):

    context ={}
  
    context["data"] = ExerciseModel.objects.get(id = id)
          
    return render(request, "detail_view.html", context)

def update_view(request, id):
    context ={}
 
    obj = get_object_or_404(ExerciseModel, id = id)
 
    form = ExerciseForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/polls/"+id)

    context["form"] = form
 
    return render(request, "create_view.html", context)

def delete_view(request, id):

    context ={}
    obj = get_object_or_404(ExerciseModel, id = id) 
 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/polls/list/")
 
    return render(request, "delete_view.html", context)


class TaskDeleteView2(DeleteView):
    
    model = ExerciseModel
    template_name = "delete_view.html"
    success_url = "/polls/list/"
    def render_to_response(self, context, **response_kwargs):
        if(self.request.is_ajax()):
            id = self.request.POST.get('data')
            obj = ExerciseModel.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"message":"success"})
        else:
            response_kwargs.setdefault('content_type', self.content_type)
            return self.response_class(
                request=self.request,
                template=self.get_template_names(),
                context=context,
                using=self.template_engine,
                **response_kwargs
            )

class TaskListView(ListView):

    model = ExerciseModel
    template_name = "list_view.html"