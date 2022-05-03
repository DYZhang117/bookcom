from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webinfo.utils import ObjectCreateMixin, PageLinksMixin
from webinfo.forms import BookForm, AuthorForm, CommentForm, UserForm, ActivityForm, PostForm, PreferForm, LikeForm, \
    ExplainForm, WriteForm, ParticipateForm
from webinfo.models import Book, Author, Post, Activity, SystemUser, Like, Prefer, Comment, Explain, Write, Participate


class BookList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 10
    model = Book
    permission_required = 'webinfo.view_book'


class BookDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    permission_required = 'webinfo.view_book'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        book = self.get_object()
        post_list = book.posts.all()
        author_list = book.writes.all()
        explain_list = book.explains.all()
        context['post_list'] = post_list
        context['author_list'] = author_list
        context['explain_list'] = explain_list
        return context


class BookCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = BookForm
    model = Book
    permission_required = 'webinfo.add_book'


class BookUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = BookForm
    model = Book
    template_name = 'webinfo/book_form_update.html'
    permission_required = 'webinfo.change_book'


class BookDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('webinfo_book_list_urlpattern')
    permission_required = 'webinfo.delete_book'

    def get(self, request, pk):
        book = get_object_or_404(Book,pk=pk)
        posts = book.posts.all()
        likes = book.likes.all()
        writes = book.writes.all()
        explains = book.explains.all()
        if posts.count() > 0 or likes.count() > 0 or writes.count() > 0 or explains.count() > 0:
            return render(
                request,
                'webinfo/book_refuse_delete.html',
                {'book': book,
                 'posts': posts,
                 'likes': likes,
                 'writes': writes,
                 'explains': explains,
                 }
            )
        else:
            return render(
                request,
                'webinfo/book_confirm_delete.html',
                {'book': book}
            )


class AuthorList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 10
    model = Author
    permission_required = 'webinfo.view_author'


class AuthorDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Author
    permission_required = 'webinfo.view_author'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        author = self.get_object()
        book_list = author.writes.all()
        context['book_list'] = book_list
        return context


class AuthorCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = AuthorForm
    model = Author
    permission_required = 'webinfo.add_author'


class AuthorUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = AuthorForm
    model = Author
    template_name = 'webinfo/author_form_update.html'
    permission_required = 'webinfo.change_author'


class AuthorDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('webinfo_author_list_urlpattern')
    permission_required = 'webinfo.delete_author'

    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        writes = author.writes.all()
        if writes.count() > 0:
            return render(
                request,
                'webinfo/author_refuse_delete.html',
                {'author': author,
                 'writes': writes,
                 }
            )
        else:
            return render(
                request,
                'webinfo/author_confirm_delete.html',
                {'author': author}
            )


class PostList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 10
    model = Post
    permission_required = 'webinfo.view_post'


class PostDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Post
    permission_required = 'webinfo.view_post'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        post = self.get_object()
        post_title = post.post_title
        rate = post.rate
        content = post.content
        user = post.user
        book = post.book
        comment_list = post.comments.all()
        context['post_title'] = post_title
        context['rate'] = rate
        context['content'] = content
        context['user'] = user
        context['book'] = book
        context['comment_list'] = comment_list
        return context


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    permission_required = 'webinfo.add_post'


class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'webinfo/post_form_update.html'
    permission_required = 'webinfo.change_post'


class PostDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('webinfo_post_list_urlpattern')
    permission_required = 'webinfo.delete_post'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.all()
        if comments.count() > 0:
            return render(
                request,
                'webinfo/post_refuse_delete.html',
                {'post': post,
                 'comments': comments,
                 }
            )
        else:
            return render(
                request,
                'webinfo/post_confirm_delete.html',
                {'post': post}
            )


class ActivityList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 10
    model = Activity
    permission_required = 'webinfo.view_activity'


class ActivityDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Activity
    permission_required = 'webinfo.view_activity'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        activity = self.get_object()
        participate_list = activity.participates.all()
        context['participate_list'] = participate_list
        return context


class ActivityCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ActivityForm
    model = Activity
    permission_required = 'webinfo.add_activity'


class ActivityUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ActivityForm
    model = Activity
    template_name = 'webinfo/activity_form_update.html'
    permission_required = 'webinfo.change_activity'


class ActivityDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Activity
    success_url = reverse_lazy('webinfo_activity_list_urlpattern')
    permission_required = 'webinfo.delete_activity'

    def get(self, request, pk):
        activity = get_object_or_404(Activity, pk=pk)
        participates = activity.participates.all()
        if participates.count() > 0:
            return render(
                request,
                'webinfo/activity_refuse_delete.html',
                {'activity': activity,
                 'participates': participates,
                 }
            )
        else:
            return render(
                request,
                'webinfo/activity_confirm_delete.html',
                {'activity': activity}
            )


