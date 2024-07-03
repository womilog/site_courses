from django.db import models
from django.contrib.auth.models import User
from PIL import Image


CHOICES = (('male', 'Мужской пол'), ('female', 'Женский пол'))
TYPE_ACCOUNT = (('full', 'Полный пакет'), ('free', 'Бесплатный пакет'))


class Profile(models.Model):
    CHOICES = (('male', 'Мужской пол'), ('female', 'Женский пол'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователся', default='default.png', upload_to='user_images')
    account_type = models.CharField(choices=TYPE_ACCOUNT, default='free', max_length=30)
    male = models.CharField(max_length=6, choices=CHOICES, default='male')
    accept = models.BooleanField(verbose_name='Согласие на отправку уведомлений на почту ', default=True)

    def __str__(self):
        return f'Профайл пользователся {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'