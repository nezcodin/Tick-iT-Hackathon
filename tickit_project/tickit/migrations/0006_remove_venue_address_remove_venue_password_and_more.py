# Generated by Django 4.1.7 on 2023-04-03 23:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickit', '0005_alter_member_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='address',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='password',
        ),
        migrations.RemoveField(
            model_name='venue',
            name='username',
        ),
        migrations.AddField(
            model_name='venue',
            name='location',
            field=models.TextField(default='location'),
        ),
        migrations.AddField(
            model_name='venue',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='eventname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stuff', to='tickit.event', to_field='name'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usertickets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]