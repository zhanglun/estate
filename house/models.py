from django.db import models


# Create your models here.

class Estate(models.Model):
    def __str__(self):
        title = '{area}-{community}-{title}'

        return title.format(area=self.area_name, community=self.community_name, title=self.title)

    origin_url = models.CharField(max_length=256, null=True)
    title = models.CharField(max_length=256, null=True)
    hid = models.CharField(max_length=32, null=True)
    rid = models.CharField(max_length=32, null=True)
    city = models.CharField(max_length=10, null=True)
    community_name = models.CharField(max_length=256, null=True)
    area_name = models.CharField(max_length=256, null=True)
    price_total = models.BigIntegerField(10, null=True)
    price_total_unit = models.CharField(max_length=10, null=True)
    unit_price = models.BigIntegerField(10, null=True)
    transaction = models.TextField(null=True)
    cost_payment = models.TextField(null=True)
    input_time = models.DateTimeField(null=True)

