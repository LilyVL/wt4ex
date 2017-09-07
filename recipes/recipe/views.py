from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic

from .models import Recipe

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'recipe/index.html'
	context_object_name = 'recipe_list'

	def get_queryset(self):
		return Recipe.objects.order_by('name').order_by('calories')


def submit(request):
    if request.method == 'POST':
        rname = request.POST.get('name')
        ringredients = request.POST.get('ingredients')
        rcalories = request.POST.get('calories')
        rprep_time = request.POST.get('prep_time')
        recipe = Recipe.objects.create(name=rname, ingredients=ringredients, calories=rcalories, prep_time=rprep_time)
        try:
            recipe.save()
            return render(request, 'recipe/saved.html', None)
        except:
            return render(request, 'recipe/failed.html', None)
    else:
        return render(request, 'recipe/submit.html', None)
