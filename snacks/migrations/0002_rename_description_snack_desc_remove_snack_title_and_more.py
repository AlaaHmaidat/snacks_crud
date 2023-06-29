# Generated by Django 4.2.2 on 2023-06-29 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snack',
            old_name='description',
            new_name='desc',
        ),
        migrations.RemoveField(
            model_name='snack',
            name='title',
        ),
        migrations.AddField(
            model_name='snack',
            name='name',
            field=models.CharField(default='snack', max_length=64),
        ),
        migrations.AlterField(
            model_name='snack',
            name='purchaser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]