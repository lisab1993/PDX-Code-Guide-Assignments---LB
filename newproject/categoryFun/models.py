from django.db import models

class Fruit_Name(models.Model):
    title_text = models.CharField(max_length=200)
    associated_date = models.DateTimeField('your date here')

    def __str__(self):
        return self.title_text

    def was_expired_recently(self):
        #see if something was published in the last day.
        return self.associated_date >= timezone.now() - datetime.timedelta(days=1)


class Fruit_Color(models.Model):
    title = models.ForeignKey(Fruit_Name, on_delete=models.PROTECT)
    color_text = models.CharField(max_length=200)
    