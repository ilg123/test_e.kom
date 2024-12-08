from django.urls import path
from .views import get_form, add_template, clear_templates

urlpatterns = [
    path('get_form', get_form, name='get_form'),
    path('add_template', add_template, name='add_template'),
    path('clear_templates', clear_templates, name='clear_templates'),
]
