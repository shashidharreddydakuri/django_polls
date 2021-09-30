from django.contrib import admin

from .models import Choice, Post, Question, Publication, Article, OpticalTypeFlag, OpticalTypes, Kelvin


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')

class OpticalTypeFlagInline(admin.TabularInline):
    model = OpticalTypeFlag
    

class OpticalType(admin.ModelAdmin):
    fields = ('name', 'title')
    inlines = [OpticalTypeFlagInline]

class PostInline(admin.TabularInline):
    model = Post
    extra = 3 

# class KelvinAdmin(admin.ModelAdmin):
#     # fields = ('name', 'title')
#     inlines = [PostInline]
    
# class Project(admin.ModelAdmin):
#     fields = ('title')



admin.site.register(Question, QuestionAdmin)

admin.site.register(Post)

admin.site.register(Kelvin)

admin.site.register(Publication)

admin.site.register(Article)

admin.site.register(OpticalTypeFlag)

admin.site.register(OpticalTypes)

# admin.site.register(project)