# from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, unique=True)

    # def __str__(self):
    #     return self.first_name


class Album(models.Model):
    artist = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    num_stars = models.CharField(max_length=100)


class Topping(models.Model):
    T_id = models.CharField(primary_key=True, max_length=50)
    T_name = models.CharField(max_length=50)


class Pizza(models.Model):
    P_id = models.CharField(primary_key=True, max_length=50)
    P_name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)


#
#
# class MusicPerson(models.Model):
#     name = models.CharField(max_length=128)
#
#     def __str__(self):  # __unicode__ on Python 2
#         return self.name
#
#
# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(Person, through='Membership')
#
#     def __str__(self):  # __unicode__ on Python 2
#         return self.name
#
#
# class Membership(models.Model):
#     person = models.ForeignKey(MusicPerson)
#     group = models.ForeignKey(Group)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)
#
# class Place(models.Model):
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=80)
#
#     def __str__(self):  # __unicode__ on Python 2
#         return "%s the place" % self.name
#
#
# class Restaurant(models.Model):
#     place = models.OneToOneField(Place, primary_key=True)
#     serves_hot_dogs = models.BooleanField(default=False)
#     serves_pizza = models.BooleanField(default=False)
#
#     def __str__(self):  # __unicode__ on Python 2
#         return "%s the restaurant" % self.place.name
#
#
# class Waiter(models.Model):
#     restaurant = models.ForeignKey(Restaurant)
#     name = models.CharField(max_length=50)
#
#     def __str__(self):  # __unicode__ on Python 2
#         return "%s the waiter at %s" % (self.name, self.restaurant)
class derson(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)
