from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('all/', views.AllNotesView.as_view(), name='all_notes'),
    # ajax
    path('ajax/', views.note_action_ajax, name='note_action_ajax'),

    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('add_note/', views.AddNoteView.as_view(), name='add_note'),
    path('add_note/<str:category_name>/', views.AddNoteView.as_view(), name='add_note_category'),
    path('<str:category_name>/', views.CategoryView.as_view(), name='category'), # ошибка в консоле
    path('search/<str:keyword>/', views.SearchView.as_view(), name='search'),
    path('delete_category/<int:pk>/', views.DeleteCategory.as_view(), name='delete_category'),
    path('delete_note/<int:pk>/', views.DeleteNote.as_view(), name='delete_note'),
    path('detail/<int:pk>/', views.DetailNoteView.as_view(), name='detail_note'),
]
