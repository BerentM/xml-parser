"""Program służący do konwersji xmli do csv."""
# -*- coding: utf-8 -*-

import csv
from xml.etree import ElementTree
import os


def odczytaj_xml(sciezka='wniosekkredytowy.xml'):
    """Funkcja odczytująca XMLa."""
    with open('wniosekkredytowy.xml', 'r', encoding='utf-8') as f:
        zawartosc_xml = ElementTree.parse(f)
        return zawartosc_xml


def zapisz_csv(xml, nazwa_pliku='wniosek', sciezka='./'):
    """Zapisywanie pliku csv."""
    adres_csv = sciezka+nazwa_pliku+'.csv'

    def sprawdz_csv(adr=adres_csv):
        if os.path.exists(adres_csv):
            liczba_bledow = 0
            opcja_csv = input('PLIK JUŻ ISTNIEJE!\n1.Zastąp istniejący\
                               \n2.Dopisz do pliku\n3.Zakończ działanie\n')
            while opcja_csv not in ['1', '2', '3']:
                if 3-liczba_bledow == 1:
                    print('\nWybrano nieodpowiednią opcję. Spróbuj ponownie. \
                            \nOstatnia próba.')
                else:
                    print('\nWybrano nieodpowiednią opcję. Spróbuj ponownie. \
                            \nPozostały '+str(3-liczba_bledow)+' próby.')
                opcja_csv = input()
                liczba_bledow += 1
                if liczba_bledow == 3:
                    opcja_csv = 'q'
                    break
        else:
            opcja_csv = '1'
            print('brak pliku, zamien')
        return opcja_csv.replace('1', 'w').replace('2', 'a').replace('3', 'q')

    typ_zapisu = sprawdz_csv()
    if typ_zapisu in (['w', 'a']):
        with open(adres_csv, mode=typ_zapisu) as plik:
            '''tworzenie czystego pliku csv'''
            wniosek_writer = csv.writer(plik, delimiter=';', quotechar='"',
                                        quoting=csv.QUOTE_MINIMAL,
                                        lineterminator="\n")
            wniosek_writer.writerow(['tag', 'text', 'attrib'])  # nagłówki
            for node in xml.iter():
                '''uzupelnianie csv'''
                print([node.tag, node.text, node.attrib])
                wniosek_writer.writerow([node.tag, node.text, node.attrib])
        os.system('cls')
        os.system('clear')
        print('Zapis zakończył się sukcesem!')
    else:
        os.system('cls')
        os.system('clear')
        print('Zakończono działanie programu.')


xml = odczytaj_xml()
zapisz_csv(xml)
