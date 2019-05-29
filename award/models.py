from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Project(models.Model):
    img = models.ImageField(default='leopard.jpg', upload_to='images')
    title = models.CharField(default='My Project', max_length = 30)
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(default='No link', max_length = 120)
    # up_vote = models.IntegerField(default=0)
    # down_vote = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    @classmethod
    def search_by_title(cls,search_term):
        projectis = cls.objects.filter(title__icontains=search_term)
        return projectis

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})

    # def was_published_recently(self):
    #     return self.date_posted >= timezone.now() - datetime.timedelta(days=1)

    #solves for me the error 'improperly configured' with suggestion
    #No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.

# class ImageVote(models.Model):

#     voter = models.ForeignKey(User, on_delete=models.CASCADE)
#     voted = models.ForeignKey(Image, on_delete=models.CASCADE)
#     published_date = models.DateField(auto_now_add=True, null=True)

#     class Meta:
#         unique_together = ('voter', 'voted')

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.voter

