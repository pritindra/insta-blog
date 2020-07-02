from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User, auth
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from .forms import NewCommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.


# def home(request):
#     context = {
#         'post': Post.objects.all
#     }
#     return render(request, 'home.html', context)



PAGINATION_COUNT = 3

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = PAGINATION_COUNT

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        all_users = []
        data_counter = Post.objects.values('author')\
            .annotate(author_count=Count('author'))\
            .order_by('-author_count')[:6]
        return data

    @login_required
    def postcreate(self, request, **kwargs):
        if request.method == 'POST':
            content = request.POST['message-text']
            poll_no = request.POST['poll_no']
        return self.get(self, request, **kwargs)

    


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments_connected = Comment.objects.filter(post_id=self.get_object()).order_by('-date')
        data['comments'] = comments_connected
        data['form'] = NewCommentForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(comment=request.POST.get('content'),
                              author=self.request.user,
                              post_id=self.get_object())
        new_comment.save()

        return self.get(self, request, *args, **kwargs)



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content', 'poll_no', 'anon']
    template_name = 'post_new.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # data['tag_line'] = 'Add a new post'
        return data





