from django.shortcuts import render
from django.views.generic import ListView, View, CreateView, UpdateView, DeleteView
from .models import Todo
from django.urls import reverse_lazy



# Create your views here.
def dashboard_view(request):
    todo_count = Todo.objects.all().count()
    context = {
        'todo_count': todo_count
    }
    return render(request, 'todo/dashboard.html', context)


class TodoCreateView(CreateView):
    model = Todo
    template_name = "todo/todo.html"
    fields = '__all__'
    success_url = reverse_lazy("todo:todo-create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] = Todo.objects.all()
        return context

class TodoUpdateView(UpdateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('todo:todo-create')

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:todo-create')
