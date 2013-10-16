Handleiding inkoopvoorstel Technotrading.
-----------------------------------------

Doel
====

De voorraad moet zo tijdig worden aangevuld, dat deze nooit onder een bepaald niveau (de ijzeren voorraad) komt, maar anderzijds zo laag mogelijk worden gehouden. Er moet dagelijks per product worden bepaald of er genoeg voorraad is om aan het einde van de levertermijn boven dit niveau te blijven, anders moet worden bijbesteld tot een maximum niveau.
Als een bestelling wordt geplaatst, moeten andere producten van dezelfde leverancier meebesteld kunnen worden, producten die ook bijna aan het minimum zitten.

Onderdelen
==========
Het inkoopvoorstel bestaat uit een aantal instellingen, processen en voorzieningen. De belangrijkste zijn:

* Instelling per product / leverancier van minimale en maximale voorraad;
* Elke dag automatische berekening van de gemiddelde omzet en een uiterste besteldatum;
* Per product is te zien wat de uiterste besteldatum en de dagomzet zijn;
* Per (primaire) leverancier is te zien wat de vroegste besteldatum van diens producten is;
* Per leverancier zijn de door hem geleverde producten te zien;
* Vanuit het leveranciersformulier kan de aanmaak van de inkoopofferte worden gestart, waarbij producten kunnen worden geselecteerd op basis van de uiterste besteldatum. Producten die incidenteel bij deze leverancier besteld worden zijn uitgesloten, maar kunnen ook mee besteld worden. De te bestellen hoeveelheid wordt automatisch berekend;
* Zodra een product in een inkoopofferte is opgenomen, wordt de uiterste besteldatum bij dat product verwijderd en bij de leverancier bijgewerkt, zodat direct andere offertes kunnen worden gemaakt;
* Bij het maken van bestellingen volgens de standaard wijze, wordt de hoeveelheid desgewenst identiek berekend.

Menu's
======

Alle benodigde menu's staan op hoofdmenu Inkoop.

* Offerteaanvraag onder Inkoop
* Leveranciers onder Adresboek,
* Producten onder Producten,
* Productcategoriën onder Instellingen/Producten

De dagelijkse run (Purchase Proposal Refresh) is ingesteld om elke nacht te worden uitgevoerd. Deze staat op hoofdmenu Instellingen onder Instellingen/Personeels enquêtes/Geplande acties

Begrippen
=========
 
* Inkoopvoorstel: feitelijk de uiterste besteldatum, die elke nacht per product en leverancier wordt bepaald en de bestelhoeveelheid die in de inkoopofferte wordt berekend
* Uiterste besteldatum, op deze datum wordt het minimale voorraadniveau bereikt

   * per product: voor zich sprekend; 
   * per leverancier: de uiterste besteldatum van het meest urgente product, dat primair door deze leverancier wordt geleverd

* Omzetperiode: het afgelopen aantal dagen waarover de dagomzet wordt berekend
* dagomzet: de gemiddelde omzet per dag in de omzetperiode
* Minimum voorraad: periode die verstrijkt tussen het maken van de inkooporder en de levering van de goederen. Neem de ijzeren voorraad hierin op.
* Maximum voorraad: de periode waarvoor de te bestellen hoeveelheid wordt berekend
* Bestelveelvoud: Aantal eenheden dat in een verpakking wordt geleverd, de bestelling wordt afgerond op dit veelvoud

Instellingen
============

Instellingen kunnen op een aantal plaatsen worden opgegeven. Bij voorkeur per product/leverancier, maar per leverancier of productcategorie kunnen standaardwaarden worden opgegeven. Instellingen per product gaan altijd voor, zijn die niet ingevuld dan gelden die van de leverancier of productcategorie. Als nergens een instelling is ingevuld geldt 91 dagen voor de maximum voorraad en de minimum voorraad en 364 dagen voor de omzetperiode. Bestelveelvoud is dan 1.

Per product(/leverancier) staan de betrokken gegevens op tabblad leveranciers (suppliers)

* maximum voorraad
* omzetperiode
* per leverancier

  * minimum voorraad
  * bestelveelvoud

Per leverancier staan de betrokken gegevens op tabblad inkoopvoorstel. De instellingen gelden voorzover niet opgegeven bij het product.

