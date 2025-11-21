from django.db import models

class Ogrenci(models.Model):
    KULUP_SECENEKLERI = [
        ('Yapay Zeka', 'Yapay Zeka Kulübü'),
        ('Robotik', 'Robotik ve Mekatronik'),
        ('Yabancı Dil', 'Yabancı Dil'),
        ('Gemi Bağları', 'Gemi Bağları'),
        ('Gemi Model', 'Gemi Maket Modelciliği'),
        ('Satranç', 'Satranç'),
        ('El Sanatları', 'El Sanatları'),
        ('Müzik', 'Müzik'),
        ('Fotoğrafçılık', 'Fotoğrafçılık'),
    ]

    ogrenci_no = models.CharField(max_length=20, unique=True, verbose_name="Öğrenci No")
    isim = models.CharField(max_length=50, verbose_name="İsim")
    soyisim = models.CharField(max_length=50, verbose_name="Soyisim")

    # Sorular (Her kategori için 2 soru)
    tekno_s1 = models.IntegerField(verbose_name="Kodlama/Yazılım İlgisi (1-5)")
    tekno_s2 = models.IntegerField(verbose_name="Robotik/Mekanik İlgisi (1-5)")

    el_s1 = models.IntegerField(verbose_name="İnce İşçilik/Maket İlgisi (1-5)")
    el_s2 = models.IntegerField(verbose_name="Düğüm/El Sanatları İlgisi (1-5)")

    dil_s1 = models.IntegerField(verbose_name="Yabancı Dil Öğrenme İsteği (1-5)")
    dil_s2 = models.IntegerField(verbose_name="Farklı Kültürlere Merak (1-5)")

    strat_s1 = models.IntegerField(verbose_name="Zeka Oyunları İlgisi (1-5)")
    strat_s2 = models.IntegerField(verbose_name="Planlama/Analiz Yeteneği (1-5)")

    sanat_s1 = models.IntegerField(verbose_name="Müzik/Enstrüman İlgisi (1-5)")
    sanat_s2 = models.IntegerField(verbose_name="Görsel Sanatlar/Fotoğraf İlgisi (1-5)")

    sertifika = models.FileField(upload_to='belgeler/', blank=True, null=True, verbose_name="Sertifika")

    tahmin_edilen_kulup = models.CharField(max_length=50, blank=True, choices=KULUP_SECENEKLERI)
    kayit_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ogrenci_no} - {self.isim} {self.soyisim}"