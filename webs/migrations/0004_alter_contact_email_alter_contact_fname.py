# Generated by Django 5.0.1 on 2024-02-07 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0003_rename_name_contact_fname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='fname',
            field=models.CharField(max_length=30),
        ),
    ]