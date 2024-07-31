from django.db import models

# Create your models here.

class Register(models.Model):
    sid = models.IntegerField(primary_key=True)
    name = models.CharField( max_length=50)
    pno = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    add = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    cources = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Topic(models.Model):
    topicname=models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.topicname


class Author(models.Model):
    topicname=models.ForeignKey(Topic, on_delete=models.CASCADE)
    authorname=models.CharField(max_length=50, primary_key=True)
    url=models.CharField(max_length=50)

    def __str__(self):
        return self.authorname
    
class Book(models.Model):
    authorname = models.ForeignKey(Author, on_delete=models.CASCADE)
    bookname=models.CharField(max_length=50, primary_key=True)
    price=models.CharField(max_length=50)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return self.bookname