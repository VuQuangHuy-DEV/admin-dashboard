from django.contrib import admin
from authentication.models import User, UserReview
from django.urls import reverse
from django.utils.safestring import mark_safe

from rental.models import Brand,Vehicle



class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "phone_number", "is_verify", "actions_col"]
    search_fields = ["full_name", "phone_number"]
    list_per_page = 7
    actions = None
    list_display_links = ["actions_col"]

    def actions_col(self, obj):
        # Tạo URL cho trang chi tiết và trang xóa đối tượng
        detail_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        delete_url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])

        detail_button = f'<a href="{detail_url}" class="button">Detail</a>'
        delete_button = f'<a href="{delete_url}" class="button" style="color:red;">Delete</a>'
        return mark_safe(f"{detail_button} {delete_button}")

    actions_col.short_description = 'Actions'



class UserReviewAdmin(admin.ModelAdmin):

    list_display = ["id","user","rating","feedback","actions_col"]
    search_fields = ["id","user__full_name"]
    actions = None
    list_display_links = ["actions_col"]

    def actions_col(self, obj):
        # Tạo URL cho trang chi tiết và trang xóa đối tượng
        detail_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        delete_url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])

        detail_button = f'<a href="{detail_url}" class="button">Detail</a>'
        delete_button = f'<a href="{delete_url}" class="button" style="color:red;">Delete</a>'
        return mark_safe(f"{detail_button} {delete_button}")
    actions_col.short_description = 'Actions'


#custome some title
class CustomAdminSite(admin.AdminSite):
    site_header = 'Manage for Admin'
    site_title = 'Admin page'
    index_title = ''

admin.site = CustomAdminSite(name='customadmin')

admin.site.register(User, UserAdmin)
admin.site.register(UserReview,UserReviewAdmin)



