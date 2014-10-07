from django.db import models

# Create your models here.
class Repo(models.Model):
    original_url = models.CharField(max_length=200)
    path = models.CharField(max_length=100)

    def __str__(self):
        return "repo {0} from {1}".format(path, original_url)
