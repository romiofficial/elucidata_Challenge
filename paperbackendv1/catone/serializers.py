from rest_framework import serializers
from .models import quiz_portal

class quiz_portal_Serializer(serializers.ModelSerializer):
    class Meta:
        model = quiz_portal
        fields='name','options','correct_option','quiz','points'
