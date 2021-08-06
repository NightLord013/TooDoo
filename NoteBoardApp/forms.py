from django import forms
from django.forms.widgets import TextInput, DateTimeInput
from .models import Category, Note
from django.contrib.admin.widgets import AdminSplitDateTime


class CustomAdminSplitDateTime(AdminSplitDateTime):
    """Кастомный административный виджет без заголовков перед формой"""
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        del context['date_label'], context['time_label']
        return context


class AddCategoryFrom(forms.ModelForm):
    color = forms.CharField(max_length=7, widget=TextInput(attrs={'type': 'color'}))

    class Meta:
        model = Category
        fields = ['name', 'color', ]


class AddNoteForm(forms.ModelForm):
    deadline = forms.SplitDateTimeField(input_date_formats=['%Y-%m-%d'], widget=CustomAdminSplitDateTime())
    class Meta:
        model = Note
        fields = ['title', 'category', 'deadline']


class UpdateNoteForm(forms.ModelForm):
    # deadline = forms.SplitDateTimeField(widget=DateTimeInput(attrs={'type': 'datetime'}))
    deadline = forms.SplitDateTimeField(input_date_formats=['%Y-%m-%d'], widget=CustomAdminSplitDateTime())
    class Meta:
        model = Note
        fields = ['title', 'category', 'deadline']

class SettingsForm(forms.Form):
    title = forms.CharField(max_length=7)