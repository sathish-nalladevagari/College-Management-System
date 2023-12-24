from django.forms import ModelForm
from .models import *
from django import forms
class n(ModelForm):
    class Meta:
        model=co
        fields="__all__"
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
class e(ModelForm):
    class Meta:
        model=Form
        fields=["subject","teacher","file"]
class rw(ModelForm):
    class Meta:
        model=regis
        fields="__all__"
class k(ModelForm):
    class Meta:
        model=keys
        fields=["subject","regulation","branch","year","key"]
class quest(ModelForm):
    class Meta:
        model=questions
        fields=['question','question1','question2','question3','question4',"answer"]
class do(ModelForm):
    class Meta:
        model=doubt
        fields=["teacher_id","subject","doubt"]
class d(ModelForm):
    class Meta:
        model=assignments
        fields="__all__"