from django.db import models
from django.urls import reverse
from django.http import Http404


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True, unique=True, editable=False)

    def save(self, *args, **kwargs):

        # Making sure top menus have proper URLs
        if self.parent:
            self.url = self.parent.url + self.name + "/"
        else:
            self.url = "/menus/" + self.name + "/"

        # Hyphenization
        self.url = self.url.replace(" ", "-")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def children(self):
        return self.menuitem_set.all()

    def get_elder_ids(self):
        if self.parent:
            return self.parent.get_elder_ids() + [self.parent.id]
        else:
            return []
