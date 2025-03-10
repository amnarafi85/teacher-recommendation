# Generated by Django 5.1.6 on 2025-03-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=255)),
                ('student_id', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('grade_received', models.CharField(blank=True, max_length=10, null=True)),
                ('teacher_behavior', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('grading_criteria', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('teaching_quality', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('review_text', models.TextField()),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
    ]
