from django.contrib import admin
from nhanvien.models import NhanVien

# Register your models here.
class NhanVienAdmin(admin.ModelAdmin):
    list_display = ('ho_ten','chuc_vu', 'nam_sinh')
    list_display_links = ('ho_ten','chuc_vu', 'nam_sinh')
    list_filter = ('ho_ten','chuc_vu', 'nam_sinh')
    search_fields = ('ho_ten','chuc_vu', 'nam_sinh')
    list_per_page = 20

admin.site.register(NhanVien, NhanVienAdmin)