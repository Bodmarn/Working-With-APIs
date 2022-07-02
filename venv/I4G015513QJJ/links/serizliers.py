from os import link
from pyexpat import model
from rest_framework import serializers 

class LinkSerializer(serializers.ModelSerializer):
 class Meta:

  model = link

 fields = "__all__"