* maximum voorraad
* omzetperiode
* minimum voorraad

Per productcategorie, deze instelingen gelden als ze niet zijn opgegeven bij product of leverancier.

* maximum voorraad
* omzetperiode
* minimum voorraad

Berekeningen
============

* dagomzet: Gemiddelde omzet per dag gedurende de omzetperiode
* Uiterste leverdatum: Vandaag + (Virtuele voorraad / dagomzet) - minimum voorraad
* Bestelhoeveelheid: dagomzet * (maximum voorraad + minimum voorraad) - virtuele voorraad

Procedure
=========

Inkoopvoorstel
..............

Elke dag berekent een programma (Purchase Proposal Refresh) de gemiddelde dagomzet en uiterste besteldatum per product en de uiterste besteldatum per leverancier.

Zolang een product in een inkoopofferte is opgenomen, wordt de bestelling niet meegeteld in de virtuele voorraad en daarom wordt het door het proces overgeslagen (uiterste besteldatum is leeg), zodat het niet dubbel in het bestelproces komt.
Zodra een bestelling definitief is, wordt het product weer dagelijks beoordeeld.

Inkoopofferte
.............

Dagelijks moet de inkoper vanuit menu leveranciers controleren (sorteren op uiterste besteldatum) bij welke leveranciers een offerte moet worden aangevraagd.
Op het leverancier-formulier (tabblad inkoopvoorstel) kan door sortering worden bekeken welke producten besteld moeten worden in de komende dagen en kan de aanmaak van de offerte worden gestart (knop Maak inkoopofferte). Daarbij kan een selectie voor de te bestellen producten worden opgegeven.

De aangemaakte offerte's kunnen via de standaard functies worden afgewerkt. Er kunnen nog producten worden toegevoegd of verwijderd. Vul 0 in bij hoeveelheid om deze te laten berekenen. Bij verwijderen wordt de uiterste besteldatum niet opnieuw bepaald, dat gebeurt in de dagelijkse berekening.

Inrichten
.........

Onder reporting kunnen de leveringsgegevens worden geanalyseerd en geëxporteerd naar een spreadsheet, zodat de instellingen kunnen worden bepaald.

Inkoopvoorstel
,,,,,,,,,,,,,,
Menu: Instellingen, Instellingen/Personeels enquêtes/Geplande acties.

Het tijdstip van de dagelijkse run (Purchase Proposal Refresh) kan worden aangepast.

Product
,,,,,,,
Menu: Inkoop, Producten, Producten; tabblad Leveranciers.

Vul de omzetperiode, de minimum en de maximum voorraad in. De minimum voorraad moet worden ingevoerd in het lijstje van leveranciers. Daar kan ook een bestelveelvoud worden ingevuld.
Als een van deze instellingen voor alle producten of een categorie gelijk is, kan deze misschien beter per productcategorie of leverancier worden opgegeven.

Voorbeeld: 

* IJzeren voorraad = 60 dagen;
* maken inkoopofferte t/m aflevering goederen = 90 dagen;
* bijbestellen voor 75 dagen.

De minimum voorraad wordt dan ingesteld op 150 (60 + 90) en de maximum voorraad op 180. De uiterste besteldatum is de dag waarop er nog voor 150 dagen voorraad is.
Op het moment van bestellen wordt dan besteld voor 225 (150 + 75) dagen minus de virtuele voorraad.

Leverancier
,,,,,,,,,,,
Menu: Inkoop, Adresboek, Leveranciers; tabblad Inkoopvoorstel.

Minimum en maximum voorraad voor de leverancier kunnen worden opgegeven, die gelden dan voor de producten waarbij die instellingen mankeren.

Productcategorie
,,,,,,,,,,,,,,,,
Menu: Inkoop, Instellingen, Producten, Productcategoriën.

Omzetperiode, minimum en maximum voorraad voor de productcategorie kunnen worden opgegeven, die gelden dan voor de producten waarbij die instellingen mankeren en ook niet per leverancier zijn opgegeven.

Algemeen
,,,,,,,,
Als helemaal geen periode's zijn opgegeven, gelden 364 dagen voor de omzet- en 91 dagen voor de lever- en inkoopperiode. Voor bestelveelvoud is 1 de standaardwaarde.

