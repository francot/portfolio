from django.shortcuts import render,  get_object_or_404

from django.http import HttpResponse
from django.template import Context, loader

from portfolio.models import Job, JobCategory
# Create your views here.


def index(request):
    latest_jobs = Job.objects.all().order_by('date')
    category = JobCategory.objects.all().order_by('description')
    t = loader.get_template('portfolio/index.html')
    context_dict = ({'latest_jobs': latest_jobs, 'category': category, })
    for job in latest_jobs:
        job.url = job.title.replace(' ','_')

    c = Context(context_dict)
    return HttpResponse (t.render(c))


def job(request, job_url):
    single_job = get_object_or_404(Job, title=job_url.replace('_',' '))
    t = loader.get_template('portfolio/job.html')
    c = Context ({'single_job': single_job,})
    return HttpResponse (t.render(c))


#def add_post(request):
#    context_dict
