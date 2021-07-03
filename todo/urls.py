from django.urls import path
from .views import dashboard_view, TodoCreateView, TodoUpdateView, TodoDeleteView
app_name = 'todo'

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('todo/', TodoCreateView.as_view(), name='todo-create'),
    path('todo/<int:pk>', TodoUpdateView.as_view(), name='todo-update'),
    path('todo/delete/<int:pk>', TodoDeleteView.as_view(), name='todo-delete'),
]
