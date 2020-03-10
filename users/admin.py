
#* Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#* Models
from users.models import Profile
from django.contrib.auth.models import User

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('pk','user', 'phone_number', 'website', 'picture', 'modified_at')
    list_display_links = ('pk', 'user')
    list_editable = ( 'phone_number', 'website', 'picture' )
    list_filter = ('create_at', 'modified_at')

    search_fields = ('user__email', 'user__username', 'user__last_name', 'website', 'phone_number')

    fieldsets = (
        ('Profile', {
            "fields": (
                ('picture','user'),
                ('phone_number', 'website'),
            ),
        }),
        ('Extra Info', {
            "fields": (
                'biography',
                ('create_at', 'modified_at')
            )
        })
    )
    readonly_fields = ('create_at', 'modified_at')


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.register(User, UserAdmin)

# Register your models here.
