# **MURHA KARTANOSSA**

Tekijä: Eino Ojala

# **Pelin idea**

Murha kartanossa on tekstipohjainen murhamysteeripeli, jossa pelaaja toimii tutkijana, joka yrittää selvittää 
Kiven kartanossa tapahtuneen murhan. Kartanossa on useita huoneita, epäiltyjä, esineitä ja vihjeitä, joiden avulla 
pelaaja voi selvittää tapahtumien kulun. Pelissä tutkitaan huoneita, etsitään vihjeitä ja yritetään niiden avulla selvittää kartanon tapahtumat.

# **Pelin tavoite**

Pelaajan tavoitteena on selvittää, kuka murhasi Albert Kiven. Pelaajan täytyy tutkia kartanon huoneita,
löytää vihjeitä, kerätä esineitä ja tutkia epäiltyjä.

Pelin lopussa pelaajan täytyy ratkaista Albertin tietokoneen PIN-koodi. Oikealla PIN-koodilla tietokoneesta löytyy salainen viesti, josta saa lisää tietoa murhaajan selvittämiseen. Tämän jälkeen pelaaja voi tehdä lopullisen arvauksen murhaajasta.

Jos pelaaja syöttää väärän PIN-koodin kaksi kertaa tai syyttää väärää henkilöä, peli epäonnistuu ja pelaaja voi aloittaa uuden pelin tai lopettaa pelin.

# **Kestävän kehityksen näkökulma**

Pelissä on mukana YK:n kestävän kehityksen tavoite 7, edullista ja puhdasta energiaa. Tämä liittyy suoraan 
pelin tarinaan, koska murhan uhri Albert Kivi työskenteli uusiutuvan energian ja aurinkopaneelien parissa.

Pelin vihjeissä käsitellään esimerkiksi aurinkopaneelien tehoa ja sitä, miten niiden toimintaa voidaan parantaa. Pelaaja tarvitsee näitä tietoja PIN-koodin ratkaisemiseen. Kestävä kehitys liittyy siis suoraan pelin tarinaan ja mysteerin ratkaisemiseen eikä ole vain erillinen teema pelissä.

Pelin kautta pelaaja saa myös tietoa uusiutuvasta energiasta ja aurinkoenergian hyödyntämisestä.

# **Toiminnallisuudet**

Pelaaja voi liikkua eri huoneissa ja tutkia huoneita tarkemmin. Huoneista voi löytyä esineitä ja vihjeitä, joita voidaan 
käyttää myöhemmin murhan ratkaisemiseen. Pelaajan inventaario pitää kirjaa kerätyistä esineistä ja vihjelista löydetyistä 
vihjeistä.

Pelissä on useita tapoja löytää vihjeitä. Pelaaja voi itse päättää, missä järjestyksessä hän tutkii huoneita, esineitä ja epäiltyjä. Vihjeitä voi siis löytää eri järjestyksessä, mutta kaikkien tapojen lopuksi pelaajan täytyy ratkaista PIN-koodi. Oikean PIN-koodin jälkeen pelaaja saa salaisen viestin ja voi tehdä lopullisen arvauksen murhaajasta.

Peli on jaettu useaan Python-tiedostoon, joista jokaisella on oma tehtävänsä:

# **paavalikko.py**

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

- **tutki_huonetta(pelaaja, otsikko)** antaa pelaajalle mahdollisuuden valita tutkittavan huoneen. Pelaaja parametri on nylyinen pelaajaolio, jonka sijainti päivitetään valitun huoneen mukaan. otsikko-parametri määrittää, mikä otsikko näytetään huoneiden valintavalikossa. Funktio kutsuu myös Huone-luokan **tutki_tarkemmin_huone** metodia, jos pelaaja haluaa tutkia huonetta tarkemmin.

- **keraa_esineita(pelaaja)** antaa pelaajalle mahdollisuuden kerätä huoneissa olevia esineitä. Pelaaja parametri on nykyinen pelaajaolio, jonka inventaarioon kerätty esine lisätään.

- **nayta_epaillyt(pelaaja)** näyttää kaikki pelin epäillyt ja antaa pelaajan tutkia niitä. Pelaaja parametri on nykyinen pelaajaolio, jonka tietoihin tutkitut epäillyt tallennetaan.

