from django.core.management.base import BaseCommand
import requests
from xextract import String, Group, Url, Prefix
from csfd.models import Filmy, Tvurci, Idecka
import re



class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(
            'https://www.csfd.cz/zebricky/nejlepsi-filmy/?show=complete',
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'})
        response.raise_for_status()
        # if response.status_code != 200:
        #     return

        def clean_year(s):
            return s.strip("()")
            


        tabulka = Group(xpath='.//tr', children=[
            String(name='nazev', css='.film a', quant='?'),
            String(name='rok', css='span', quant='?', callback=clean_year),
            Url(name='url', css='.film a', quant='?'),
            String(name='hodnoceni', css='td.average', quant='?')
        ]).parse(response.text, url='https://www.csfd.cz/')

        for film in tabulka:
            if film['nazev']:
                Filmy.objects.create(**film)     

        seznam_url = []
        n = 0
        for i in tabulka:
            if tabulka[n]['url']:
                seznam_url.append(tabulka[n]['url'])
            n+=1

        
        id_filmu = []
        
        for url in seznam_url:
            response = requests.get(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'})
            #response.raise_for_status()
            cislo_filmu = re.match(r'https:\/\/www\.csfd\.cz\/film\/(?P<id_filmu>\d+)-',url)
            id_filmu = cislo_filmu.group('id_filmu')
            
            tvurci = Prefix(css='.creators', children=(  
                String(name='jmeno', css='a'),
                Url(name='id_tvurce', css='a'),
            )).parse(response.text)

            
            for jmeno, id_tvurce in zip(tvurci['jmeno'], tvurci['id_tvurce']):
                if id_tvurce.startswith('/tvurce/'):
                #__import__('ipdb').set_trace()
                    Tvurci.objects.get_or_create(jmeno=jmeno, id_tvurce=id_tvurce)
                    Idecka.objects.get_or_create(id_tvurce=id_tvurce, id_filmu=id_filmu)

            
        


        



# from pprint import pprint
# pprint(Group(css='#results table.content tr', quant=302, children=[
#     String(name='nazov_filmu', css='td.film > a', quant='?'),
#     String(name='rok', css='td.film > span.film-year', quant='?', callback=clean_year),
# ])(response.text))