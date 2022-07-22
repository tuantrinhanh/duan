from multiprocessing import context
from django.shortcuts import get_object_or_404, render

from dangky.models import NguoiDung

# Create your views here.
def dangnhap(request):
    return render(request,'dangnhap.html')

def xuly_dangnhap(request):
    ten = request.GET.get('ten')
    mk = request.GET.get('matkhau')
  
    thongtin = NguoiDung.objects.filter(ten_dang_nhap = ten, mat_khau = mk)
    danh_sach = NguoiDung.objects.all()
    context = {
        'ds_nguoidung':danh_sach,
    }
    if thongtin.exists():
        return render(request, 'thanhcong.html', context)
    else:
        return render(request, 'thatbai.html')

def chi_tiet(request, nguoidung_id):
    user = get_object_or_404(NguoiDung, pk = nguoidung_id)
    context = {
        'nd':user,
    }   
    return render(request, 'chitiet.html', context)

def xuly_capnhat(request):
    id_nguoidung = request.GET.get('id_nguoidung')
    ten = request.GET.get('ten')
    mail = request.GET.get('mail')
    mk = request.GET.get('matkhau')

    NguoiDung.objects.filter(id=id_nguoidung).update(
        ten_dang_nhap = ten,
        email = mail,
        mat_khau = mk
    )
    # thongtin = NguoiDung.objects.filter(ten_dang_nhap = ten, mat_khau = mk)
    danh_sach = NguoiDung.objects.all()
    context = {
        'ds_nguoidung':danh_sach,
    }
    return render(request, 'thanhcong.html', context)

def xoa_nguoidung(request, nguoidung_id):
    dulieu = get_object_or_404(NguoiDung,pk = nguoidung_id)
    try:
        dulieu.delete()
    except:
        print("Xóa bị lỗi")
    danh_sach = NguoiDung.objects.all()
    context = {
        'ds_nguoidung':danh_sach,
    }
    return render(request, 'thanhcong.html', context)