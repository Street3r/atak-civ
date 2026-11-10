# ATAK Finnish glossary (sanasto)

Terminology used in `values-fi/strings.xml`. Military terms follow the Finnish Defence Forces (Puolustusvoimat, PV) publications listed in [README.md](README.md#sources). Where PV terminology exists it is preferred over a literal translation. Where two PV sources disagree, the newer one is preferred unless noted.

Source abbreviations:

- **SML** = Sotilasmerkistö ja -lyhenteet 2005
- **TO** = Taistelijan opas 2013
- **JKK** = Johtajan käsikirja 2022
- **JJR** = Jääkärijoukkueen ja -ryhmän käsikirja 2018
- **MSK** = Merisotilaan käsikirja 2010
- **SK** = Suojelutoiminnan käsikirja 2022
- **SuojKK** = Suojaamisen käsikirja 2021
- **SNKK** = Suojanedistämisen käsikirja 2021
- **MTK** = Mittaustoiminnan käsikirja 2015
- **ITKK** = Ilmatorjunnan ampumaopin käsikirja 2017
- **HJKK** = Huoltojoukkueen käsikirja 2017
- **VM** = Viestimies 4/2017
- **AJP** = AJP-01 FI
- **SKK** = Sotilaan käsikirja. Section numbers are given as *2024 / 2026*, because the 2026 edition renumbered the chapters (for example 5.4.1 → 4.4.1).
- **NS** = Nato-sanasto (Valtioneuvosto, 2025 edition)
- **RA** = Ohje R-alueelle lentämisestä (Pääesikunta)
- **TKO** = Talvikoulutusopas 2004
- **TEA** = Taisteluensiapu-opetuspaketti 2019 (Pääesikunta)
- **AO** = Yleinen ase- ja asejärjestelmäopas 2001
- **KT** = Kybertaistelu 2020 (MPKK 2014)
- **KTS** = Kyberturvallisuuden sanasto 2018
- **KOTS** = Kokonaisturvallisuuden sanasto 2017
- **PS** = Pelastusalan sanasto 2026
- **GIS** = Geoinformatiikan sanasto (4th ed.)
- **MS** = Microsoft terminology (fi-FI)
- **–** = general Finnish UI usage (no PV source)

Rows marked *open* are waiting for a decision by the project owner.

## Style

- **Case.** Use sentence case (Finnish does not use Title Case): *Show All* → *Näytä kaikki*.
- **Commands and questions.**
  - Commands use the imperative singular (*Valitse*, *Anna*, *Ota käyttöön*).
  - Questions use the *sinä* form (*Haluatko…?*), as in Android's own Finnish UI.
  - Short yes/no confirmations may use the passive (*Poistetaanko…?*, *Korvataanko…?*).
- **Quotation marks.** Use ”…” (U+201D on both sides, Finnish convention).
  - Exception: where the Java code adds one half of the pair as a straight apostrophe, the string uses `'` too. These strings are `are_you_sure_delete`, `video_text17`, `video_text19`, `video_text20`, `point_dropper_text23`, `iconset_delete` and `mapping_iconset`.
- **Abbreviation inflection.** Abbreviations take a colon: *GPS:n*, *URL:n*, *KML:ää*. *ATAK* inflects as a word: *ATAKin*, *ATAKiin*.
- **Menu paths.** Write them with " > ": *Asetukset > Työkaluasetukset*.
- **Untranslated names.** Product and protocol names are not translated: ATAK, TAK Server, CoT, KML, KMZ, GeoChat, DTED, MISB, KLV, SPI (Sensor Point of Interest).
  - The CIV build's *Digital Pointer (DP)* is *DP-osoitin*; its tool label is *Osoitin (DP)*.
- **Tool names.** Tools are named by what they do, not translated word for word (owner's decision, 2026-11-07). See *Tool names* under *Software / UI*.

## Navigation, coordinates and units

| English | Suomi | Source / note |
|---|---|---|
| Range & Bearing (R&B) | Etäisyys ja suunta | – (follows the tool name). PV reports give the order *suunta ja etäisyys* (SKK 2026); *open* |
| Bearing | Suunta | TO 10 |
| Magnetic bearing | Kompassisuunta | TO 10 |
| Heading (movement) | Kulkusuunta; *Track Up* = kulkusuunta ylös | TO 10 |
| Heading / azimuth (orientation of a drawn shape or model) | Suunta | *Atsimuutti* is not used in PV material; MTK uses *suuntakulma* for the angle |
| True North | Napapohjoinen | TO 10, SKK 5.4.1 / 4.4.1 |
| Magnetic North | Neulapohjoinen | TO 10, SKK 5.4.1 / 4.4.1 |
| Grid North | Karttapohjoinen | TO 10, SKK 5.4.1 / 4.4.1 |
| Zone North | Kaistapohjoinen | SKK 5.4.1 / 4.4.1 (map legend) |
| North reference / North Up | Pohjoisen viitesuunta / pohjoinen ylös | – (MTK: *pohjoissuunnat*) |
| Magnetic correction / true north correction / total correction | Neulaluvun korjaus / napaluvun korjaus / kokonaiskorjaus | SKK 5.4.1 / 4.4.1 (map legend), MTK |
| Declination | Eranto | MSK. On Army maps the same quantity is *neulaluvun korjaus (Nek)* (MTK) |
| Mils | Piirut (6400) | See note below |
| Degrees | Asteet | TO 4 |
| MGRS | MGRS (MGRS-ruudusto); MGRS location = MGRS-sijainti (= ruudustoperusteinen sijainti) | SML IV, TO 10, SKK 5.4.2 / 4.4.2 |
| Grid zone (designator) | Vyöhyke, vyöhyketunnus (34V = kaista 34, lohko V) | SML IV, TO 10, SKK 5.4.2 / 4.4.2 |
| UTM zone | Kaista (kaistatunnus) | SKK 5.4.2 / 4.4.2. The ATAK key `zone` is shared by MGRS and UTM and stays *Vyöhyke* |
| 100 km square | Ruututunnus, 100 km ruutu | SML IV, TO 10, SKK 5.4.2 / 4.4.2 |
| Easting / Northing | Itäkoordinaatti (E) / pohjoiskoordinaatti (N) | TO 10, SKK 5.4.2 / 4.4.2 |
| UTM location (zone + E/N) | Koordinaattiperusteinen sijainti | SKK 5.4.2 / 4.4.2 |
| UTM | UTM-koordinaatisto | SML IV |
| Lat / Lon | Leveysaste / pituusaste | SML IV |
| Grid lines (map grid overlay) | Koordinaattiviivat | TO 10, SKK 4.4.2, SML IV. *Ruudukko* is kept for the user-drawn Grid tool |
| Contour lines: index (major) / regular (minor) | Korkeuskäyrät: johtokäyrät / pääkäyrät | SKK 2026 4.4.1 (map legend), MTK |
| Elevation (terrain) | Korkeus (maaston korkeus) | – |
| Elevation data | Korkeustiedot (values); korkeusaineisto (a data set); korkeusmalli (DTED/DEM) | – |
| Altitude | Korkeus | SML I (field X: korkeus/syvyys) |
| MSL / HAE / AGL | Merenpinnasta (MSL) / ellipsoidikorkeus (HAE) / korkeus maanpinnasta (AGL) | SML I (X), MTK; HAE and AGL: – |
| Slant range | Vinoetäisyys | – |
| Inclination (vertical angle from the observer to the target) | Korkeuskulma | PV and survey usage. *Kaltevuus* is kept for terrain slope |
| Bullseye direction: From Center / To Center | Keskeltä / Keskelle | *Keskuksesta / Keskukseen* does not fit the button |
| Waypoint | Reittipiste | TO 10.4 |
| Checkpoint (route) | Tarkastuspiste | – . *Open.* PV route planning uses *rasti* (TO 2013 and SelvKK 2024: "Jaa reitti rasteiksi noin kilometrin välein"). PV's *tarkastuspiste* / *tarkastuspaikka* is a manned control point (SML, TAKK 2025). *Reittipiste* is taken by *Waypoint* |
| Route; infil / exfil (route direction) | Reitti; meno / paluu | PV *meno- ja paluureitti*. In ATAK infil/exfil is a generic label and every new route defaults to Infil, so *soluttautuminen* (a covert manoeuvre) is not used. *Irtautuminen* stays for Withdraw and the 9-line Egress |
| Route type: primary / secondary / tertiary | Pääreitti / varareitti / 2. varareitti | PV *pää- ja varareitti*. Full words, because the labels also stand alone in the route-type list |
| Resection (tool) | Oman paikan määritys; the classic method is *taaksepäinleikkaus* | SKK 2026 (*oman paikan määrittäminen*); MTK covers only forward intersection |
| Range rings | Etäisyysrenkaat | – |
| Track / breadcrumbs (recorded path); single breadcrumb | Kulkujälki; jälkipiste. Bread Crumb Preferences = *Jälkipisteiden asetukset* (Track History Preferences = *Kulkujälkihistorian asetukset*) | – |
| Track History | Kulkujälkihistoria; tool label *Kulkujäljet* | – |
| Point of Interest | Kiinnostava kohde | – |
| Self / Self marker | Oma sijainti / oma merkki | – |
| Nautical mile (NM) | Meripeninkulma (mpk) | MSK. Map readouts show *NM*, which comes from the code |
| ETA | Arvioitu saapumisaika (ETA); *ETA* in short labels | – |
| GPS / GNSS | GPS; GNSS where the English says GNSS (satelliittipaikannus in running text) | TO 10.4, SKK 5.4.4 / 4.4.4 (*GPS-paikannuslaite*) |
| Laser range finder (LRF) | Laseretäisyysmittari (LRF) | SKK 5.4.4 / 4.4.4 |
| Situational awareness (SA) | Tilannetietoisuus; SA message = SA-viesti | SKK 5.10.1 / 4.10.1 |
| Common operational picture | Tilannekuva | JKK 2.6 |

**Note on mils.** ATAK uses the NATO circle of 6400 mils (`ConversionFactors`, `LRFReader`), so the unit is always labelled *Piirut (6400)*.

- TO 4 gives 6000 mils per circle.
- SKK 2026 still gives 6000 as the basic circle and allows 6400 in some branches, such as artillery.
- PV is moving to the NATO 6400 standard.
- The PV map legend marks the 6000 mil as **v** and the 6400 mil as *mils*.
- The engine also has a 6000-mil unit (`Angle.MIL_WARSAW`), which the UI does not offer.

## Military symbology (MIL-STD-2525 / APP-6)

| English | Suomi | Source |
|---|---|---|
| Tactical symbol / graphic | Taktinen merkki / taktinen kuvio | SML I |
| Frame / icon / fill / modifier (amplifier) | Kehys / kuvake / täyteväri / lisämerkintä | SML I kohta 7 |
| Affiliation (standard identity) | Tunnistetieto | SML I |
| Friendly / Hostile / Neutral / Unknown | Oma / vihollinen / puolueeton / tuntematon | SML I gives both forms, *neutraali, puolueeton* (abbreviation *neu*). *Open:* NS 2025 (5212) defines *neutral* in the identification sense, recommends *neutraali* and rejects *puolueeton* |
| Assumed friend / suspect / pending | Oletettu oma / epäilty / odottaa tunnistusta | – |
| Adversary / Enemy | Vastustaja / vihollinen | NS |
| Exercise / Simulation / Reality (symbol context) | Harjoitus / simulaatio / todellinen | NS (*exercise*) |
| Command and control (C2) / C2 system | Johtaminen / johtamisjärjestelmä | NS |
| Battle dimension / domain | Toimintaympäristö | SML I |
| Warfighting functions (2525D): Movement and Maneuver / Fires / Protection / Sustainment | Liike ja taisteluliike / tulenkäyttö / suojaaminen / huolto | NS (*manoeuvre* = taisteluliike), SuojKK (*suojaaminen*). *Suojaus* is kept for the Cover task |
| Echelon | Johtotaso (joukon koko) | SML I |
| Echelons | Partio/miehistö, ryhmä, puolijoukkue, joukkue/osasto, komppania/patteri/eskadroona, pataljoona, rykmentti/lennosto, prikaati, divisioona, armeijakunta, armeija, armeijaryhmä/rintama, alue/operaatioalue, johtoporras (*Command*) | JJR liite 2.3, HJKK (*puolijoukkue*), NS (*command* as an organisation = johtoporras) |
| Task force | Taisteluosasto | SML I, JJR |
| Coordination Point (2525C) / Coordinating Point (2525D) | Yhteistoimintapiste | The same control measure in both symbol sets |
| Reinforced / Reduced | Vahvennettu / heikennetty | SML I |
| Higher formation | Ylempi johtoporras | SML I, JKK |
| Unique designation | Yksilöivä nimi | SML I |
| Staff comments / Additional information | Esikuntakommentti / lisätieto | SML I |
| Evaluation rating | Arvioinnin luokitus | SML I |
| Direction of movement | Liikesuunta | SML I |
| Feint / dummy / decoy | Harhautus / vale / harhamaali | SML I (AB *vale/harhautus*); decoy: – |
| Installation | Laitos (civilian symbols: toimipiste) | SML I |
| Planned / anticipated | Suunniteltu / ennakoitu | SML I 6 kohta 48, kohta 30 |
| Present | Oleva | SML I 6 kohta 48 |
| Headquarters | Esikunta | SML I |
| Observation post (OP) | Tähystyspaikka | SML I kohta 36 |
| Contact point | Yhteydenottopiste | SML I |
| Start point / release point | Lähtökynnys / tulokynnys | SML I, JJR |
| Traffic control point | Liikenteen ohjauspiste | SML I |
| Objective | Tavoite | SML I |
| Rally point / assembly area | Kokoontumispaikka / kokoontumisalue | SML I |
| Attack position / assault position | Hyökkäysasema / lähtöasema | JJR 7.2: *hyökkäysasema* is the prepared base where the unit waits (under 3 km from the engagement area); *lähtöasema* is close to the engagement area, covered from observation, where the final refinements are made. JJR's order (hyökkäysasema → lähtöasema → tuhoamisalue → tavoite) matches 2525's attack position → assault position → objective |
| Engagement area (EA) | Tuhoamisalue (EA) | JJR |
| Named area of interest (NAI) | Tiedustelun kohdealue (NAI) | – |
| Ambush | Väijytys | JJR 2018 (symbol table and 8.2). SML 2005 has *ylläkkö*; JJR treats *ylläkkö* as a quick form of väijytys |
| Cache | Kätkö | SML I |
| Main supply route (MSR) / supply route / alternate supply route | Päähuoltotie (MSR) / huoltotie / varahuoltotie | SML I kohta 28 (*huoltotiet*) |
| Boundary | Raja, väliraja | SML I |
| Zone of responsibility (ZOR) | Vastuuvyöhyke (ZOR) | – (*vastuualue* is kept for AOR) |
| Sector of fire / maximum range / range fan | Ampumasektori / suurin ampumaetäisyys / kantamasektori | SML I kohta 32; range fan: – |
| Firing position / firing point | Tuliasema / ampumapaikka | SML I kohta 31; firing point: *open* |
| Main / supporting attack | Päähyökkäys / tukihyökkäys | SML I |
| Axis of advance | Hyökkäyksen suuntautuminen; aviation = ilmahyökkäyksen suuntautuminen | SML I 4 e kohta 42 (open arrow) |
| Direction of attack | Tarkka hyökkäysreitti | SML I 4 e kohta 42: the line arrow, usually for a battalion or smaller unit. This keeps *hyökkäyssuunta* for the FAH |
| Principal direction of fire (PDF) | Pääampumasuunta (PDF) | TO, JJR, ITKK use *ampumasuunta*; *tulensuunta* is not in the sources |
| Fix (task) | Sitominen | SKK 2024/2026 *sitoa vihollisen huomio* = Soldiers' Guide 2020 *fix the enemy's attention*; JJR *sitoo vihollisen taisteluun*. The obstacle effect *fix* is *hidastaminen* (SuojKK) |
| Retain (task) | Pitäminen | TO 2013 and SKK 2026 position sketches: *pidettävä maastonkohta* (Soldiers' Guide: *terrain to be held*); SML map example *PITÄÄ*. SKK's *hallussa pitäminen* is about possessing weapons, not terrain |
| Relief in place (RIP) | Rintamavastuun vaihto | JJR 3.6.1 |
| Withdraw under pressure | Irtautuminen vihollisen painostaessa | JJR |
| Counterattack | Vastahyökkäys | SML I |
| Delay | Viivytys | SML I |
| Infantry / Armor / Anti-armor | Jalkaväki / panssari / panssarintorjunta | SML I |
| Reconnaissance | Tiedustelu | SML I |
| Signal | Viesti | SML I |
| Electronic warfare | Elektroninen sodankäynti | SML I, KT |
| Field artillery | Kenttätykistö | SML I |
| Air defense | Ilmatorjunta (branch symbol); NS uses *ilmapuolustus* for the broader concept | SML I, NS |
| Engineer: combat / construction | Pioneeri: taistelupioneeri / rakennuspioneeri | SML I |
| CBRN | Suojelu (branch); the abbreviation CBRN is kept (CBRN-aineet, Suojelukalusto (CBRN)). CBRN sensor = ilmaisin. *ABC/NBC/KBRN* are not used | SML I, SK |
| Ground zero | Räjähdyspiste; nuclear = ydinräjähdyksen räjähdyspiste | SuojKK 2022 ("Ydinräjähdyksessä lämpötila kohoaa räjähdyspisteessä") |
| Supply / Maintenance | Täydennykset / kunnossapito | SML I |
| Supply point / supply class | Jakopaikka / huoltoluokka (Class I–X = huoltoluokka I–X) | SML I; class: – |
| Combat service support (CSS) | Huolto (category); huoltojoukot (units); huoltotuki (CSS) under *Sustainment* | – |
| Army aviation | Maavoimien ilmailu | SML I |
| Wheeled / tracked / towed / over-snow / amphibious | Pyöräajoneuvo / tela-ajoneuvo / hinattava / lumiajoneuvo / uintikykyinen | SML I B 1 d |
| Light / Medium / Heavy (weapons and tanks) | Kevyt / raskas / järeä | SML I B 1 f kohta 22: "Panssarivaunut ja aseet, poislukien it-ohjukset sekä käsiaseet" are classed *kevyt / raskas / järeä* (1/2/3 bars); SML II D 3 b; AO (155 mm = raskas). Used for guns, howitzers, rocket and missile launchers, AT guns, AT missile and rocket launchers, recoilless guns, AD guns, tanks and tank recovery vehicles. Deliberate exceptions, which keep the NATO scale *kevyt / keskiraskas / raskas*: mortars (PV's 120 mm *raskas kranaatinheitin* matches NATO heavy), and machine guns and grenade launchers (infantry weapons; SML 21: "40 mm:n kevyt kranaattikonekivääri"). AD missiles, vehicles, aircraft and maintenance also keep the NATO scale |
| Recovery (vehicle) / tank recovery vehicle | Hinaus / hinauspanssarivaunu | SML II D 3 b, II D 8 c (*hinaus ja evakuointi*). *Evakuointi* is kept for casualties |
| Rotary wing | Helikopteri | – . SKK 2026 uses *pyöriväsiipinen* only for drones |
| Fixed wing | Kiinteäsiipinen | – |
| Fixed-wing roles: attack/strike, cargo, trainer, utility, tanker, patrol, reconnaissance, communications, passenger | Rynnäkkökone, kuljetuskone, koulukone, monitoimikone, ilmatankkauskone, partiokone, tiedustelukone, viestikone, matkustajakone | – |
| Special operations forces (SOF) / special forces (SF) | Erikoisjoukot (SOF) / erikoisjoukot (SF) | SML II H kohta 64, SKK 2026, NS (*special operations* = erikoisoperaatiot) |
| Psychological operations (PSYOP, MISO) | Psykologiset operaatiot (PSYOP) / (MISO) | – |
| Target acquisition | Maalitiedustelu | SML II D 4 d |
| Electronic support (ES/ESM) / electronic attack (EA) / electronic combat (EC) / jammer (ECM) | Elektroninen tuki / elektroninen vaikuttaminen / elektroninen sodankäynti (EC) / häirintäkone, häirintälennokki | KT 9.2.4.2 |
| Electro-optical | Optroniikka (maintenance branch); elektro-optinen (adjective) | SML II D 8 a |
| Improvised explosive device (IED) | Improvisoitu räjähde (IED) | SuojKK (C-IED) |
| Replacement holding unit (RHU) | Henkilötäydennyselin (RHU) | SML II C |
| Personnel recovery (PR) | Henkilöstön etsintä ja pelastaminen (PR) | SuojKK |
| Command vehicle (C2V, ACV) / bridge vehicle | Komentopanssarivaunu / silta-ajoneuvo | SML II D 3 b, II D 6 e |
| Tank | Taistelupanssarivaunu (symbols); *panssarivaunu* in the short palette name `tank` | SML I B 1 g |
| Infantry fighting vehicle | Rynnäkköpanssarivaunu | SML I B 1 g |
| Armored personnel carrier | Panssaroitu miehistönkuljetusajoneuvo | SML I B 1 g |
| Utility vehicle | Hyötyajoneuvo | – |
| UAV / UAS / drone | Lennokki / miehittämätön ilma-alus (UAS); reconnaissance UAV = tiedustelulennokki; *drooni* is an accepted synonym | SKK 2026 appendix, SML II E 5 c, TKO, RA |
| Minehunter / minelayer | Miinanetsijä / miinoittaja | MSK |
| Track (sensor track) | Raita (koeraita, alustava raita, käsin luotu raita) | – |
| Airspace control (areas, lines, points) | Ilmatilan valvonta-alueet / -linjat / -pisteet | – . *Open:* *valvonta* collides with *ilmavalvonta* (air surveillance); RA uses *ilmatilanhallinta* |
| Airspace coordination area (ACA) | Ilmatilan yhteensovitusalue (ACA) | – (JKK: *yhteensovittaminen*) |
| Missile engagement zone (MEZ) | Ilmatorjuntaohjusten torjuntavyöhyke (MEZ) | – |
| Surface combat air patrol (SUCAP) | Pintatorjunnan taistelupartio (SUCAP) | – |

## Obstacles, protection and CBRN

| English | Suomi | Source |
|---|---|---|
| Obstacle | Este (estevyö, estelinja, estevyöhyke) | SML II D 6 c |
| Obstacle effect | Sulutteen vaikutus | SuojKK. A *sulute* is a combination of mines, charges and obstacles (JJR 3.2.3), so it is narrower than *obstacle* |
| Block / fix / turn / disrupt (obstacle effect) | Pysäyttäminen / hidastaminen / ohjaaminen / häiritseminen | SuojKK 2.3.9 |
| Roadblocks, craters and blown bridges | Hävitteet (tiesulut, kuopat, räjäytetyt sillat) | SML II D 6 b |
| Roadblock planned / safe (SoR 1) / armed but passable (SoR 2) / executed | Hävite, suunniteltu / panostettu ja varmistettu / hävittämisvalmis, läpikuljettava / toimeenpantu | SML II D 6 b, JJR 3.2.3. PV readiness numbering differs from NATO, so the NATO number is shown |
| Abatis | Puumurroste | SML II D 6 b |
| Concertina wire | Lieriöeste | SML II D 6 c |
| Antitank ditch (under construction / complete / reinforced with antitank mines) | Panssariestekaivanto (valmisteilla / valmis / jossa miinoite) | SML |
| Minefield (static / dynamic) / dummy minefield | Miinoite (asennettu / sirotettava) / valemiinoite | TO, SKK 2026 (*sirotemiinoite*) |
| Antipersonnel / antitank mine; directional AP mine | Jalkaväkimiina / panssarimiina; viuhkapanos (suunnattu jalkaväkimiina) | SKK 2026 3.9.1 |
| Anti-handling device | Käsittelynestolaite | SKK 2026. SML 2005 has *raivauksenestolaite* |
| Sea mine: drifting (floating) / moored / bottom; neutralized mine | Ajomiina / ankkuroitu miina / pohjamiina; vaarattomaksi tehty miina | SML II F 8, MSK |
| Fighting position | Potero, pesäke tai asepaikka | SML II D 6 c |
| Shelter above / below ground | Sirpalesuoja maan päällä / maan alla (korsu) | SML II D 6 c |
| Mobility and survivability / survivability | Liikkeen- ja suojanedistäminen / suojanedistäminen | SNKK 1.2 |
| Contaminated area (biological, chemical, radiological, nuclear) | Saastealue (biologinen, kemiallinen, radiologinen saastealue; nuclear = ydinsaastealue) | SK 3.2.3 |
| Decontamination: immediate / operational / thorough | Välitön / täydentävä / perusteellinen puhdistus | SK 3.5.1 (execution 4.6) |
| Light line | Pimennysraja | – (own choice) |

## Fires and reporting

| English | Suomi | Source |
|---|---|---|
| Call for fire | Tulikomento | TO 5.5 |
| Target | Maali | TO 5.5 |
| Forward observer | Tulenjohtaja | TO 5.5 |
| Observer | Tähystäjä | TO 5.4 |
| Danger close | Danger close (varmuusetäisyyden sisällä) | TO: *varmuusetäisyys*; the NATO term is kept because it is used verbatim in CAS and fires procedures |
| Close air support (CAS) | Lähi-ilmatuki (CAS) | – |
| Final attack heading (FAH) | Hyökkäyssuunta (FAH) | ITKK. The *Direction of Attack* graphics use *tarkka hyökkäysreitti*, so the two do not collide |
| Final protective fire (FPF) | Torjuntamaali (FPF) | SKK 2026 (*epäsuoran tulen torjuntamaali*), JJR |
| Munition | Ampumatarvike | TO |
| Range finder | Etäisyysmittari | TO |
| Known point | Kiintopiste | TO |
| Reference point | Viitepiste | – |
| Target reference point (TRP) | Maalin viitepiste (TRP) | – . *Open:* JJR and SKK 2026 use *maalipiste* |
| Air warning / air raid alert | Ilmavaroitus / ilmahälytys | TO, JJR 4.1.5, SKK 5.9.8 / 4.9.9 |
| Air surveillance | Ilmavalvonta | NS, SML, SKK 5.9.8 / 4.9.9 |
| Restricted area (airspace) | Rajoitusalue (R-alue) | RA |
| Airspace management cell (AMC) | Ilmatilanhallintayksikkö (AMC) | RA |
| Suppression (fires) | Lamauttaminen | TO, JJR |
| Risk estimate distance (RED) / minimum safe distance (MSD) | Riskiarvioetäisyys (RED) / varmuusetäisyys (MSD) | RED: –; MSD: JJR liite 1.2 (definition of *varmuusetäisyys*) |

## Medical

| English | Suomi | Source |
|---|---|---|
| Tactical combat casualty care (TCCC) | Taisteluensiapu; protocol cABC (every soldier) / cABCDE (combat lifesaver) | TEA, SKK 5.9.10 / 4.7.7 |
| Casualty (wounded) | Haavoittunut | TEA |
| Combat lifesaver / medic | Taistelupelastaja / lääkintämies | TEA (taistelupelastaja), JJR and TO (lääkintämies) |
| Tourniquet / dressing / rescue blanket | Kiristysside / ensiside / pelastuspeite | TEA, SKK 5.9.10 / 4.7.7 |
| Nasopharyngeal airway / occlusive dressing / needle decompression / hemostatic | Nenänieluputki / ilmatiivis sidos / paineilmarinnan purkaminen / hemostaatti | TEA |
| Recovery position | Kylkiasento | TEA |
| Emergency move (drag to cover) | Hätäsiirto (suojaan) | TEA, SKK |
| Casualty evacuation (CASEVAC) / evacuation preparation | Evakuointi (CASEVAC) / evakuointivalmistelut | TEA. SuojKK calls CASEVAC *hätäsiirto*, which would collide with *Emergency move* |
| Medical evacuation (MEDEVAC) | Potilasevakuointi (MEDEVAC) | SuojKK, HJKK |
| Casualty report (MIST) | AT-MIST-raportti | TEA |
| Triage / triage card | Potilasluokittelu / luokittelukortti | TEA, KOTS |
| Casualty collection point | Haavoittuneiden kokoamispaikka (symbol; pattern of SML *sotavankien kokoamispaikka*) | – . *Open.* PV has no single term: TO 2013 moves casualties to the *evakuointipaikka* and then to the *hoitopaikka*; SKK 2024 *evakuointi-/hoitopaikka* = Soldiers' Guide *evacuation/casualty collection point*; SKK 2026 *lääkintä-/evakuointipaikka* = *Casualty Collection/Evacuation Point* |
| Litter / ambulatory (patient) | Paaripotilas / kävelevä | SK 4.8, TKO |
| MEDEVAC precedence: urgent / urgent surgical / priority / routine | Kiireellinen / kiireellinen kirurginen / etusija / rutiini | – |

## Communications and networks

| English | Suomi | Source |
|---|---|---|
| Command post | Johtamispaikka (komentopaikka) | JJR 2.3, SML II |
| Field radio / software-defined radio (SDR) | Kenttäradio / ohjelmistoradio | TO 7, SML; SDR: – |
| Message handling system | Sanomanvälitysjärjestelmä | VM |
| End user device (EUD) / terminal | Päätelaite | JJR, KT |
| Backbone network / wireless backbone | Runkoverkko / langaton runkoverkko | KT, VM |
| Access network | Liityntäverkko | KT, VM |
| Mobile ad hoc network (MANET) | MANET-verkko | VM |
| Mesh network | Mesh-verkko | – |
| Radio link | Radiolinkki | VM |
| Input / output (network connection) | Saapuva / lähtevä yhteys | – |
| Streaming | Suoratoisto; the persistent TAK Server connection may also be *palvelinyhteys*; video stream = videovirta | MS |
| Multicast | Multicast | – (MS: *monilähetys*; kept as the technical term) |
| Message (CoT, SA, chat) | Viesti | – (PV uses *sanoma* for formatted messages) |
| Encryption | Salaus | KTS, TO 7.2 |
| Certificate / client certificate / trust store / passphrase | Varmenne / asiakasvarmenne / luottamussäilö / tunnuslause | MS |

## Software / UI

| English | Suomi | Source / note |
|---|---|---|
| Settings / Preferences | Asetukset | MS |
| File name extension | Tiedostotunniste | MS. Not bare *tunniste*, which reads as *tunnistetiedot* (credentials) |
| Plugin | Laajennus | MS |
| Overlay / Overlay Manager | Karttataso / karttatasojen hallinta | Owner's decision |
| Image overlay (CIV) / video overlay / FOV overlay | Kuvapäällyste / videon karttapäällyste / näkökenttäkuvio | – |
| Imagery | Kuva-aineisto | – |
| Marker / map item | Merkki / karttakohde | – |
| Callsign | Kutsutunnus | – (MS: *kutsumerkki*) |
| Broadcast | Lähetä kaikille | – |
| Stale (data) | Vanhentunut | – |
| Data package / mission package | Datapaketti; *paketti* in short messages | – |
| Alert / emergency alert | Hälytys / hätähälytys; the Alert tool is *Hätähälytys* | MS |
| Notification | Ilmoitus | MS |
| Iconset | Kuvakesarja | – |
| Track number (TADIL-J) / datalink ID | Raitanumero / datalinkkitunnus | – |
| Quick Pic | Pikakuva | – |
| Telestration | Vapaan käden piirto | – |
| Viewshed | Näkyvyysalue | – . *Open:* MPKK 2003 (Hyytiäinen) uses *näkemäalue* |
| Label (map) | Nimiö | – |
| Chat | Chat (chat-viesti, chat-historia) | – |
| Configuration | Määritykset | MS |
| Polyline (line string) | Murtoviiva | SML II, GIS |
| Map tile / tileset | Karttatiili / tiilisarja | GIS. *Ruutu* is kept for the MGRS square |
| Feature (GIS) | Kohde | GIS |
| Geofence; geofence monitoring | Alueraja; aluerajan valvonta (tracked items: *valvotut kohteet*) | Owner's decision. *Aluevalvonta* is not used: in law and PV usage it means territorial surveillance. Fence name = *Aluerajan nimi*; trigger Entry / Exit / Both = *Saapuminen / Poistuminen / Molemmat*. The key `exit` is also the app menu's Exit (*Sulje ATAK*), so the 5.8 package has its own `geofence_triggers_names` |
| Heat map | Lämpökartta | MS |
| Dismiss (alert) | Kuittaa | – . The key `dismiss` is also used as a plain close button (upstream issue) |
| Layer (map layer, WMS layer) | Taso; overlay = karttataso | – |
| Radial menu | Ympyrävalikko | – (MS: *kehävalikko*) |
| Shape (drawn object) | Muoto | MS |
| Scan (search for devices, files or apps) | Haku | – |

### Tool names

| English (tool) | Suomi | Note |
|---|---|---|
| Point Dropper | Merkin lisäys | – |
| Red X (tool) | Koordinaatit kartalta | The map marker itself stays *punainen X* |
| Bloodhound | Kohteen seuranta | Strings say *seuranta*, *seurattava kohde* |
| Digital Pointer | Osoitin (DP) | *DP-osoitin* in sentences |
| Toolbar Manager | Työkalupalkit | – |
| Elevation Tools | Maastoanalyysi | Tile has a `\u200B` break point |
| Rubber Sheet | Georeferointi | *georeferoitu kuva / 3D-malli* |
| Link EUD | Linkitä TAK.GOV-tiliin | – |
| First Person | FPV-näkymä | – |
| Go To | Siirry sijaintiin | The dialog button stays *Siirry* |
| Orientation (screen) | Näytön suunta | *Suuntaus* is a map term in PV usage |
| Import | Tuo tiedostoja | The button stays *Tuo* |
| Quit | Sulje ATAK | *Lopeta* stays for stopping an action (navigation, editing, monitoring) |
| End (toolbar button) | Valmis | The key is shared with the track history date range (upstream issue) |
| NO GNSS / NO GPS (map warning) | EI GNSS-SIGNAALIA / EI GPS-SIGNAALIA | 5.8 says GNSS, 5.5 says GPS |
| Quick Nav, Lasso Select, Clear Content | Pikanavigointi, Lassovalinta, Tyhjennä sisältö | Unchanged after review |
