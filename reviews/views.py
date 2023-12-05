from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

class ReviewListView(ListView):
    model = Post
    template_name = "review.html"
    context_object_name = "all_posts_list"
    

class ReviewDetailView(DetailView):
    model = Post
    template_name = "review_detail.html"


class ReviewCreateView(CreateView):
    model = Post
    fields = ('title', 'body')
    template_name = 'review_new.html'
    
    
class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'review_delete.html'
    success_url = reverse_lazy('review.html')
    
    
    def test_func(self):
        obj = self.get_object()
        
        return obj.author == self.request.user
    
    