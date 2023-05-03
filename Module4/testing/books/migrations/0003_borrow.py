# Generated by Django 4.2 on 2023-05-03 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0002_rename_post_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed', models.DateTimeField(auto_now_add=True)),
                ('returned', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_returned', models.BooleanField()),
                ('book_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
