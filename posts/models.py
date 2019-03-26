import datetime

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from categories.models import Category

from .models_manager import PostManager

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Category)
    thumbnail = models.ImageField(upload_to="images")

    objects = PostManager()

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"slug": self.slug})

    @property
    def total_comments(self):
        return len(self.comments)

    @property
    def comments(self):
        return self.comment_set.all()

    @property
    def get_next_by_created_at(self):
        return self.__class__.objects.filter(id__gt=self.id).order_by('id').first()

    @property
    def get_previous_by_created_at(self):
        return self.__class__.objects.filter(id__lt=self.id).order_by('id').last()

    @property
    def how_old_post_is(self):
        post_time = self.updated
        post_time = post_time.replace(tzinfo=None)
        current_time = datetime.datetime.now()

        diff = current_time - post_time

        days, seconds = diff.days, diff.seconds
        hours = days * 24 + seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        weeks = days // 7
        months = days // 30
        years = months // 12

        if years > 0:
            return f"{years} years ago"
        elif months > 0:
            return f"{months} months ago"
        elif weeks > 0:
            return f"{weeks} weeks ago"
        elif days > 0:
            return f"{days} days ago"
        elif hours > 0:
            return f"{hours} hours ago"
        elif minutes > 0:
            return f"{minutes} minutes ago"
        else:
            return f"{seconds} seconds ago"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.content
