import email
import re
# from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from baidoxe_dangki.forms import PhuongTien_Form
from .forms import Dangky_Form, Dangnhap_Form, PhuongTien_Form, TimKiem_form
from .models import NguoiDung, PhuongTien, LichSuPhuongTien
# Create your views here.
def requiredLogin(arg=None):
    global rqLogin
    rqLogin = arg

def dangnhap(request):
    if request.method == "POST":
        tentaikhoan = request.POST['tentaikhoan']
        matkhau = request.POST['matkhau']
        dnF = Dangnhap_Form(request.POST)
        if dnF.is_valid():
            try:
                nd = NguoiDung.objects.get(tentaikhoan=tentaikhoan, matkhau=matkhau)
                if nd is not None:
                    requiredLogin(True)
                    global ttk 
                    ttk = tentaikhoan
                    if tentaikhoan == "admin":
                        base(tentaikhoan)
                        return redirect('/baidoxe/admin_form/')
                    else:
                        base(tentaikhoan)
                        return redirect('/baidoxe/danhsachphuongtien/')
                    # return HttpResponse("HELO")
            except NguoiDung.DoesNotExist:
                context = {'dnF':dnF, 'error':'Lỗi đăng nhập.Tên tài khoản hoặc mật khẩu không đúng'}
                return render(request, 'baidoxe_dangki/dangnhap.html', context)
    else:
        dnF = Dangnhap_Form()
        return render(request, 'baidoxe_dangki/dangnhap.html',{'dnF':dnF})

def base(ttk):
    if rqLogin:
        print(ttk)
        return redirect('/baidoxe/base/', var = ttk)
    else:
        return redirect('/baidoxe/dangnhap/')

def danhsach_phuongtien(request):
    if rqLogin:
        context = {'danhsach':PhuongTien.objects.all()}
        return render(request,"baidoxe_dangki/danhsach_phuongtien.html",context)
    else:
        return redirect('/baidoxe/dangnhap/')

def danhsach_lichsu(request):
    if rqLogin:
        context = {'danhsach':LichSuPhuongTien.objects.all(), 'ttk':ttk}
        return render(request,"baidoxe_dangki/danhsach_lichsu.html",context)
    else:
        return redirect('/baidoxe/dangnhap/')

def phuongtien_form(request, id=0):
    if rqLogin:
        if request.method == 'GET':
            if id==0:
                context = {'form':PhuongTien_Form(), 'ttk':ttk}
            else:
                phuongtien = PhuongTien.objects.get(pk=id)
                context = {'form':PhuongTien_Form(instance=phuongtien), 'ttk':ttk}
            return render(request,"baidoxe_dangki/phuongtien_form.html",context)  
        else:
            if id == 0:
                form = PhuongTien_Form(request.POST)
            else:    
                phuongtien = PhuongTien.objects.get(pk=id)
                form = PhuongTien_Form(request.POST,instance = phuongtien)
            if form.is_valid():
                form.save()
            return redirect('/baidoxe/danhsachphuongtien/')
    else:
        return redirect('/baidoxe/dangnhap/')

def admin_form(request):
    if rqLogin:
        context = {'danhsach':PhuongTien.objects.all()}
        return render(request,"baidoxe_dangki/admin_form.html",context)
    else:
        return redirect('/baidoxe/dangnhap/')

def ds_nguoidung(request):
    if rqLogin:
        context = {'ds_nguoidung':NguoiDung.objects.all()}
        return render(request, "baidoxe_dangki/danhsach_nguoidung.html", context)
    else:
        return redirect('/baidoxe/dangnhap/')

def xoa_nguoidung(request, id):
    if rqLogin:
        nguoidung = NguoiDung.objects.get(pk = id)
        nguoidung.delete()
        return redirect('/baidoxe/danhsach_nguoidung/')
    else:
        return redirect('/baidoxe/dangnhap/')

def lichsu_phuongtien(request,id):
    phuongtien = PhuongTien.objects.get(pk=id)
    phuongtien.delete()
    phuongtienlichsu = LichSuPhuongTien()
    phuongtienlichsu.bienso = phuongtien.bienso
    phuongtienlichsu.tenphuongtien = phuongtien.tenphuongtien
    phuongtienlichsu.chusohuu = phuongtien.chusohuu
    phuongtienlichsu.thoigian = phuongtien.thoigian
    phuongtienlichsu.loaiphuongtien = phuongtien.loaiphuongtien
    phuongtienlichsu.save()
    return redirect('/baidoxe/danhsachphuongtien/')

def dangxuat(request):
    requiredLogin(False)
    return redirect('/baidoxe/dangnhap/')

def dangky(request):
    if request.method=="POST":
        dkF = Dangky_Form(request.POST)
        if dkF.is_valid():
            tentaikhoan = dkF.cleaned_data['tentaikhoan']
            tennguoidung = dkF.cleaned_data['tennguoidung']
            matkhau = dkF.cleaned_data['matkhau']
            nhaplaimatkhau = dkF.cleaned_data['nhaplaimatkhau']
            email = dkF.cleaned_data['email']
            # print(nd1)         
            if matkhau == nhaplaimatkhau:
                # nd = NguoiDung.objects.get(tentaikhoan = tentaikhoan)
                try:
                    NguoiDung.objects.get(tentaikhoan = tentaikhoan)
                    context = {'dkF':dkF, 'error':'Tên tài khoản đã tồn tại! Vui lòng chọn tên khác'}
                    return render(request, 'baidoxe_dangki/dangky.html', context)
                except NguoiDung.DoesNotExist:
                    luuND = NguoiDung(tentaikhoan = tentaikhoan, tennguoidung = tennguoidung,
                    matkhau = matkhau, email = email)
                    luuND.save()
                    # return HttpResponseRedirect('dangnhap/')
                    dnF = Dangnhap_Form(initial={'tentaikhoan':tentaikhoan})
                    # dnF = Dangnhap_Form()
                    # return render(request, 'baidoxe_dangki/dangnhap.html', {'dnF':dnF})
                    return redirect('/baidoxe/dangnhap/')
            else:
                context = {'dkF':dkF,'error':'Mật khẩu không khớp! Vui lòng nhập lại'}
                return render(request, 'baidoxe_dangki/dangky.html', context)
    else:
        dkF = Dangky_Form()
        return render(request, 'baidoxe_dangki/dangky.html',{'dkF':dkF})

def timkiemlichsu(request):
    if request.method == "POST":
        thongtinnhapvao = request.POST['thongtinnhapvao']
        luachon = request.POST['luachon']
        if luachon == "Biển số":
            context = {'danhsach':LichSuPhuongTien.objects.filter(bienso__icontains=thongtinnhapvao)}
        elif luachon == "Tên phương tiện":
            context = {'danhsach':LichSuPhuongTien.objects.filter(tenphuongtien__icontains=thongtinnhapvao)}
        
        return render(request, 'baidoxe_dangki/ketqua_timkiem.html',context)
    else:
        form = TimKiem_form()
        return render(request,"baidoxe_dangki/timkiem_form.html",{'form':form}) 

def xoa_lichsu(request,id):
    phuongtienlichsu = LichSuPhuongTien.objects.get(pk=id)
    phuongtienlichsu.delete()
    return redirect('/baidoxe/danhsachlichsu/')
