from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    description = models.TextField()
    pages = models.IntegerField()

    published_year = models.IntegerField(validators = [
MinValueValidator(1000),
MaxValueValidator(2100)
    ])
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null =True, blank=True)


    def  __str__(self) -> str:
        return self.title
    
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name ='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('book', 'user')

    def __str__(self):
        return f'{self.user.username} rated {self.book.title} ({self.rating})'


