from django.urls import path, include
from django.views import View
from . import views
urlpatterns = [
    # path('base/', views.base, name='base'),
    path('dangnhap/', views.dangnhap, name='dangnhap'),
    path('dangky/', views.dangky, name='dangky'),
    path('danhsachphuongtien/',views.danhsach_phuongtien,name="danhsach_phuongtien"),
    path('danhsachlichsu/',views.danhsach_lichsu,name="danhsach_lichsu"),
    path('dangkiphuongtien/<int:id>/', views.phuongtien_form,name="chinhsua_thongtinphuongtien"),
    path('xoa/<int:id>/', views.lichsu_phuongtien,name="xoa_phuongtien"),
    path('xoalichsu/<int:id>/', views.xoa_lichsu,name="xoa_lichsu"),
    path('dangkiphuongtien/', views.phuongtien_form,name="them_phuongtien"),
    path('dangxuat/', views.dangxuat, name='dangxuat'),
    path('timkiemlichsu/',views.timkiemlichsu, name="timkiem_lichsu"),
    path('admin_form/', views.admin_form, name ="admin_form"),
    path('danhsach_nguoidung/', views.ds_nguoidung, name="danhsach_nguoidung"),
    path('xoa_nguoidung/<int:id>/', views.xoa_nguoidung, name="xoa_nguoidung")
]