class UserList(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'webinfo.view_systemuser'
    def get(self, request):
        return render(
            request,
            'webinfo/user_list.html',
            {'user_list': SystemUser.objects.all()}
        )


class UserDetail(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'webinfo.view_systemuser'
    def get(self, request, pk):
        user = get_object_or_404(
            SystemUser,
            pk=pk
        )
        post_list = user.posts.all()
        comment_list = user.comments.all()
        like_list = user.likes.all()
        activity_list = user.participates.all()
        prefer_list = user.prefers.all()
        return render(
            request,
            'webinfo/user_detail.html',
            {'user': user,
             'post_list': post_list,
             'comment_list': comment_list,
             'like_list': like_list,
             'activity_list': activity_list,
             'prefer_list': prefer_list
             }
        )


class UserCreate(LoginRequiredMixin, PermissionRequiredMixin, ObjectCreateMixin, View):
    permission_required = 'webinfo.add_systemuser'
    form_class = UserForm
    template_name = 'webinfo/user_form.html'


class UserUpdate(LoginRequiredMixin, PermissionRequiredMixin, View):
    form_class = UserForm
    model = SystemUser
    template_name = 'webinfo/user_form_update.html'
    permission_required = 'webinfo.change_systemuser'

    def get_object(self, pk):
        return get_object_or_404(
            self.model,
            pk=pk)

    def get(self, request, pk):
        user = self.get_object(pk)
        context = {
            'form': self.form_class(
                instance=user),
            'user': user,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        user = self.get_object(pk)
        bound_form = self.form_class(
            request.POST, instance=user)
        if bound_form.is_valid():
            new_user = bound_form.save()
            return redirect(new_user)
        else:
            context = {
                'form': bound_form,
                'user': user,
            }
            return render(
                request,
                self.template_name,
                context)


class UserDelete(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'webinfo.delete_systemuser'
    def get(self, request, pk):
        user = self.get_object(pk)
        posts = user.posts.all()
        likes = user.likes.all()
        prefers = user.prefers.all()
        comments = user.comments.all()
        participates = user.participates.all()
        if posts.count() > 0 or likes.count() > 0 or prefers.count() > 0 or comments.count() > 0 or participates.count() > 0:
            return render(
                request,
                'webinfo/user_refuse_delete.html',
                {'user': user,
                 'posts': posts,
                 'likes': likes,
                 'prefers': prefers,
                 'comments': comments,
                 'participates': participates
                 }
            )
        else:
            return render(
                request,
                'webinfo/user_confirm_delete.html',
                {'user': user}
            )

    def get_object(self, pk):
        return get_object_or_404(
            SystemUser,
            pk=pk)

    def post(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return redirect('webinfo_user_list_urlpattern')


class LikeList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Like
    permission_required = 'webinfo.view_like'


class LikeDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Like
    permission_required = 'webinfo.view_like'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        like = self.get_object()
        user = like.user
        book = like.book
        context['user'] = user
        context['book'] = book
        return context


class LikeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = LikeForm
    model = Like
    permission_required = 'webinfo.add_like'


class LikeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = LikeForm
    model = Like
    template_name = 'webinfo/like_form_update.html'
    permission_required = 'webinfo.change_like'


class LikeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Like
    success_url = reverse_lazy('webinfo_like_list_urlpattern')
    permission_required = 'webinfo.delete_like'


class PreferList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Prefer
    permission_required = 'webinfo.view_prefer'


class PreferDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Prefer
    permission_required = 'webinfo.view_prefer'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        prefer = self.get_object()
        user = prefer.user
        context['user'] = user
        return context


class PreferCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PreferForm
    model = Prefer
    permission_required = 'webinfo.add_prefer'


class PreferUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PreferForm
    model = Prefer
    template_name = 'webinfo/prefer_form_update.html'
    permission_required = 'webinfo.change_prefer'


class PreferDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Prefer
    success_url = reverse_lazy('webinfo_prefer_list_urlpattern')
    permission_required = 'webinfo.delete_prefer'


class CommentList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    paginate_by = 10
    model = Comment
    permission_required = 'webinfo.view_comment'


class CommentDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Comment
    permission_required = 'webinfo.view_comment'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        comment = self.get_object()
        user = comment.user
        post = comment.post
        context['user'] = user
        context['post'] = post
        return context


class CommentCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CommentForm
    model = Comment
    permission_required = 'webinfo.add_comment'


class CommentUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CommentForm
    model = Comment
    template_name = 'webinfo/comment_form_update.html'
    permission_required = 'webinfo.change_comment'


class CommentDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('webinfo_comment_list_urlpattern')
    permission_required = 'webinfo.delete_comment'


class ExplainList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Explain
    permission_required = 'webinfo.view_explain'


class ExplainDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Explain
    permission_required = 'webinfo.view_explain'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        explain = self.get_object()
        book = explain.book
        context['book'] = book
        return context


class ExplainCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ExplainForm
    model = Explain
    permission_required = 'webinfo.add_explain'


class ExplainUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ExplainForm
    model = Explain
    template_name = 'webinfo/explain_form_update.html'
    permission_required = 'webinfo.change_explain'


class ExplainDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Explain
    success_url = reverse_lazy('webinfo_explain_list_urlpattern')
    permission_required = 'webinfo.delete_explain'


class WriteList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Write
    permission_required = 'webinfo.view_write'


class WriteDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Write
    permission_required = 'webinfo.view_write'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        write = self.get_object()
        book = write.book
        author = write.author
        context['book'] = book
        context['author'] = author
        return context


class WriteCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = WriteForm
    model = Write
    permission_required = 'webinfo.add_write'


class WriteUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = WriteForm
    model = Write
    template_name = 'webinfo/write_form_update.html'
    permission_required = 'webinfo.change_write'


class WriteDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Write
    success_url = reverse_lazy('webinfo_write_list_urlpattern')
    permission_required = 'webinfo.delete_write'


class ParticipateList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Participate
    permission_required = 'webinfo.view_participate'


class ParticipateDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Participate
    permission_required = 'webinfo.view_participate'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        participate = self.get_object()
        user = participate.user
        activity = participate.activity
        context['user'] = user
        context['activity'] = activity
        return context
    

class ParticipateCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ParticipateForm
    model = Participate
    permission_required = 'webinfo.add_participate'


class ParticipateUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ParticipateForm
    model = Participate
    template_name = 'webinfo/participate_form_update.html'
    permission_required = 'webinfo.change_participate'


class ParticipateDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Participate
    success_url = reverse_lazy('webinfo_participate_list_urlpattern')
    permission_required = 'webinfo.delete_participate'
