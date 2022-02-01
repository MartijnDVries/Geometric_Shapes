Ruimtelijke figuren
====

Dit was mijn eerste opdracht in python naast de opdrachten in het boek "Crash Course Programmere in Python". \
De bedoeling van deze opdracht was om mij bekend te raken met de syntax van python en dingen \
die ik nog niet kende vanuit Small Basic zoals classes en hun definities. 


Opdracht
----

Maak een programma in python waarbij je de eigenschappen van de volgende ruimtelijke figuren \
kan berekenen:

1. Rechthoek \
  Invoer: 
    * Lengte
    * Breedte 
    
   Uitvoer:
    * Omtrek
    * Oppervlakte
    
2. Cirkel\
  Invoer:
    * Diameter 
    
   Uitvoer:
    * Omtrek
    * Oppervlakte
    
3. Driehoek \
  Invoer:
    * Hoogte
    * Breedte 
    
   Uitvoer:
    * Oppervlakte
    
4. Rechthoekige Driehoek\
   Invoer:
     * Twee van de drie zijden 
   
   Uitvoer:
     * Derde zijde

5. Vlieger\
    Invoer:
      * Hoogte omhoog
      * Hoogte omlaag
     
     Uitvoer:
      * Oppervlakte

6. Kubus\
     Invoer:
      * Zijde (1x)

     Uitvoer:
      * Volume

7. Cilinder\
    Invoer:
      * Diameter
      * hoogte

    Uitvoer:
      * Volume

8. Piramide\
    Invoer:
      * Breedte
      * Hoogte

    Uitvoer:
      * Volume

9. Parallelogram\
    Invoer:
      * Zijde (1x)
      * Hoogte

    Uitvoer:
      * Oppervlakte

10. Trapezium\
    Invoer: 
      * Breedte
      * Hoogte

    Uitvoer:
      * Oppervlakte


Werkwijze
----

Taal: Python \
Libraries: Tkinter, Pillow, math \
Tools: Paint

Voor dit project is de weergave gedaan door tkinter. Tkinter is goed voor 2D grafische weergave \
De images die gebruikt zijn, zijn gemaakt in paint. Door het gebruik van de library Pillow zijn \
de images geintegreerd in de code. \
Met tkinter is het mogelijk om buttons, labels en entry's op het scherm te plaasten die een basis \
functionaliteit hebben. Om een duidelijke structuur in de layout te krijgen heb ik eerst een grid \
gemaakt waar je dan de zoganaamde widgets in kan plaatsen zonder dat je met x- en y- waarden aan \
de gang hoeft te gaan. In plaats daavan je de rij en de kolom kiezen waar je een bepaalde widget \
wil plaatsen. \
Ik wilde graag een interface waarin je kan scrollen tussen de pagina's. Dit heb ik gedaan door \
bepaalde widgets op het scherm te plaatsen en deze te binden aan een bepaalde pagina met een  \
if-then-else constructie. Als de pagina verandert door op één van de pijlen te klikken veranderen \
ook de widgets die op dat moment op het scherm zichtbaar zijn. \
Wanneer je op een button klikt met een bepaald figuur opent een nieuw scherm. De hoofdinterface \
verdwijnt dan. Hier in dit scherm zijn er meerdere dingen. Als eerste is er een back button. Deze \
button brengt je terug naar de hoofdinterface waarvan hij ook de pagina heeft onthouden waar je vandaan \
komt. Verder zijn er invoer widgets, door alle invoer widgets in te vullen zal er een berekening plaats \
vinden die de weergegeven worden in de uitvoer van deze figuur. Dit gebeurt onmiddelijk, zolang alle \
invoervelden maar ingevuld zijn. Wanneer je met de muis over de labels heen gaat (zonder te klikken) \
wordt er grafisch weergegeven om welke eigenschap van het figuur het gaat door middel van een kleur. \
Dit is gedaan door de muis-events (in dit geval hover) te binden aan bepaalde widgets. Er is geprogrammeerd \
wat er gebeurt als de muis hovert over de label, en wanneer de muis niet hovert over de label. \
Dit om de figuur weer terug te brengen in de originele staat wanneer er niet gehoverd wordt over \
een label. \
Voordat er een uitvoer op het scherm wordt weergegeven, vindt er nog een check plaats. Deze checkt \
de lengte van de uitvoer. Wanneer het getal dat de uitvoer geeft een komma getal is dat niet op het \
uitvoervenster past, wordt deze afgerond. Wanneer het getal te groot is (groter dan vijf nullen) voor \
de komma, dan wordt er een waarschuwing getoond dat het getal niet op het scherm past. Ik weet dat dit \
makkelijk gedaan kan worden met de library Decimal, maar ik vond het een uitdaging om zelf iets te \
programmeren wat goed werkt. 

    
