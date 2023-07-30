# Generated by Django 4.0.6 on 2023-04-18 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0010_alter_childpersonalinfo_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='wechslerchild',
            name='birthdate',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wechslerchild',
            name='range',
            field=models.IntegerField(default=None, editable=False),
            preserve_default=False,
        ),
    ]
