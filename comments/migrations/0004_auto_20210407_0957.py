# Generated by Django 3.1.7 on 2021-04-07 09:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0023_delete_comment'),
        ('comments', '0003_auto_20210406_1721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_time'], 'verbose_name': 'comments', 'verbose_name_plural': 'comments'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.post', verbose_name='post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]