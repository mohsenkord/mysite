# Generated by Django 5.0.3 on 2024-04-17 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
