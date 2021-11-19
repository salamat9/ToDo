from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Task, Tag
from .forms import CategoryForm, TaskForm


def base(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'base.html', {'tasks': tasks,
                                         'categories': categories,
                                         'tags': tags})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    tasks = Task.objects.filter(category=category)
    return render(request, 'category/category_detail.html', {'category': category,
                                                             'tasks': tasks})


def create_category(request):
    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_category = Category.objects.create(
                name=cd['name'],
            )
            return redirect(new_category.get_absolute_url())
    else:
        form = CategoryForm()
    return render(request, 'category/category_create.html', {'form': form})


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            category.save()
            return redirect(category.get_absolute_url())
    else:
        form = CategoryForm(initial={
            'name': category.name
        })
    return render(request, 'category/category_edit.html', {'form': form})


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')


def task_list(request, category_pk=None):
    category = None
    categories = Category.objects.all()
    tasks = Task.objects.all()
    if category_pk:
        category = get_object_or_404(Category, pk=category_pk)
        tasks = Task.objects.filter(category=category)
    return render(request, 'task/task_list.html', {'tasks': tasks,
                                                   'category': category,
                                                   'categories': categories})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    tags = Tag.objects.filter(tasks=task)
    return render(request, 'task/task_detail.html', {'task': task,
                                                     'tags': tags})


def create_task(request):
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_task = Task.objects.create(
                title=cd['title'],
                description=cd['description'],
                deadline=cd['deadline'],
                category=cd['category']
            )
            tags = Tag.objects.all()
            tags_name = []
            for tag in tags:
                tags_name.append(tag.name)
            for tag in cd['tags']:
                if tag in tags_name:
                    get_tag = Tag.objects.get(name=tag)
                    new_task.tags.add(get_tag)
                else:
                    new_tag = Tag.objects.create(name=tag)
                    new_task.tags.add(new_tag)
            new_task.save()
            return redirect(new_task.get_absolute_url())
    else:
        form = TaskForm()
    return render(request, 'task/task_create.html', {'form': form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            task.save()
            return redirect(task.get_absolute_url())
    else:
        form = TaskForm(initial={
            task.title,
            task.description,
            task.deadline,
            task.category
        })
    return render(request, 'task/task_edit.html', {'form': form})


def tag_list(request):
    ...


def tag_detail(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    tasks = Task.objects.filter(tags=tag)
    return render(request, 'tag/tag_detail.html', {'tag': tag,
                                               'tasks': tasks})

def create_tag(request, pk):
    ...


def delete_tag(request, pk):
    ...


def update_tag(request, pk):
    ...
