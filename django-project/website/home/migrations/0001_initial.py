# Generated by Django 4.0.4 on 2022-04-24 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Functions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outpic', models.ImageField(height_field=1024, upload_to='', width_field=1024)),
                ('inpic', models.ImageField(height_field=1024, upload_to='', width_field=1024)),
            ],
            options={
                'verbose_name': '图片操作',
                'verbose_name_plural': '图片操作',
            },
        ),
        migrations.CreateModel(
            name='Cd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_text', models.CharField(max_length=200)),
                ('cd_num', models.IntegerField()),
                ('pic_in', models.ManyToManyField(related_name='pic_input', to='home.pic', verbose_name='图片输入')),
                ('pic_out', models.ManyToManyField(related_name='pic_output', to='home.pic', verbose_name='图片输出')),
            ],
            options={
                'verbose_name': '变化检测',
                'verbose_name_plural': '变化检测',
            },
        ),
    ]