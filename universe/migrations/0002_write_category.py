# Generated by Django 3.2.23 on 2023-11-22 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='write',
            name='category',
            field=models.CharField(choices=[('Video', 'Video'), ('Design', 'Design'), ('Photo', 'Photo'), ('Web', 'Web'), ('Composing', 'Composing'), ('Product Manager', 'Product Manager'), ('IOS', 'IOS'), ('Lyric', 'Lyric'), ('Vocal', 'Vocal'), ('Android', 'Android'), ('Marketing', 'Marketing'), ('Dance', 'Dance'), ('Server', 'Server'), ('Advertisement', 'Advertisement'), ('etc', 'etc')], max_length=20, null=True),
        ),
    ]
