from django.shortcuts import render

from nhanvien.models import NhanVien

# Create your views here.

def nhanvien(request):
    return render(request,'nhanvien.html')
def trangchu(request):
    return render(request,'trangchu.html')

def them_nhan_vien(request):
    hoten = request.GET.get('hoten')
    chucvu = request.GET.get('chucvu')
    namsinh = request.GET.get('namsinh')
    data = NhanVien(
        ho_ten = hoten,
        chuc_vu = chucvu,
        nam_sinh = namsinh
    )
    data.save()
    return render(request,'nhanvien.html') 