from django.contrib import admin

# from polls.models import QuestionModel

# from .models import Choice, Lens, Manufacturer, Material, Post, Question, Publication, Article, OpticalTypeFlag, OpticalTypes, Kelvin, Project

from polls.models.QuestionModel import Question
from polls.models.ChoiceModel import Choice
from polls.models.PublicationModel import Publication
from polls.models.ArticleModel import Article
from polls.models.KelvinModel import Kelvin
from polls.models.PostModel import Post
from polls.models.OpticalTypeFlagModel import OpticalTypeFlag
from polls.models.OpticalTypesModel import OpticalTypes
from polls.models.ProjectModel import Project
from polls.models.ManufacturerModel import Manufacturer
from polls.models.MaterialModel import Material
from polls.models.LensModel import Lens
from polls.models.BrandsModel import Brand
from polls.models.CurveModel import BaseCurve, DIACurve
from polls.models.BlogModel import Blog

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
    fields = ('title')
    inlines = [OpticalTypeFlagInline]

class PostInline(admin.TabularInline):
    model = Post
    extra = 3 

# class KelvinAdmin(admin.ModelAdmin):
#     # fields = ('name', 'title')
#     inlines = [PostInline]
    
# class Project(admin.ModelAdmin):
#     fields = ('title')

class ProjectInline(admin.TabularInline):
    model = Project

class ManufacturerInline(admin.TabularInline):
    model = Manufacturer

class LensAdmin(admin.ModelAdmin):
    fields = ('title', 'manufacturer', 'project', 'material')
    # readonly_fields = ("created", "updated")
    # inlines = [ProjectInline, ManufacturerInline]


class BaseCurveInline(admin.TabularInline):
    model = BaseCurve
    extra = 3

class DIACurveInline(admin.TabularInline):
    model = DIACurve
    Extra = 3

class BrandAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['created'], 'classes': ['collapse']}),
    ]
    inlines = [BaseCurveInline, DIACurveInline]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)

admin.site.register(Post)

admin.site.register(Kelvin)

admin.site.register(Publication)

admin.site.register(Article)

admin.site.register(OpticalTypeFlag)

admin.site.register(OpticalTypes)

admin.site.register(Project)

admin.site.register(Manufacturer)

admin.site.register(Lens)

admin.site.register(Material)

admin.site.register(Brand, BrandAdmin)