from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Course(models.Model):
    slug = models.SlugField(verbose_name='Уникальное название курса', unique=True)
    title = models.CharField(verbose_name='Название курса', max_length=255)
    desc = models.TextField(verbose_name='Описание курса')
    image = models.ImageField(verbose_name='Изображение', default='default.png', upload_to='course_images', blank=True)
    is_free = models.BooleanField(verbose_name='Бесплатно?', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'slug': self.slug})


class Lesson(models.Model):
    slug = models.SlugField(verbose_name='Уникальное название урока')
    title = models.CharField(verbose_name='Название урока', max_length=255)
    desc = models.TextField(verbose_name='Описание урока')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Какой курс?')
    number = models.IntegerField(verbose_name='Номер урока')
    video = models.CharField(verbose_name='Видео URL', max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson-detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='комментатор')
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING, verbose_name='урок')
    comment = models.TextField(verbose_name='комментарий')

    # def __str__(self):
    #     return self.user.name