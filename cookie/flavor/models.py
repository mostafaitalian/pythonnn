from django.conf import settings
from django.db import models
from cookie.core.models import TimeStamp
from django.utils import timezone
# Create your models here.
class Flavor(TimeStamp):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    
    def __str__(self):
        self.title
class PublishedManager(models.Manager):
    use_for_related_fields=True
    def published(self):
        return self.filter(pub_date__lte=timezone.now())
class FlavorReview(models.Model):
    @classmethod
    def create_review(cls, user, flavor, review):
        flavor_review = cls(user=user,flavor=flavor, review=review)
        flavor_review.save()
        return
    review = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)
    objects = PublishedManager()
    def __str__(self):
        if self.user:
            return self.flavor + ' review by' + self.user
        else:
            return self.flavor + 'review'
        