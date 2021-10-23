from django.db import models
from venues.models import Venue
from profiles.models import UserProfile


class Level(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    level = models.ForeignKey('Level', null=True, blank=True,
                              on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


# Linking table between lesson and course type
class CourseLesson(models.Model):
    name = models.CharField(max_length=254)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    course_type = models.ForeignKey('CourseType', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Type of course that can be re-run on different dates
class CourseType(models.Model):
    level = models.ForeignKey('Level', null=True, blank=True,
                              on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


# A specific event of a course
class Course(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    level = models.ForeignKey('Level', null=True, blank=True,
                              on_delete=models.SET_NULL)
    course_type = models.ForeignKey('CourseType', null=True, blank=True,
                                    on_delete=models.SET_NULL)
    start_date = models.DateTimeField(auto_now_add=False)
    venue = models.ForeignKey(Venue, null=True, blank=True, on_delete=models.SET_NULL)
    coach = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
