from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse


class Year(models.Model):
    year_id = models.AutoField(primary_key=True)
    year = models.IntegerField(unique=True)

    def __str__(self):
        return '%s' % self.year

    class Meta:
        ordering = ['year']


class Nation(models.Model):
    nation_id = models.AutoField(primary_key=True)
    nation = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '%s' % self.nation

    class Meta:
        ordering = ['nation']


class Publisher(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    publisher_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '%s' % self.publisher_name

    class Meta:
        ordering = ['publisher_name']


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=225)
    textbook_or_not = models.BooleanField(default=False)
    year = models.ForeignKey(Year, related_name='books', on_delete=models.PROTECT)
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.PROTECT)

    def __str__(self):
        return '%s (%s)' % (self.book_name, self.year.year)

    def get_absolute_url(self):
        return reverse('webinfo_book_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('webinfo_book_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('webinfo_book_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['book_name', 'year', 'publisher']
        constraints = [
            UniqueConstraint(fields=['book_name', 'year', 'publisher'], name='unique_book')
        ]


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    disambiguator = models.CharField(max_length=45, blank=True, default='')
    nation = models.ForeignKey(Nation, related_name='authors', on_delete=models.PROTECT)
    year = models.ForeignKey(Year, related_name='authors', on_delete=models.PROTECT)

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s %s [%s]' % (self.first_name, self.last_name, self.nation.nation)
        else:
            result = '%s %s [%s] - %s' % (self.first_name, self.last_name, self.nation.nation, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('webinfo_author_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('webinfo_author_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('webinfo_author_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['first_name', 'last_name', 'nation', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'nation', 'disambiguator'],
                             name='unique_author')
        ]


class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.type

    class Meta:
        ordering = ['type']


class Explain(models.Model):
    explain_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, related_name='explains', on_delete=models.PROTECT)
    type = models.ForeignKey(Type, related_name='explains', on_delete=models.PROTECT)

    def __str__(self):
        return '{ %s } %s' % (self.type, self.book)

    def get_absolute_url(self):
        return reverse('webinfo_explain_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('webinfo_explain_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('webinfo_explain_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['type', 'book']
        constraints = [
            UniqueConstraint(fields=['book', 'type'], name='unique_explain')
        ]


class Write(models.Model):
    written_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, related_name='writes', on_delete=models.PROTECT)
    author = models.ForeignKey(Author, related_name='writes', on_delete=models.PROTECT)

    def __str__(self):
        return '%s / %s ' % (self.author, self.book)

    def get_absolute_url(self):
        return reverse('webinfo_write_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('webinfo_write_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('webinfo_write_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['author', 'book']
        constraints = [
            UniqueConstraint(fields=['book', 'author'], name='unique_write')
        ]


class SystemUser(models.Model):
    systemuser_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    disambiguator = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('webinfo_user_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('webinfo_user_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('webinfo_user_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['last_name', 'first_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'disambiguator'],
                             name='unique_systemuser')
        ]


class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(SystemUser, related_name='likes', on_delete=models.PROTECT)
    book = models.ForeignKey(Book, related_name='likes', on_delete=models.PROTECT)

    def __str__(self):
        return '%s / %s' % (self.user, self.book)

    def get_absolute_url(self):
        return reverse('webinfo_like_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('webinfo_like_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('webinfo_like_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['user', 'book']
        constraints = [
            UniqueConstraint(fields=['user', 'book'],
                             name='unique_like')
        ]


class Prefer(models.Model):
    prefer_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(SystemUser, related_name='prefers', on_delete=models.PROTECT)
    type = models.ForeignKey(Type, related_name='prefers', on_delete=models.PROTECT)

    def __str__(self):
        return '%s / %s' % (self.user, self.type)

    def get_absolute_url(self):
        return reverse('webinfo_prefer_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('webinfo_prefer_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('webinfo_prefer_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['user', 'type']
        constraints = [
            UniqueConstraint(fields=['user', 'type'], name='unique_prefer')
        ]


class Rate(models.Model):
    rate_id = models.AutoField(primary_key=True)
    rate_sequence = models.IntegerField(unique=True)
    rate_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.rate_name

    class Meta:
        ordering = ['rate_sequence']


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=255)
    content = models.TextField(default='NA')
    user = models.ForeignKey(SystemUser, related_name='posts', on_delete=models.PROTECT)
    book = models.ForeignKey(Book, related_name='posts', on_delete=models.PROTECT)
    rate = models.ForeignKey(Rate, related_name='posts', on_delete=models.PROTECT)

    def __str__(self):
        return 'post: [%s] - %s' % (self.book.book_name, self.post_title)

    def get_absolute_url(self):
        return reverse('webinfo_post_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('webinfo_post_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('webinfo_post_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['book', 'post_title']
        constraints = [
            UniqueConstraint(fields=['post_title', 'user', 'book'], name='unique_post')
        ]


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=255)
    user = models.ForeignKey(SystemUser, related_name='comments', on_delete=models.PROTECT)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.PROTECT)

    def __str__(self):
        return 'comment: [%s] - %s' % (self.post.post_title, self.content)

    def get_absolute_url(self):
        return reverse('webinfo_comment_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('webinfo_comment_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('webinfo_comment_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['post__post_title', 'content']
        constraints = [
            UniqueConstraint(fields=['user', 'content', 'post'], name='unique_comment')
        ]


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # date = models.DateTimeField(auto_now=False)
    date = models.DateField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False)
    address = models.CharField(max_length=255)
    description = models.TextField(default='NA')

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('webinfo_activity_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('webinfo_activity_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('webinfo_activity_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['date', 'time', 'name']
        constraints = [
            UniqueConstraint(fields=['name', 'date', 'address'], name='unique_activity')
        ]


class Participate(models.Model):
    participate_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(SystemUser, related_name='participates', on_delete=models.PROTECT)
    activity = models.ForeignKey(Activity, related_name='participates', on_delete=models.PROTECT)

    def __str__(self):
        return '%s [registers] %s' % (self.user, self.activity)

    def get_absolute_url(self):
        return reverse('webinfo_participate_detail_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_update_url(self):
        return reverse('webinfo_participate_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('webinfo_participate_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['user', 'activity']
        constraints = [
            UniqueConstraint(fields=['user', 'activity'], name='unique_participate')
        ]
