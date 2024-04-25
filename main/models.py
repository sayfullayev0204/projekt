from django.db import models

class Tuman(models.Model):
    Nomi = models.CharField(max_length=300)
    Masul = models.CharField(max_length=300)
    def __str__(self):
        return self.Nomi

class Maktab(models.Model):
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    Nomi = models.CharField(max_length=300)
    Masul = models.CharField(max_length=300)
    def __str__(self):
        return self.Nomi
    
class Shaxs(models.Model):
    Ismi = models.CharField(max_length=300)
    Familyasi = models.CharField(max_length=300)
    Sharfi = models.CharField(max_length=300)
    viloyats = {
        ('Qashqadaryo', 'Qashqadaryo'),
        ('Samarqand', 'Samarqand'),
        ('Navoiy', 'Navoiy'),
        ('Buxoro', 'Buxoro')
    }
    viloyat = models.CharField(max_length=300,verbose_name='viloyat', choices=viloyats)
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
    maktab = models.ForeignKey(Maktab, on_delete=models.CASCADE)
    maxallasi = models.TextField()
    JSHSHIR = models.IntegerField()
    Telefon_raqam = models.CharField(max_length=30)
    til = {
        ('UZBEK', 'uzbek'),
        ('RUS', 'rus'),
        ('NEMIS', 'nemis'),
        ('ENGLISH', 'ingliz')
    }
    Biladigan_tili = models.CharField(max_length=30, verbose_name='til', choices=til)
    daraja = {
        ('A1 daraja','A1 daraja'),
        ('A2 daraja','A2 daraja'),
        ('B1 daraja','B1 daraja'),
        ('B2 daraja','B2 daraja'),
        ('C1 daraja','C1 daraja')
    }
    Til_bilish_darajasi = models.CharField(max_length=30, verbose_name='daraja', choices=daraja)
    holat = {
        ('Ayni vaqtda o\'qimoqda','Ayni vaqtda o\'qimoqda'),
        ('O\'qib bo\'lgan','O\'qib bo\'lgan'),
        ('Sertifikati bor', 'Sertifikati bor')
    }
    Holati = models.CharField(max_length=30, verbose_name='holat', choices=holat)
    def __str__(self):
        return self.Ismi