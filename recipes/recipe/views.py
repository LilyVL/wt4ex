from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Recipe

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'recipe/index.html'
	context_object_name = 'recipe_list'

	def get_queryset(self):
		return Recipe.objects.order_by('name')
