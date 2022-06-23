from cProfile import label
from dataclasses import field
import email
from pyexpat import model
from django import forms
from matplotlib import widgets
from .models import NguoiDung, PhuongTien
class PhuongTien_Form(forms.ModelForm):
    
    class Meta:
        model = PhuongTien
        fields = ('chusohuu','tenphuongtien','bienso','loaiphuongtien')
        labels = {
            'bienso': 'Biển số xe',
            'chusohuu': 'Chủ sở hữu',
            'loaiphuongtien': 'Loại phương tiện',
            'tenphuongtien': 'Tên phương tiện'
        }
    def  __init__(self, *args, **kwargs):
        super(PhuongTien_Form,self).__init__(*args, **kwargs)
        self.fields['loaiphuongtien'].empty_label = "Lựa chọn"

class TimKiem_form(forms.Form):
    thongtinnhapvao = forms.CharField(max_length=100, label='Nhập vào thông tin')
    CHOICES=[('Biển số','Biển số'),
         ('Tên phương tiện','Tên phương tiện')]
    luachon = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Lựa chọn")

class Dangky_Form(forms.Form):
    tentaikhoan = forms.CharField(max_length=100, label='Tên tài khoản')
    tennguoidung = forms.CharField(max_length=100, label='Tên người dùng')
    matkhau = forms.CharField(max_length=100, widget=forms.PasswordInput(), label='Mật khẩu')
    nhaplaimatkhau = forms.CharField(max_length=100, widget=forms.PasswordInput(), label='Nhập lại mật khẩu')
    email = forms.CharField(max_length=100, label='Email')

class Dangnhap_Form(forms.Form):
    tentaikhoan = forms.CharField(max_length=100, label='Tên tài khoản')
    matkhau  = forms.CharField(max_length=100, widget= forms.PasswordInput(), label='Mật khẩu')