- **nayta_ohjeet()** lukee data-kansiossa olevan tarina_ohjeet.txt-tiedoston ja näyttää pelaajalle pelin tarinan ja ohjeet kappaleittain. Pelaaja siirtyy seuraavaan kappaleeseen enterillä.

- **nayta_tapahtumat()** näyttää pelin tapahtuma-ajat.

- **paavalikko(pelaaja)** toimii pelin keskeisenä valikkona. Se kutsuu muita funktioita ja Pelaajaluokan metodeja pelaajan valintojen perusteella. Esimerkiksi huoneiden tutkimiseen kutsutaan **tutki_huonetta(pelaaja)** funktiota ja inventaarion näyttämiseen **pelaaja.nayta_inventaario()** metodia. Pelaaja parametri on nykyinen pelaajaoliota, jonka tietoja päävalikon eri toiminnot käyttävät ja päivittävät.

- Päävalikossa tarkistetaan myös **pelaaja.pin_ratkaistu** ominaisuuden avulla, onko PIN-koodi ratkaistu ennen kuin pelaaja voi yrittää ratkaista murhaajaa.

- **paavalikko(pelaaja)** palauttaa arvon **False**, **True**, **None** tai **"uusi"** sen mukaan, miten pelin kulku jatkuu. Jos tutkinta epäonnistuu väärän PIN-koodin tai väärän syytöksen vuoksi, funktio palauttaa **Falsen** main.py:lle. Tällöin **main()** siirtyy tutkinnan epäonnistumisen käsittelyyn, jossa pelaaja voi aloittaa uuden pelin tai lopettaa pelin. Jos pelaaja ratkaisee murhaajan oikein ja valitsee pelin lopettamisen, funktio palauttaa **Truen**. Jos pelaaja valitsee päävalikosta 12. Lopeta, funktio palauttaa **Nonen**. Jos pelaaja ratkaisee murhaajan oikein ja valitsee pelaamisen uudestaan, funktio palauttaa **"uusi"**, jolloin main() aloittaa uuden pelin.

# **main.py**

- main.py sisältää pelin käynnistämisen ja pelin pääsilmukan.

- **uusi_pelaaja()** kysyy pelaajan nimen ja iän, luo uuden Pelaajaolion ja palauttaa sen. Samalla huoneiden esineet palautetaan alkuperäiseen tilaansa.

- **pelin_valinta()** antaa pelaajalle mahdollisuuden jatkaa tallennettua peliä tai aloittaa uusi peli. Jos tallennustiedosto sattuu olemaan virheellinen, se poistetaan ja aloitetaan uusi peli.

- **tutkinta_epaonnistui()** käsittelee tilanteen, jossa tutkinta epäonnistuu. Pelaaja voi aloittaa uuden pelin tai lopettaa pelin.

- **main()** käynnistää pelin ja hallitsee pelin pääsilmukkaa. Se käsittelee **paavalikko(pelaaja)** funktion palauttaman arvon. **False** tarkoittaa, että tutkinta epäonnistui ja pelaajalle näytetään vaihtoehto aloittaa uusi peli tai lopettaa nykyinen peli. **True** tarkoittaa, että pelaaja ratkaisi murhaajan oikein ja päätti lopettaa pelin. **None** tarkoittaa, että pelaaja lopetti pelin päävalikon kautta. **"uusi"** tarkoittaa, että pelaaja haluaa aloittaa uuden pelin. **True** ja **None** päättävät pelin normaalisti, kun taas **False** käynnistää tutkinnan epäonnistumisen käsittelyn.

# **pelaaja.py**

- pelaaja.py sisältää Pelaaja luokan. Se muodostaa pelaajaolion, jonka tiedoissa säilytetään pelaajan nimi, ikä, inventaario, vihjeet, tutkitut huoneet, tutkitut epäillyt, sijainti ja PIN-koodin ratkaisemisen tila.

- **lisaa_esine(self, esine)** lisää esineen pelaajan inventaarioon, jos esine ei ole vielä inventaariossa. Esine-parametri tarkoittaa lisättävää esineoliota. 

- **nayta_inventaario(self)** näyttää pelaajan inventaarion ja antaa pelaajalle mahdollisuuden tutkia inventaariossa olevia esineitä.

- **lisaa_vihje(self, vihje)** lisää uuden vihjeen pelaajan vihjelistaan, jos vihjettä ei ole vielä löydetty.

