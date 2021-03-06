# Generated by Django 2.1.2 on 2018-11-06 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LianjiaChengjiao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_at', models.DateTimeField(blank=True, null=True)),
                ('sign_method', models.CharField(blank=True, max_length=256, null=True)),
                ('total_price', models.CharField(blank=True, max_length=256, null=True)),
                ('unit_price', models.CharField(blank=True, max_length=256, null=True)),
                ('building_structure', models.CharField(blank=True, max_length=256, null=True)),
                ('building_floor', models.CharField(blank=True, max_length=256, null=True)),
                ('building_size', models.CharField(blank=True, max_length=256, null=True)),
                ('building_meta', models.CharField(blank=True, max_length=256, null=True)),
                ('building_style', models.CharField(blank=True, max_length=256, null=True)),
                ('building_towards', models.CharField(blank=True, max_length=256, null=True)),
                ('building_year', models.CharField(blank=True, max_length=256, null=True)),
                ('city', models.CharField(blank=True, max_length=256, null=True)),
                ('city_area', models.CharField(blank=True, max_length=256, null=True)),
                ('area_name', models.CharField(blank=True, max_length=256, null=True)),
                ('community_name', models.CharField(blank=True, max_length=256, null=True)),
                ('community_meta', models.CharField(blank=True, max_length=256, null=True)),
                ('origin_title', models.CharField(blank=True, max_length=256, null=True)),
                ('origin_url', models.CharField(blank=True, max_length=256, null=True)),
                ('input_at', models.DateTimeField(blank=True, null=True)),
                ('hid', models.CharField(max_length=36, unique=True)),
                ('rid', models.CharField(max_length=36)),
            ],
            options={
                'db_table': 'lianjia_chengjiao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LianjiaErshoufang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('hid', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('rid', models.CharField(blank=True, max_length=32, null=True)),
                ('price_total', models.BigIntegerField(blank=True, null=True)),
                ('price_total_unit', models.CharField(blank=True, max_length=4, null=True)),
                ('unit_price', models.BigIntegerField(blank=True, null=True)),
                ('community_name', models.CharField(blank=True, max_length=256, null=True)),
                ('area_name', models.CharField(blank=True, max_length=256, null=True)),
                ('input_time', models.DateTimeField(blank=True, null=True)),
                ('transaction', models.TextField(blank=True, null=True)),
                ('cost_payment', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=11, null=True)),
                ('extra', models.TextField(blank=True, null=True)),
                ('origin_url', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'lianjia_ershoufang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LianjiaXiaoqu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=256, null=True)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('average_price', models.BigIntegerField(blank=True, null=True)),
                ('service_fees', models.CharField(blank=True, max_length=256, null=True)),
                ('service_company', models.CharField(blank=True, max_length=256, null=True)),
                ('developers', models.CharField(blank=True, max_length=256, null=True)),
                ('building_type', models.CharField(blank=True, max_length=256, null=True)),
                ('building_count', models.CharField(blank=True, max_length=256, null=True)),
                ('building_year', models.CharField(blank=True, max_length=100, null=True)),
                ('house_count', models.CharField(blank=True, max_length=256, null=True)),
                ('origin_title', models.CharField(blank=True, max_length=256, null=True)),
                ('origin_url', models.CharField(blank=True, max_length=256, null=True)),
                ('input_at', models.DateTimeField(blank=True, null=True)),
                ('rid', models.CharField(blank=True, max_length=36, null=True, unique=True)),
                ('lng', models.CharField(blank=True, max_length=256, null=True)),
                ('lat', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'lianjia_xiaoqu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LianjiaZufang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hid', models.CharField(blank=True, max_length=36, null=True, unique=True)),
                ('city', models.CharField(blank=True, max_length=256, null=True)),
                ('city_area', models.CharField(blank=True, max_length=256, null=True)),
                ('area_name', models.CharField(blank=True, max_length=256, null=True)),
                ('community_name', models.CharField(blank=True, max_length=256, null=True)),
                ('community_meta', models.CharField(blank=True, max_length=256, null=True)),
                ('monthly_rent', models.BigIntegerField(blank=True, null=True)),
                ('monthly_rent_unit', models.CharField(blank=True, max_length=256, null=True)),
                ('decoration_type', models.CharField(blank=True, max_length=256, null=True)),
                ('space', models.CharField(blank=True, max_length=256, null=True)),
                ('inside_space', models.CharField(blank=True, max_length=256, null=True)),
                ('building_structure', models.CharField(blank=True, max_length=256, null=True)),
                ('building_floor', models.CharField(blank=True, max_length=256, null=True)),
                ('building_towards', models.CharField(blank=True, max_length=256, null=True)),
                ('subway_info', models.CharField(blank=True, max_length=256, null=True)),
                ('publish_time', models.CharField(blank=True, max_length=256, null=True)),
                ('lease_way', models.CharField(blank=True, max_length=256, null=True)),
                ('pay_way', models.CharField(blank=True, max_length=256, null=True)),
                ('status', models.CharField(blank=True, max_length=256, null=True)),
                ('heating_way', models.CharField(blank=True, max_length=256, null=True)),
                ('origin_title', models.CharField(blank=True, max_length=256, null=True)),
                ('origin_url', models.CharField(blank=True, max_length=256, null=True)),
                ('input_at', models.DateTimeField(blank=True, null=True)),
                ('lng', models.CharField(blank=True, max_length=256, null=True)),
                ('lat', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'lianjia_zufang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PollsChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField()),
            ],
            options={
                'db_table': 'polls_choice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PollsQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'polls_question',
                'managed': False,
            },
        ),
    ]
