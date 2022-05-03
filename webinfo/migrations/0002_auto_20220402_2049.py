# Generated by Django 3.2.5 on 2022-04-02 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['first_name', 'last_name', 'nation', 'disambiguator']},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['book_name', 'year', 'publisher']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['post__post_title', 'content']},
        ),
        migrations.AlterModelOptions(
            name='explain',
            options={'ordering': ['type', 'book']},
        ),
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ['user', 'book']},
        ),
        migrations.AlterModelOptions(
            name='nation',
            options={'ordering': ['nation']},
        ),
        migrations.AlterModelOptions(
            name='participate',
            options={'ordering': ['user', 'activity']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['book', 'post_title']},
        ),
        migrations.AlterModelOptions(
            name='prefer',
            options={'ordering': ['user', 'type']},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['publisher_name']},
        ),
        migrations.AlterModelOptions(
            name='rate',
            options={'ordering': ['rate_sequence']},
        ),
        migrations.AlterModelOptions(
            name='systemuser',
            options={'ordering': ['last_name', 'first_name', 'disambiguator']},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ['type']},
        ),
        migrations.AlterModelOptions(
            name='write',
            options={'ordering': ['author', 'book']},
        ),
        migrations.AlterModelOptions(
            name='year',
            options={'ordering': ['year']},
        ),
        migrations.AddConstraint(
            model_name='activity',
            constraint=models.UniqueConstraint(fields=('name', 'date', 'address'), name='unique_activity'),
        ),
        migrations.AddConstraint(
            model_name='author',
            constraint=models.UniqueConstraint(fields=('last_name', 'first_name', 'nation', 'disambiguator'), name='unique_author'),
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.UniqueConstraint(fields=('book_name', 'year', 'publisher'), name='unique_book'),
        ),
        migrations.AddConstraint(
            model_name='comment',
            constraint=models.UniqueConstraint(fields=('user', 'content', 'post'), name='unique_comment'),
        ),
        migrations.AddConstraint(
            model_name='explain',
            constraint=models.UniqueConstraint(fields=('book', 'type'), name='unique_explain'),
        ),
        migrations.AddConstraint(
            model_name='like',
            constraint=models.UniqueConstraint(fields=('user', 'book'), name='unique_like'),
        ),
        migrations.AddConstraint(
            model_name='participate',
            constraint=models.UniqueConstraint(fields=('user', 'activity'), name='unique_participate'),
        ),
        migrations.AddConstraint(
            model_name='post',
            constraint=models.UniqueConstraint(fields=('post_title', 'user', 'book'), name='unique_post'),
        ),
        migrations.AddConstraint(
            model_name='prefer',
            constraint=models.UniqueConstraint(fields=('user', 'type'), name='unique_prefer'),
        ),
        migrations.AddConstraint(
            model_name='systemuser',
            constraint=models.UniqueConstraint(fields=('last_name', 'first_name', 'disambiguator'), name='unique_systemuser'),
        ),
        migrations.AddConstraint(
            model_name='write',
            constraint=models.UniqueConstraint(fields=('book', 'author'), name='unique_write'),
        ),
    ]