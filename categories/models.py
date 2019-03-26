from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _


class Category(models.Model):
    name = models.CharField(max_length=250, primary_key=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"name": self.name})

    def total_posts(self):
        return len(self.post_set.all())
