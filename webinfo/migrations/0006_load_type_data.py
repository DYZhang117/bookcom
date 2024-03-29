# Generated by Django 3.2.5 on 2022-04-16 04:09
from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations

TYPES = [
    { 'type': 'Fiction',},
    { 'type': 'Action and adventure',},
    { 'type': 'Alternate history',},
    { 'type': 'Anthology',},
    { 'type': 'Chick lit',},
    { 'type': 'Children',},
    { 'type': 'Classic',},
    { 'type': 'Comic book',},
    { 'type': 'Coming-of-age',},
    { 'type': 'Crime',},
    { 'type': 'Drama',},
    { 'type': 'Fairytale',},
    { 'type': 'Fantasy',},
    { 'type': 'Graphic novel',},
    { 'type': 'Historical fiction',},
    { 'type': 'Horror',},
    { 'type': 'Mystery',},
    { 'type': 'Paranormal romance',},
    { 'type': 'Picture book',},
    { 'type': 'Poetry',},
    { 'type': 'Political thriller',},
    { 'type': 'Romance',},
    { 'type': 'Satire',},
    { 'type': 'Science fiction',},
    { 'type': 'Short story',},
    { 'type': 'Suspense',},
    { 'type': 'Thriller',},
    { 'type': 'Western',},
    { 'type': 'Young adult',},
    { 'type': 'Nonfiction',},
    { 'type': 'Art/architecture',},
    { 'type': 'Autobiography',},
    { 'type': 'Biography',},
    { 'type': 'Business/economics',},
    { 'type': 'Crafts/hobbies',},
    { 'type': 'Cookbook',},
    { 'type': 'Diary',},
    { 'type': 'Dictionary',},
    { 'type': 'Encyclopedia',},
    { 'type': 'Guide',},
    { 'type': 'Health/fitness',},
    { 'type': 'History',},
    { 'type': 'Home and garden',},
    { 'type': 'Humor',},
    { 'type': 'Journal',},
    { 'type': 'Math',},
    { 'type': 'Memoir',},
    { 'type': 'Philosophy',},
    { 'type': 'Prayer',},
    { 'type': 'Religion, spirituality, and new age',},
    { 'type': 'Textbook',},
    { 'type': 'True crime',},
    { 'type': 'Review',},
    { 'type': 'Science',},
    { 'type': 'Self help',},
    { 'type': 'Sports and leisure',},
    { 'type': 'Travel',},
    { 'type': 'True crime',}
]


def add_type_data(apps, schema_editor):
    type_class = apps.get_model('webinfo', 'Type')
    for type in TYPES:
        try:
            duplicate_object = type_class.objects.get(
                type=type['type']
            )
            print('Duplicate type entry not added to type table:', type['type'])
        except ObjectDoesNotExist:
            type_object = type_class.objects.create(
                type=type['type']
            )


def remove_type_data(apps, schema_editor):
    type_class = apps.get_model('webinfo', 'Type')
    for type in TYPES:
        type_object = type_class.objects.get(
            type=type['type']
        )
        type_object.delete()
        
        
class Migration(migrations.Migration):

    dependencies = [
        ('webinfo', '0005_load_nation_data'),
    ]

    operations = [
        migrations.RunPython(
            add_type_data,
            remove_type_data
        )
    ]
