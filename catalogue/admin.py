from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

from models import CatalogueItem, TopicArea, Profile, JobType, Level


class CatalogueItemAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "topic_area", "discovered_by"]

    class Meta:
        model = CatalogueItem

admin.site.register(CatalogueItem, CatalogueItemAdmin)


class LevelAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "active"]

    class Meta:
        model = Level

admin.site.register(Level, LevelAdmin)


class TopicAreaAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "curator", "active"]

    class Meta:
        model = TopicArea

admin.site.register(TopicArea, TopicAreaAdmin)


class JobTypeAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "active"]

    class Meta:
        model = JobType

admin.site.register(JobType, JobTypeAdmin)


# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton to display profile detail in ADMIN panel
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
