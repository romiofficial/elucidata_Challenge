from django.db import models

class quiz_portal(models.Model):
    name=models.CharField(max_length=500)
    options=models.CharField(max_length=500)
    correct_option=models.CharField(max_length=500)
    quiz=models.CharField(max_length=500)
    points=models.CharField(max_length=500)

    def __str__(self):
        return self.name+'-'+self.quiz