from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator


username_validator = UnicodeUsernameValidator()

class Whisper(models.Model):
  username = models.CharField(max_length=32, validators=[username_validator], verbose_name='nombre de usuario')
  content = models.TextField(verbose_name='contenido')
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')

  class Meta:
    verbose_name = 'susurro'
    verbose_name_plural = 'susurros'

  def __str__(self):
      return f'"{self.content}" by {self.username}'
