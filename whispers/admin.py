from django.contrib import admin
from .models import Whisper

@admin.register(Whisper)
class WhisperAdmin(admin.ModelAdmin):
  list_display = ('username', 'content')