- **nayta_vihjeet(self)** näyttää kaikki pelaajan löytämät vihjeet.

- **nayta_tutkinnan_tilanne(self)** näyttää tutkinnan etenemisen.

# **huoneet.py**

- huoneet.py sisältää Huone luokan sekä pelin huoneet.

- Jokaisella huoneella on nimi, kuvaus, tarkemman tutkimisen vihje ja huoneessa olevat esineet.

- **tutki_tarkemmin_huone(self, pelaaja)** antaa pelaajalle mahdollisuuden tutkia huoneen tarkemmin. Saman huoneen tarkemman vihjeen voi löytää vain kerran. Pelaaja parametri on nykyinen pelaajaolio, jonka tietoihin löydetty vihje tallennetaan. 

- **nollaa_huoneet()** palauttaa huoneiden esineet alkuperäiseen tilaansa uuden pelin alussa.

# **epaillyt.py**

- epaillyt.py sisältää Epailty luokan ja pelin epäillyt.

- Jokaisella epäillyllä on nimi, ikä, rooli ja motiivi. 

- Epäillyt tallennetaan epaillyt-listaan, josta niitä voidaan käyttää muualla pelissä.

# **esineet.py**

- esineet.py sisältää Esine luokan ja pelissä käytettävät esineet.

- Jokaisella esineellä on nimi, kuvaus ja vihje.

- Esineet tallennetaan esineet-listaan, josta niitä voidaan käyttää muualla pelissä.

- **tutki(self)** näyttää pelaajalle esineen nimen, kuvauksen ja vihjeen.

- Lisäksi tiedostossa on LukittuEsine luokka, joka perii Esine luokan ominaisuudet. Lukitulla esineellä on myös PIN-koodi.

# **mysteerit.py**

- mysteerit.py sisältää pelin murhamysteerin ratkaisemiseen liittyvät funktiot.

- **ratkaise_pin_koodi(pelaaja)** antaa pelaajalle mahdollisuuden ratkaista tietokoneen PIN-koodin. Pelaajalla on kaksi yritystä ja jos molemmat yritykset ovat vääriä, funktio palauttaa **Falsen** paavalikko.py:lle, jolloin tutkinta epäonnistuu. Oikean PIN-koodin jälkeen pelaaja saa tietokoneelta salaisen viestin ja voi tämän jälkeen yrittää ratkaista murhaajaa päävalikon kautta.

- **ratkaise_murhaaja(pelaaja)** antaa pelaajalle mahdollisuuden valita epäillyn ja syyttää häntä murhasta. Jos pelaaja syyttää väärää henkilöä, funktio palauttaa **False** paavalikko.py:lle ja tutkinta epäonnistuu. Jos pelaaja valitsee oikean murhaajan, hän voi joko lopettaa pelin tai aloittaa uuden pelin. Jos pelaaja haluaa lopettaa pelin, funktio palauttaa **Truen**. Jos pelaaja haluaa aloittaa uuden pelin, funktio palauttaa arvon **"uusi"**.

# **tallennus.py**

- **tallenna_peli(pelaaja)** tallentaa pelaajan nimen, iän, sijainnin, inventaarion, löydetyt vihjeet, tutkitut huoneet, tutkitut epäillyt sekä PIN-koodin ratkaisemisen tilan save.json-tiedostoon.

- **lataa_peli()** lukee tallennetut tiedot JSON-tiedostosta ja palauttaa ne takaisin pelaajaolioon. 

- Tallennetut nimet yhdistetään pelin valmiisiin huone-, esine- ja epäilty olioihin, jotta peli voi jatkua oikeista olioista.

# **__init__.py**

- Tekee peli kansiosta Python paketin ja mahdollistaa Pelaaja luokan tuomisen suoraan paketista ilman, että luokkaa tarvitsee tuoda suoraan pelaaja.py tiedostosta

# **data**

- Data-kansiossa sijaitsevat pelin ulkopuoliseen tiedostoon tallennetut tiedot.

- Tarina_ohjeet.txt sisältää pelin tarinan ja ohjeet.

- Tallennuksessa luotu save.json sisältää tallennetun pelin tiedot.

## **Pelin käynnistäminen**

- **Peli käynnistetään **peliprojekti-kansion main.py tiedostosta**.
