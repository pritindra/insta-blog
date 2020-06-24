from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User, auth
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# Create your views here.
PAGINATION_COUNT = 3

# class PostListView(LoginRequiredMixin, ListView):
#     model = Post
#     template_name = 'home.html'
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     paginate_by = PAGINATION_COUNT

#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)

#         all_users = []
#         data_counter = Post.objects.values('author')\
#             .annotate(author_count=Count('author'))\
#             .order_by('-author_count')[:6]

#         for aux in data_counter:
#             all_users.append(User.objects.filter(pk=aux['author']).first())
#         # if Preference.objects.get(user = self.request.user):
#         #     data['preference'] = True
#         # else:
#         #     data['preference'] = False
#         data['preference'] = Preference.objects.all()
#         # print(Preference.objects.get(user= self.request.user))
#         data['all_users'] = all_users
#         print(all_users, file=sys.stderr)
#         return data

#     def get_queryset(self):
#         user = self.request.user
#         qs = Follow.objects.filter(user=user)
#         follows = [user]
#         for obj in qs:
#             follows.append(obj.follow_user)
#         return Post.objects.filter(author__in=follows).order_by('-date_posted')

def home(request):
    context = {
        'post': Post.objects.all
    }
    return render(request, 'home.html', context)
