# Generated by Django 5.0.6 on 2024-05-31 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_comment_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
