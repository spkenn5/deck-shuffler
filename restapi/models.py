from django.db import models

class Cards(models.Model):
    dbf_id = models.IntegerField(max_length=30)
    player_class = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'cards'