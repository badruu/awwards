from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import generic
from django.db.models import F
from users.models import Profile
from . models import Project

def welcome(request):
    return render(request, 'award/welcome.html')

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['img','title','description','link']

    def form_valid(self, form):
        # we override the create validation to tell it this is the author of the post. Otherwise we'll get an integrity error
        form.instance.poster = self.request.user
        return super().form_valid(form)


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