from django.db import models

# Create your models here.

# makemigration command ---> will convert the orm class into sql command
# migrate command --> will execute the sql command generated by the makemigration.

subject = 'computer'
dept = 'bsc'


class computer_bsc(models.Model) :
    filename = models.CharField(max_length = 1000)
    def __str__(self) :
        return self.filename