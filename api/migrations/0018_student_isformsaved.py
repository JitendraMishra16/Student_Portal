# Generated by Django 3.2.7 on 2021-10-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_student_studentname'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='IsformSaved',
            field=models.TextField(blank=True, default='false', null=True),
        ),
    ]
