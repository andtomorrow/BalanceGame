
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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('select1_content', models.CharField(max_length=200)),
                ('select2_content', models.CharField(max_length=200)),
                ('image1', models.ImageField(blank=True, upload_to='%Y/%m/%d/')),
                ('image2', models.ImageField(blank=True, upload_to='%Y/%m/%d/')),
                ('like_users', models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL)),
                ('select1_users', models.ManyToManyField(related_name='select1_posts', to=settings.AUTH_USER_MODEL)),
                ('select2_users', models.ManyToManyField(related_name='select2_posts', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
