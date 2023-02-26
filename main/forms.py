from django import forms
from django.db.models import fields
from .models import *
teachers = Teacher.objects.all()
choices_teacher = []

for i in teachers:
    choices_teacher.append((i.name, i.name))
choices_teacher = tuple(choices_teacher)

classes = Class.objects.all()
choices_class = []

for i in classes:
    choices_class.append((i.class_name, i.class_name))
    
choices_class = tuple(choices_class)

class Formforgo(forms.Form):
    select_teacher = forms.ChoiceField(widget=forms.Select, choices=choices_teacher)
    select_class =  forms.ChoiceField(widget=forms.Select, choices=choices_class)
    class Meta:
        fields = ('select_teacher', 'select_class')