from django.contrib import admin
from entries.models import Blog, Author, Entry


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'nationality')
    search_fields = ('id', 'name')


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'headline', 'number_comments', 'scoring')
    list_filter = ('blog',)
    actions = ['reset_scoring']

    def reset_scoring(self, request, queryset):
        rows_updated = queryset.update(scoring=0)
        self.message_user(request, '{} entry score(s) reset.'.format(rows_updated))
