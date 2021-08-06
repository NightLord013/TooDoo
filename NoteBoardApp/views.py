from django.shortcuts import redirect, render
from .models import Category, Note
from UserApp.models import User
from django.utils import timezone
from django.http import JsonResponse
from django.views.generic import ListView, FormView, DeleteView, UpdateView
from .forms import AddCategoryFrom, AddNoteForm, UpdateNoteForm, SettingsForm
from .calculation import get_popular_category
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy
from .config import SiteTheme


class HomeView(ListView):
    """Вывод заметок на сегоднешний день"""
    model = Note
    template_name = 'NoteBoardApp/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # получение заметок на сегоднешний день
        context['datetime'] = timezone.datetime.now().day
        context['notes'] = Note.objects.filter(user=self.request.user, deadline__day=timezone.datetime.now().day)
        return context


def note_action_ajax(request):
    """Редактирование заметки полученной Ajax"""
    if request.is_ajax():
        data = request.GET
        note = Note.objects.get(id=data['checked'])
        if note.is_done:
            note.is_done = False
        else:
            note.is_done = True
        note.save(update_fields=['is_done'])
    return JsonResponse({'success': 'success'})


class AllNotesView(ListView):
    model = Note
    template_name = 'NoteBoardApp/all_notes.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # получение заметок за все время
        context['notes'] = Note.objects.filter(user=self.request.user).order_by('-deadline__date',
                                                                                'category__name',
                                                                                'deadline__time').distinct()
        return context


class CategoryView(ListView):
    model = Note
    template_name = 'NoteBoardApp/category.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        category_name = self.kwargs.get('category_name')
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(user=self.request.user, name=category_name)
        # Вычисление позиции нужной категории в списке всех категорий
        context['position'] = [category.name for category in Category.objects.filter(user=self.request.user)].index(category_name)
        context['notes'] = Note.objects.filter(user=self.request.user, category__name=category_name).order_by('-deadline')
        return context


class SearchView(ListView):
    model = Note
    template_name = 'NoteBoardApp/search.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        keyword = self.kwargs.get('keyword')
        context = super().get_context_data(**kwargs)
        context['keyword'] = keyword
        context['notes'] = Note.objects.filter(Q(user=self.request.user) & Q(title__icontains=keyword))
        return context


class AddCategoryView(FormView):
    form_class = AddCategoryFrom
    template_name = 'NoteBoardApp/add_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_category'] = get_popular_category(Category)
        return context

    def form_valid(self, form):
        form = form.save(commit=False)
        if form.name not in [i.name for i in Category.objects.filter(user=self.request.user)]:
            form.user = User.objects.get(email=self.request.user)
            form.save()
            return redirect('add_category')
        else:
            messages.error(self.request, 'Такая категория уже существует!')
            return redirect('add_category')

class DeleteCategory(DeleteView):
    model = Category
    template_name = 'NoteBoardApp/delete_category.html'
    success_url = reverse_lazy('home')

class AddNoteView(FormView):
    form_class = AddNoteForm
    template_name = 'NoteBoardApp/add_note.html'

    def get_initial(self):
        initial = super().get_initial()
        if self.kwargs.get('category_name') != None: # проверка 'необязательного' url параметра
            category_name = self.kwargs.get('category_name')
            initial['category'] = Category.objects.get(user=self.request.user, name=category_name)
            return initial

    def form_valid(self, form):
        note_id = self.kwargs.get('pk')
        form = form.save(commit=False)
        form.user = User.objects.get(email=self.request.user)
        form.save()
        return redirect('category', form.category)

class DeleteNote(DeleteView):
    model = Note
    template_name = 'NoteBoardApp/delete_note.html'
    success_url = reverse_lazy('home')

class DetailNoteView(UpdateView):
    model = Note
    template_name = 'NoteBoardApp/detail_note.html'
    form_class = UpdateNoteForm

    def form_valid(self, form):
        note_id = self.kwargs.get('pk')
        form = form.save(commit=False)
        category = form.category
        form.save()
        return redirect('category', category)

class SettingsView(FormView):
    template_name = 'NoteBoardApp/settings.html'
    form_class = SettingsForm

    def post(self, request, *args, **kwargs):
        # print(request.session.get('site_color'))
        SiteTheme.set_color(request)
        return redirect('settings')






