from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Whisper

class WhisperListView(ListView):
  model = Whisper
  paginate_by = 15
  ordering = ('-created_at',)

class WhisperCreateView(SuccessMessageMixin, CreateView):
  model = Whisper
  fields = '__all__'
  success_url = '/'
  success_message = "Susurro registrado."
