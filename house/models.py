# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Chengjiao(models.Model):
    sign_at = models.DateTimeField(blank=True, null=True)
    sign_method = models.CharField(max_length=256, blank=True, null=True)
    total_price = models.CharField(max_length=256, blank=True, null=True)
    unit_price = models.CharField(max_length=256, blank=True, null=True)
    building_structure = models.CharField(max_length=256, blank=True, null=True)
    building_floor = models.CharField(max_length=256, blank=True, null=True)
    building_size = models.CharField(max_length=256, blank=True, null=True)
    building_meta = models.CharField(max_length=256, blank=True, null=True)
    building_style = models.CharField(max_length=256, blank=True, null=True)
    building_towards = models.CharField(max_length=256, blank=True, null=True)
    building_year = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    city_area = models.CharField(max_length=256, blank=True, null=True)
    area_name = models.CharField(max_length=256, blank=True, null=True)
    community_name = models.CharField(max_length=256, blank=True, null=True)
    community_meta = models.TextField(blank=True, null=True)
    origin_title = models.CharField(max_length=256, blank=True, null=True)
    origin_url = models.CharField(max_length=256, blank=True, null=True)
    input_at = models.DateTimeField(blank=True, null=True)
    hid = models.CharField(unique=True, max_length=36)
    rid = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'chengjiao'


class Ershoufang(models.Model):
    hid = models.CharField(unique=True, max_length=36)
    rid = models.CharField(max_length=36)
    price_total = models.BigIntegerField(blank=True, null=True)
    unit_price = models.BigIntegerField(blank=True, null=True)
    cost_payment = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    city_area = models.CharField(max_length=256, blank=True, null=True)
    area_name = models.CharField(max_length=256, blank=True, null=True)
    community_name = models.CharField(max_length=256, blank=True, null=True)
    community_meta = models.TextField(blank=True, null=True)
    origin_title = models.CharField(max_length=256, blank=True, null=True)
    origin_url = models.CharField(max_length=256, blank=True, null=True)
    input_at = models.DateTimeField(blank=True, null=True)
    base_attributes = models.TextField(blank=True, null=True)
    transaction_attributes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ershoufang'


class Xiaoqu(models.Model):
    city = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    average_price = models.BigIntegerField(blank=True, null=True)
    service_fees = models.CharField(max_length=256, blank=True, null=True)
    service_company = models.CharField(max_length=256, blank=True, null=True)
    developers = models.CharField(max_length=256, blank=True, null=True)
    building_type = models.CharField(max_length=256, blank=True, null=True)
    building_count = models.CharField(max_length=256, blank=True, null=True)
    building_year = models.CharField(max_length=100, blank=True, null=True)
    house_count = models.CharField(max_length=256, blank=True, null=True)
    origin_title = models.CharField(max_length=256, blank=True, null=True)
    origin_url = models.CharField(max_length=256, blank=True, null=True)
    input_at = models.DateTimeField(blank=True, null=True)
    rid = models.CharField(unique=True, max_length=36, blank=True, null=True)
    lng = models.CharField(max_length=256, blank=True, null=True)
    lat = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xiaoqu'
