from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    year_permissions = permission_class.objects.filter(content_type__app_label='webinfo',
                                                             content_type__model='year')

    nation_permissions = permission_class.objects.filter(content_type__app_label='webinfo',
                                                          content_type__model='nation')

    publisher_permissions = permission_class.objects.filter(content_type__app_label='webinfo',
                                                                  content_type__model='publisher')

    type_permissions = permission_class.objects.filter(content_type__app_label='webinfo',
                                                                  content_type__model='type')

    rate_permissions = permission_class.objects.filter(content_type__app_label='webinfo',
                                                           content_type__model='rate')

    user_permissions = permission_class.objects.filter(content_type__app_label='webinfo',
                                                         content_type__model='systemuser')

    book_permissions = permission_class.objects.filter(content_type__app_label='webinfo',
                                                          content_type__model='book')

    author_permissions = permission_class.objects.filter(content_type__app_label='webinfo',
                                                               content_type__model='author')

    explain_permissions = permission_class.objects.filter(content_type__app_label='webinfo',
                                                       content_type__model='explain')

    write_permissions = permission_class.objects.filter(content_type__app_label='webinfo',
                                                         content_type__model='write')

    like_permissions = permission_class.objects.filter(content_type__app_label='webinfo',
                                                            content_type__model='like')

    prefer_permissions = permission_class.objects.filter(content_type__app_label='webinfo',
                                                       content_type__model='prefer')

    post_permissions = permission_class.objects.filter(content_type__app_label='webinfo',
                                                       content_type__model='post')

    comment_permissions = permission_class.objects.filter(content_type__app_label='webinfo',
                                                       content_type__model='comment')

    activity_permissions = permission_class.objects.filter(content_type__app_label='webinfo',
                                                       content_type__model='activity')

    participate_permissions = permission_class.objects.filter(content_type__app_label='webinfo',
                                                         content_type__model='participate')


    perm_view_year = permission_class.objects.filter(content_type__app_label='webinfo',
                                                           content_type__model='year',
                                                           codename='view_year')

    perm_view_nation = permission_class.objects.filter(content_type__app_label='webinfo',
                                                        content_type__model='nation',
                                                        codename='view_nation')

    perm_view_publisher = permission_class.objects.filter(content_type__app_label='webinfo',
                                                               content_type__model='publisher',
                                                               codename='view_publisher')

    perm_view_type = permission_class.objects.filter(content_type__app_label='webinfo',
                                                               content_type__model='type',
                                                               codename='view_type')

    perm_view_rate = permission_class.objects.filter(content_type__app_label='webinfo',
                                                         content_type__model='rate',
                                                         codename='view_rate')

    perm_view_user = permission_class.objects.filter(content_type__app_label='webinfo',
                                                       content_type__model='systemuser',
                                                       codename='view_systemuser')

    perm_view_book = permission_class.objects.filter(content_type__app_label='webinfo',
                                                        content_type__model='book',
                                                        codename='view_book')

    perm_view_author = permission_class.objects.filter(content_type__app_label='webinfo',
                                                             content_type__model='author',
                                                             codename='view_author')

    perm_view_explain = permission_class.objects.filter(content_type__app_label='webinfo',
                                                           content_type__model='explain',
                                                           codename='view_explain')

    perm_view_write = permission_class.objects.filter(content_type__app_label='webinfo',
                                                        content_type__model='write',
                                                        codename='view_write')

    perm_view_like = permission_class.objects.filter(content_type__app_label='webinfo',
                                                               content_type__model='like',
                                                               codename='view_like')

    perm_view_prefer = permission_class.objects.filter(content_type__app_label='webinfo',
                                                               content_type__model='prefer',
                                                               codename='view_prefer')

    perm_view_post = permission_class.objects.filter(content_type__app_label='webinfo',
                                                         content_type__model='post',
                                                         codename='view_post')

    perm_view_comment = permission_class.objects.filter(content_type__app_label='webinfo',
                                                       content_type__model='comment',
                                                       codename='view_comment')

    perm_view_activity = permission_class.objects.filter(content_type__app_label='webinfo',
                                                        content_type__model='activity',
                                                        codename='view_activity')

    perm_view_participate = permission_class.objects.filter(content_type__app_label='webinfo',
                                                             content_type__model='participate',
                                                             codename='view_participate')

    perm_delete_post = permission_class.objects.filter(content_type__app_label='webinfo',
                                                        content_type__model='post',
                                                        codename='delete_post')

    perm_delete_comment = permission_class.objects.filter(content_type__app_label='webinfo',
                                                             content_type__model='comment',
                                                             codename='delete_comment')

    user_permissions = chain(
        perm_view_year,
        perm_view_nation,
        perm_view_publisher,
        perm_view_type,
        perm_view_rate,
        book_permissions,
        author_permissions,
        explain_permissions,
        write_permissions,
        like_permissions,
        prefer_permissions,
        post_permissions,
        comment_permissions,
        perm_view_activity,
        participate_permissions
    )

    activity_scheduler_permissions = chain(
        perm_view_year,
        perm_view_nation,
        perm_view_publisher,
        perm_view_type,
        perm_view_rate,
        perm_view_user,
        perm_view_book,
        perm_view_author,
        perm_view_explain,
        perm_view_write,
        perm_view_post,
        perm_view_comment,
        activity_permissions,
        perm_view_participate
    )

    info_manager_permissions = chain(
        year_permissions,
        nation_permissions,
        publisher_permissions,
        type_permissions,
        rate_permissions,
        perm_view_user,
        book_permissions,
        author_permissions,
        explain_permissions,
        write_permissions,
        perm_view_post,
        perm_view_comment,
        perm_delete_post,
        perm_delete_comment,
        perm_view_activity,
        perm_view_participate
    )

    my_groups_initialization_list = [
        {
            "name": "user",
            "permissions_list": user_permissions,
        },
        {
            "name": "activity_scheduler",
            "permissions_list": activity_scheduler_permissions,
        },
        {
            "name": "info_manager",
            "permissions_list": info_manager_permissions,
        },
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('webinfo', '0010_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
