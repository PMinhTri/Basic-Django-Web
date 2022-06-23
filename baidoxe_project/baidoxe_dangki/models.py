from django.db import models
from django.utils import timezone, dateformat

# Create your models here.
class LoaiPhuongTien(models.Model):
    loaiphuongtien  = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.loaiphuongtien

class PhuongTien(models.Model):
    bienso          = models.CharField(max_length=20)
    tenphuongtien   = models.CharField(max_length=50)
    chusohuu        = models.CharField(max_length=100)
    thoigian        = models.DateTimeField(auto_now_add=True)
    loaiphuongtien  = models.ForeignKey(LoaiPhuongTien,on_delete=models.CASCADE)

class LichSuPhuongTien(models.Model):
    bienso          = models.CharField(max_length=20)
    tenphuongtien   = models.CharField(max_length=50)
    chusohuu        = models.CharField(max_length=100)
    thoigian        = models.DateTimeField()
    loaiphuongtien  = models.CharField(max_length=50)
    thoigianra        = models.DateTimeField(auto_now_add=True)

class NguoiDung(models.Model):
    tentaikhoan     = models.CharField(max_length=100)
    tennguoidung    = models.CharField(max_length=100)
    matkhau         = models.CharField(max_length=50)
    email           = models.EmailField()