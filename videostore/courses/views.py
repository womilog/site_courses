from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddCourse, CommentForm
from .models import Course, Lesson, Comment
from cloudipsp import Api, Checkout
import time


def tarrifsPage(request):
    api = Api(merchant_id=1397120,
              secret_key='test'
              )
    checkout = Checkout(api=api)
    data = {
        'currency': 'USD',
        'amount': 1500,
        'order_decs': 'Покупка подписки на сайте',
        'order_id': str(time.time()),
    }
    url = checkout.url(data).get('checkout_url')
    return render(request, 'courses/tarrifs.html', {'title': 'Тарифы на сайте', 'url': url})


class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Главная страница сайта'
        return ctx


class CourseDetailPage(DetailView):
    model = Course
    template_name = 'courses/course-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CourseDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['title'] = course
        ctx['lessons'] = Lesson.objects.filter(course=course).order_by('number')
        return ctx


class LessonDetailPage(DetailView):
    model = Course
    template_name = 'courses/lesson-detail.html'
    form_class = CommentForm

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LessonDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()
        lesson.video = lesson.video.split('=')[-1]

        comments = Comment.objects.filter(lesson__slug=lesson.slug)

        ctx['title'] = lesson
        ctx['lesson'] = lesson
        ctx['comments'] = comments
        ctx['form'] = CommentForm()
        return ctx

    def post(self, request, *args, **kwargs):
        lesson = Lesson.objects.get(slug=self.kwargs['lesson_slug'])

        post = request.POST.copy()
        post['user'] = request.user
        post['lesson'] = lesson
        request.POST = post

        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()

        url = self.kwargs['slug'] + '/' + self.kwargs['lesson_slug']
        return redirect('/course/' + url)


class AddCoursePage(CreateView):
    form_class = AddCourse
    # fields = ['slug', 'title', 'desc', 'image']
    template_name = 'courses/addcourse.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'title': 'Добавление курса'
    }