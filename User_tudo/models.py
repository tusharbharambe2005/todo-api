from django.db import models


class User_model(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    user_number = models.CharField(max_length=10)

    class Meta:
        ordering = ['created']  
    def __str__(self):
        return self.user_name

#tudo_list
class tudo_list_model(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    tudo_id = models.AutoField(primary_key=True)
    user_work = models.TextField(max_length=250)

    user_tudo_relation = models.ForeignKey(User_model,on_delete=models.CASCADE)







