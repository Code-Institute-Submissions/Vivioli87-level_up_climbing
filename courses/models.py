from django.db import models

class Level(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class CourseType(models.Model):
    level = models.ForeignKey('Level', null=True, blank=True,
                              on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
                                  

class Course(models.Model):
    level = models.ForeignKey('Level', null=True, blank=True,
                              on_delete=models.SET_NULL)
    name = models.ForeignKey('CourseType', null=True, blank=True,
                             on_delete=models.SET_NULL)
    start_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
