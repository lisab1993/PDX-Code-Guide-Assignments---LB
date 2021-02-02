import datetime

from django.utils import timezone
from django.db import models

# ORM: object relational mapping. Mapping things to tables in
#  the database.
# Don't delete tables or anything in dbsqlite.

# Get your database structure set early.
# this particular structure says that one questions can have
#  multiple choices.

# models should be in pascal case, and a singular noun.
# ex: use question, not questions, even though there may be many.


class Question(models.Model):
    # these fields become the columns of the database table
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        #see if something was published in the last day.
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#the foreign key creates a many-to-one relationship
#the related name controls how the 'one' refers to the 'many'

class Choice(models.Model):
    # these represent the properties of the class instances
 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question.question_text + " " + self.choice_text
