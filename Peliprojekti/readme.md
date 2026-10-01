# **MURHA KARTANOSSA**

Tekijä: Eino Ojala

# **Pelin idea**

Murha kartanossa on tekstipohjainen murhamysteeripeli, 
jossa pelaaja toimii tutkijana ja yrittää selvittää 
Kiven kartanossa tapahtuneen murhan. 
Kartanossa on useita huoneita, epäiltyjä, esineitä 
ja vihjeitä, joiden avulla pelaaja voi selvittää 
tapahtumien kulun. Peli perustuu tutkimiseen, 
päättelyyn ja erilaisten vihjeiden yhdistämiseen.

# **Pelin tavoite**

Pelaajan tavoitteena on selvittää, 
kuka murhasi Albert Kiven. Pelaajan täytyy tutkia 
kartanon huoneita, löytää vihjeitä, 
kerätä esineitä ja tutkia epäiltyjä.

Pelin lopussa pelaajan täytyy ratkaista Albertin tietokoneen 
PIN-koodi. Oikean PIN-koodin avulla tietokoneesta löytyy 
salainen viesti, joka auttaa murhaajan tunnistamisessa. 
Tämän jälkeen pelaaja voi tehdä lopullisen arvauksen
murhaajasta.

Jos pelaaja syöttää väärän PIN-koodin tai syyttää väärää 
henkilöä, peli alkaa uudelleen.

# **Toiminnallisuudet**

Peli toimii tekstipohjaisen päävalikon kautta. 
Päävalikon toiminnot:
1. Tutki huoneita
2. Kerää esineitä
3. Katso inventaariota
4. Tutki epäiltyjä
5. Tutki vihjeitä
6. Tutki tapahtuma-aikoja
7. Ratkaise PIN-koodi
8. Ratkaise murhaaja
9. Tutkinnan tilanne
10. Ohjeet
11. Tallenna peli
12. Lopeta

Pelaaja voi liikkua eri huoneissa ja tutkia niitä tarkemmin. 
Huoneista voi löytyä esineitä ja vihjeitä, joita voidaan 
käyttää myöhemmin murhan ratkaisemiseen. Pelaajan inventaario 
pitää kirjaa kerätyistä esineistä ja vihjelista löydetyistä 
vihjeistä.

Pelissä on useita erilaisia tapoja löytää vihjeitä. 
Pelaaja voi päättää itse, missä järjestyksessä hän 
tutkii huoneita, esineitä ja epäiltyjä. Vihjeitä voi 
siis löytyä eri järjestyksessä, mutta kaikkien etenemistapojen 
lopussa pelaajan täytyy ratkaista tietokoneen PIN-koodi.
PIN-koodin ratkaisemisen jälkeen pelaaja saa salaisen viestin 
ja voi tehdä lopullisen arvauksen murhaajasta

Pelissä on myös tallennus- ja lataustoiminto. 
Pelaajan nimi, ikä, sijainti, inventaario, löydetyt vihjeet, 
tutkitut huoneet, tutkitut epäillyt sekä PIN-koodin ratkaisemisen tila 
tallennetaan erilliseen tekstitiedostoon. Näin peliä voi jatkaa myöhemmin.

Peli on jaettu useisiin Python-tiedostoihin ja moduuleihin. Pelaajaa, 
huoneita, esineitä ja epäiltyjä käsitellään omissa luokissaan.
Pelin tallennus, PIN-koodin ja murhan ratkaiseminen ja päävalikko on 
toteutettu omissa moduuleissaan. Peli käynnistetään main.py-tiedostosta.

# **Kestävän kehityksen näkökulma**

Pelissä on mukana YK:n kestävän kehityksen tavoite 7, 
Edullista ja puhdasta energiaa. Teema liittyy suoraan 
pelin juoneen, koska murhan uhri Albert Kivi työskenteli 
uusiutuvan energian ja aurinkopaneelien parissa.

Pelin vihjeissä käsitellään esimerkiksi aurinkopaneelien tehoa
ja niiden tehokkuuden paranemista. Pelaaja joutuu käyttämään 
näitä energiaan liittyviä tietoja PIN-koodin ratkaisemisessa. 
Näin kestävän kehityksen teema ei ole vain erillinen osa pelissä,
vaan se on osa pelin tarinaa, vihjeitä ja mysteerin ratkaisemista.

Pelin avulla pelaaja tutustuu uusiutuvaan energiaan ja siihen, 
miten esimerkiksi aurinkoenergian talteenottoa pyritään kehittämään 
entistä tehokkaammaksi.