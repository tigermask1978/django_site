# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

    def __str__(self):
        return self.name


class NewManager(models.Manager):
    pass


class MyPerson(Person):
    objects = NewManager()

    class Meta:
        proxy = True

    def do_something(self):
        pass

class OrderedPerson(Person):
    class Meta:
        ordering = ['last_name']
        proxy = True

class Group(models.Model):
    name = models.CharField("the group's name", max_length=128)
    members = models.ManyToManyField(Person, through='Membership', related_name='in_groups_set')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invited_reason = models.CharField(max_length=64)

    def __str__(self):
        return self.person.name + ' in ' + self.group.name


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Musician(models.Model):
    first_name = models.CharField("musician's first name", max_length=50)
    last_name = models.CharField("musician's last name", max_length=50)
    instrument = models.CharField("musician's instrument", max_length=100)

    def __str__(self):
        return self.first_name + '-' + self.last_name

    def _get_full_name(self):
        """Returns the full name"""
        return '%s %s' %(self.first_name, self.last_name)
    full_name = property(_get_full_name)


class Album(models.Model):
    artist = models.ForeignKey(Musician, verbose_name="the album's artist", on_delete=models.CASCADE)
    name = models.CharField("the album's name", max_length=100)
    release_date = models.DateField("the album's release date")
    num_stars = models.IntegerField("the album's num")

    def __str__(self):
        return self.name


class Organization(models.Model):
    organization_name = models.CharField(max_length=30)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='suborganizations')

    def __str__(self):
        return self.organization_name


class Teacher(models.Model):
    name = models.CharField("the teacher's name", max_length=40)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField("the course's name", max_length=40)
    teacher = models.ManyToManyField(Teacher, blank=True, related_name='courses_set')

    def __str__(self):
        return self.name


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    class Meta:
        db_table = 'student_info'

    def __str__(self):
        return self.home_group

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "restaurant"

class Supplier(Place):
    customers = models.ManyToManyField(Place, related_name='provider')

    def __str__(self):
        return "supplier"

# class Article(models.Model):
#     article_id = models.AutoField(primary_key=True)

# class Book(models.Model):
#     book_id = models.AutoField(primary_key=True)
#
# class BookReview(Article, Book):
#     pass


"""Making queries"""
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(null=True, max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)
    email = models.EmailField()
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline


class ThemeBlog(Blog):
    theme = models.CharField(max_length=200)

    def __str__(self):
        return self.theme

"""Aggregation"""
class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    pages = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(default=0.0)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    pubdate = models.DateField()

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=10)
    data = models.IntegerField()

    class Meta:
        ordering = ["name"]


"""Examples of model relationship API usage"""

"""Many-to-many relatonships"""


class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', )


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline', )

"""文件上传"""
class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')





