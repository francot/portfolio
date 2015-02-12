from django.db import models

# Create your models here.

class JobCategory(models.Model):
    description = models.CharField(max_length=20)

    def __unicode__(self):
        return self.description


class Job(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(JobCategory, related_name='category')
    #TODO: non rendere possibile la scelta della prima categoria
    secondary_category = models.ForeignKey(JobCategory, null=True, blank=True, related_name='secondary_category')
    job_date = models.DateTimeField(null=True, blank=True)
    tag = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    priority = models.PositiveIntegerField(null=True, blank=True)


    def __unicode__(self):
        return str(self.title) + "/" + str(self.description) + "/" + str(self.category)
