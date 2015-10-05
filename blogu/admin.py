from django.contrib import admin
from blogu.models import Category,Blog,Comment,UserProfile,Follow

class BlogAdmin (admin.ModelAdmin):
    list_display = ('title','category','written_by','likes','slug')
    prepopulated_fields = { 'slug':('title',)}
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','likes','slug')
    prepopulated_fields = { 'slug':('name',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment)
admin.site.register(Blog,BlogAdmin)
admin.site.register(UserProfile)
admin.site.register(Follow)
# Register your models here.
