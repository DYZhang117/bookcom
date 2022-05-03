from django.contrib import admin
from .models import (
    Activity,
    Author,
    Book,
    Comment,
    Explain,
    Like,
    Nation,
    Participate,
    Post,
    Prefer,
    Publisher,
    Rate,
    SystemUser,
    Type,
    Write,
    Year,
)

admin.site.register(Activity)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Explain)
admin.site.register(Like)
admin.site.register(Nation)
admin.site.register(Participate)
admin.site.register(Post)
admin.site.register(Prefer)
admin.site.register(Publisher)
admin.site.register(Rate)
admin.site.register(SystemUser)
admin.site.register(Type)
admin.site.register(Write)
admin.site.register(Year)
