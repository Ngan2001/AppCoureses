# Generated by Django 4.0.2 on 2022-03-25 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_lesson_content_alter_lesson_course_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='users/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='courses.lesson'),
        ),
    ]