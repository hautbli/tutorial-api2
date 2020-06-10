from django.contrib.auth.models import User
from django.db import models



class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    content = models.CharField(max_length=100, default="")

# from django.contrib.auth.models import User
# for i in range(20):
#     c = Card.objects.create(content="ㅎㅁㅎㅁㅎㅁㅎㅁㅎ",user=User.objects.get(pk=1), )