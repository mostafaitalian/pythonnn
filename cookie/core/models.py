from django.db import models
from cookie.flavor.models import Flavor

# Create your models here.
class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
def get_image_url(instance, filename):
    return '/'.join(['icecream', instance.slug, filename])        
class IceCream(TimeStamp):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to=get_image_url)
    flavors = models.ManyToManyField(Flavor, related_name='icecreams', on_delete=models.CASCADE)
    def __str__(self):
        return self.name + '--{}'.format(self.created)
    class Meta:
        ordering = ['-created', 'name']
