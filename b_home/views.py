from django.views import generic
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_details.html'
    
class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    
class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    
class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')