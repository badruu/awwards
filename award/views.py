from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import generic
from django.db.models import F
from users.models import Profile
from . models import Project
from django.contrib.auth.models import User


def welcome(request):
    return render(request, 'award/welcome.html')

class ProjectListView(ListView):
    model = Project
    # template_name = 'award/home.html' 
    # context_object_name = 'images'
    ordering = ['-timestamp']

class UserProjectListView(ListView):
    model = Project
    context_object_name = 'object'
    template_name = 'award/user_projects.html'
    ordering = ['-timestamp']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Project.objects.filter(poster=user).order_by('-timestamp')

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(CreateView):
    model = Project
    fields = ['img','title','description','link']

    def form_valid(self, form):
        # we override the create validation to tell it this is the author of the post. Otherwise we'll get an integrity error
        form.instance.poster = self.request.user
        return super().form_valid(form)

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'award/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'award/search.html',{"message":message})

def about(request):
    return render(request, 'award/about.html')

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             username = u_form.cleaned_data.get('username')
#             messages.success(request, f'{username}, Your account has been updated!')
#             return redirect('profile')

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#     return render(request, 'users/profile.html', context)