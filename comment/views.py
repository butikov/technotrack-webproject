from django.views.generic import DetailView, ListView

from .models import Comment


class CommentView(DetailView):
    model = Comment
    context_object_name = 'comment'
    template_name = 'comment.html'


class CommentsList(ListView):
    model = Comment
    context_object_name = 'comments'
