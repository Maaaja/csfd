from django.shortcuts import render
from . forms import UvodniForm
from  . models import Filmy, Tvurci,Idecka
from django.views.generic import ListView

# Create your views here.

def index(request):
    # okynko s vyhledavanim
    if request.method == 'POST':
        form = UvodniForm(request.POST)
        if form.is_valid():
            retezec = form.cleaned_data['form']
            filmy = Filmy.objects.filter(nazev__contains=retezec)
            herci = Tvurci.objects.filter(jmeno__contains=retezec)
            #__import__("ipdb").set_trace()
            return render(request, 'vysledek.html', {'filmy': filmy, 'herci': herci, 'form': form})
            

    else:
        form = UvodniForm()

    return render(request, 'home.html', {'form': form})

class FilmyList(ListView):
    model = Filmy





    # def get_name(request):
    # if request.method == 'POST':
    #     # uzivatel submtitol form
    #     form = NameForm(request.POST)
    #     if form.is_valid():
    #         hodnota = form.cleaned_data['your_name']
    #         Komentar.objects.create(komentar = hodnota, datum = timezone.now())

    #         return render(request, 'name.html', {'form_sablona': form, 'hodnota': hodnota, 'komentare': Komentar.objects.all()})
    #     else:
    #         return render(request, 'name.html', {'form_sablona': form, 'komentare': Komentar.objects.all()})
    # else:
    #     # uzivatel iba dosiel na stranku
    #     form = NameForm()
    #     return render(
    #         request, 
    #         'name.html', 
    #         {
    #             'form_sablona': form, 
    #             'komentare': Komentar.objects.all()
    #         })
