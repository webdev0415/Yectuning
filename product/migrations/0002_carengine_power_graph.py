# Generated by Django 3.0.8 on 2020-09-07 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carengine',
            name='power_graph',
            field=models.ImageField(default='images/engine/watermark_91.jpg', help_text='Upload The Image For The Power Graph', upload_to='images/engine/'),
            preserve_default=False,
        ),
    ]
