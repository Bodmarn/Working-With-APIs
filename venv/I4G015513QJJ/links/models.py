from I4G015513QJJ.links.views import ActiveLinkView
from django.db import models
from datetime import datetime


# Create your models here.
class links (models.Model) :
    target_url = models.URLField(max_lenght=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(Set_blank=True )
    author = models.ForeignKey(get_user_model=())
    created_date = models.DateTimeField (auto_now_add=False, auto_now=False,blank=True)
    active =  models.BooleanField (True)
    objects = models.Manager()
    public = ActiveLinkView.Manager()