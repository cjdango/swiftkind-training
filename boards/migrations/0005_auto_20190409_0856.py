# Generated by Django 2.2 on 2019-04-09 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_cardcomment_frm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardcomment',
            name='frm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]