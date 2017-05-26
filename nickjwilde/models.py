from django.db import models

# Create your models here.
class Skill(models.Model):
    num_years = models.IntegerField()
    image_name = models.CharField(max_length=255)

    def num_years_text(self):
        return "".join(str(self.num_years) + ' years' if self.num_years > 1 else str(self.num_years) + ' year')

    def __str__(self):
        return self.image_name.split('.')[0]
