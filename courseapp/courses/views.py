from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

data = {
    "urunler": "urunler kategorisine ait urunler",
    "hakkinda": "hakkinda kategorisine ait urunler"
}

def home(request):
    return HttpResponse('anasayfa')

def kurslar(request):
    return HttpResponse('<h1>Kurslar</h1>')

def urunler(request):
    return HttpResponse('urunler')

def hakkında(request, kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")

def getCoursesByCategory(request, category):
    try:
        category_text = data.get(category, "Kategori bulunamadı")
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")

def getCoursesByCategoryId(request, category_id):
    # 1-2-3 =>
    category_list = list(data.keys())
    if(category_id > len(category_listt)):
        return HttpResponseNotFound("yanlış kategori seçimi")
    redirect_text = category_list[category_id]
    return redirect('/kurs/kategori/urunler')
