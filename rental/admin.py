from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe



from rental.models import RentalPost

# Register your models here.
class RentalPostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "details", "user", "details", "actions_col"]
    search_fields = ["title","user__phone_number"]
    list_display_links = ["actions_col"]
    actions = None
    list_per_page = 7


    def actions_col(self, obj):
        detail_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        delete_url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        # Tạo các nút xem chi tiết và xóa
        detail_button = f'<a href="{detail_url}" class="button">Detail</a>'
        delete_button = f'<a href="{delete_url}" class="button" style="color:red;">Delete</a>'
        # Sử dụng mark_safe để hiển thị HTML an toàn
        return mark_safe(f"{detail_button} {delete_button}")

    # Đặt tiêu đề cho cột action
    actions_col.short_description = 'Actions'


admin.site.register(RentalPost, RentalPostAdmin)

