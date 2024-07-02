from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Project, Image
from .forms import ProjectForm, ImageFormSet, ThreeDModelForm


# Create your views here.

def show_model(request, pid):
    project = Project.objects.get(pk=pid)
    context = {'project': project}
    return render(request, 'ModelScene.html', context=context)


@login_required
def project_list(request):
    projects = request.user.projects.all()
    context = {'projects': projects}
    return render(request, 'project_list.html', context=context)


def model_add(request, pid):
    if request.method == 'POST':
        threed_model_form = ThreeDModelForm(request.POST, request.FILES)

        if threed_model_form.is_valid():
            project = Project.objects.get(pk=pid)
            threed_model = threed_model_form.save(commit=False)
            threed_model.project = project
            threed_model.save()
            return redirect('project_list')

    else:
        threed_model_form = ThreeDModelForm()
        context = {'threed_model_form': threed_model_form}

    return render(request, 'model_add.html', context=context)


@login_required
def add_project_and_images(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())

        if project_form.is_valid() and image_formset.is_valid():
            project = project_form.save(commit=False)
            project.user = request.user
            project.save()

            for form in image_formset.cleaned_data:
                if form:
                    image = form['image']
                    description = form.get('description', '')
                    Image.objects.create(project=project, image=image, description=description)

            return redirect('project_detail', project.pk)

    else:
        project_form = ProjectForm()
        image_formset = ImageFormSet(queryset=Image.objects.none())

    return render(request, 'add_project_and_images.html', {
        'project_form': project_form,
        'image_formset': image_formset,
    })


@login_required
def add_project_images(request, pid):
    if request.method == 'POST':
        image_formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        if image_formset.is_valid():
            project = Project.objects.get(pk=pid)
            if not project.user == request.user:
                return redirect('project_list')
            for form in image_formset.cleaned_data:
                if form:
                    image = form['image']
                    description = form.get('description', '')
                    Image.objects.create(project=project, image=image, description=description)
            return redirect('project_detail', project.pk)
    else:
        image_formset = ImageFormSet(queryset=Image.objects.none())
    context = {'image_formset': image_formset}
    return render(request, 'add_project_images.html', context=context)


@login_required
def image_delete(request, iid):
    image = Image.objects.get(pk=iid)
    project = image.project
    if request.user == project.user:
        image.delete()
        return redirect('project_detail', project.pk)
    else:
        return redirect('project_list')


@login_required
def project_detail(request, pid):
    project = Project.objects.get(pk=pid)
    context = {'project': project}
    if project.user.is_staff:
        return render(request, 'case_project_detail.html', context=context)
    else:
        return render(request, 'project_detail.html', context=context)


@login_required
def project_delete(request, pid):
    project = Project.objects.get(pk=pid)
    control = project.user
    if request.user == control:
        project.delete()
        return redirect('project_list')
    else:
        return redirect('project_list')


def case_list(request):
    staff_name = 'wind'
    staff = User.objects.get(username=staff_name)
    projects = staff.projects.all()
    context = {'projects': projects}
    return render(request, 'case_project_list.html', context=context)
