# Generated by Django 4.1.2 on 2022-10-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ManyToManyField(through='simpleapp.PostCategory', to='simpleapp.newscategory'),
        ),
    ]
