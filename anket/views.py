from django.shortcuts import render, redirect
from .forms import AnketForm
from .models import Ogrenci
import random

def kulup_hesapla(tekno_p, el_p, dil_p, strat_p, sanat_p):
    puanlar = {
        'teknoloji': tekno_p,
        'el_becerisi': el_p,
        'dil': dil_p,
        'strateji': strat_p,
        'sanat': sanat_p
    }

    max_puan = max(puanlar.values())
    kazananlar = [k for k, v in puanlar.items() if v == max_puan]
    secilen_kategori = random.choice(kazananlar)

    if secilen_kategori == 'teknoloji':
        return random.choice(['Yapay Zeka Kulübü', 'Robotik ve Mekatronik'])
    elif secilen_kategori == 'el_becerisi':
        return random.choice(['Gemi Bağları', 'Gemi Maket Modelciliği', 'El Sanatları'])
    elif secilen_kategori == 'dil':
        return 'Yabancı Dil'
    elif secilen_kategori == 'strateji':
        return 'Satranç'
    else:
        return random.choice(['Müzik', 'Fotoğrafçılık'])

def anket_view(request):
    if request.method == 'POST':
        form = AnketForm(request.POST, request.FILES)
        if form.is_valid():
            ogrenci = form.save(commit=False)

            p_tekno = ogrenci.tekno_s1 + ogrenci.tekno_s2
            p_el = ogrenci.el_s1 + ogrenci.el_s2
            p_dil = ogrenci.dil_s1 + ogrenci.dil_s2
            p_strat = ogrenci.strat_s1 + ogrenci.strat_s2
            p_sanat = ogrenci.sanat_s1 + ogrenci.sanat_s2

            kulup = kulup_hesapla(p_tekno, p_el, p_dil, p_strat, p_sanat)

            ogrenci.tahmin_edilen_kulup = kulup
            ogrenci.save()
            return render(request, 'anket/sonuc.html', {'ogrenci': ogrenci, 'kulup': kulup})
    else:
        form = AnketForm()
    return render(request, 'anket/form.html', {'form': form})

def liste_view(request):
    ogrenciler = Ogrenci.objects.all().order_by('-kayit_tarihi')
    return render(request, 'anket/liste.html', {'ogrenciler': ogrenciler})