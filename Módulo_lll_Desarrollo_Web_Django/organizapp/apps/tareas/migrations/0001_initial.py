# Generated by Django 2.2 on 2019-05-04 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Homeworks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreHomework', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaEntrega', models.DateTimeField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='img/hw/%Y-%m-%d/')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
