from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_details.html'