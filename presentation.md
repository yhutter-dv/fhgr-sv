[comment]: # (THEME = black)
[comment]: # (CODE_THEME = monokai)
[comment]: # (controls: true)
[comment]: # (keyboard: true)
[comment]: # (markdown: { smartypants: true })
[comment]: # (hash: false)
[comment]: # (respondToHashChanges: false)
[comment]: # (Other settings are documented at https://revealjs.com/config/)


# Scientific Visualization 
Yannick Hutter | FHGR Chur | 

[comment]: # (!!!)

## Scientific Visualization
* Teilgebiet der Computergrafik
* Beschäftigt sich mit der **visuellen Darstellung naturwissenschaftlicher Phänomene**
* Dient dem **besseren Verständnis der zu Grunde liegenden Daten**
* Daten werden **vom Computer anhand von mathematischen/physikalischen Gesetzen generiert**

[comment]: # (!!!)

## Wissenschaftliche Simulation
* Wird für die **Rekonstruktion und Vorhersage** von Phänomenen und technischen Prozessen eingesetzt
* Ist die **dritte Säule der Erkennnis** (nebst Theorie und Experiment)

[comment]: # (!!!)

## Warum braucht es Simulationen?
* Nicht alle Experimente können durchgeführt werden
* Experimente sind teilweise unerwünscht oder zu kostspielig
* Simulationsergebnisse (reine Zahlen) oft nicht intuitiv, d.h. es braucht eine **visuelle Darstellung**

[comment]: # (!!!)

## Simulationspipeline
* Modellierung - Bestimmung von Parametern und Beziehungen
* Numerische Behandlung - Diskretisierung, Algorithmenentwicklung
* Implementierung - Softwareentwicklung, Parallelisierung
* **Visualisierung** - Darstellung abstrakter Simulationsergebnisse
* Validierung - Vergleich mit Realität
* Einbettung - Einführung in den Arbeitsprozess

[comment]: # (!!!)

## Komplexität
* Da es sehr Ressourcenintensiv ist Simulationen durchzuführen, sollte die **richtige Skala** gewählt werden (1D, 2D, 3D)
* 1D - keine Informationen in Breite und Höhe
* 2D - keine Information in der Höhe
* 3D - Alle Informationen vorhanden

[comment]: # (!!!)

## Beispiele von Simulationen
* Personenstromsimulation (basierend auf Cellular Automata)

[comment]: # (!!!)

## Geometrische Modellierung
* Beschreibung von Körpern im 3D Raum
* Modellierung von physikalischen Eigenschaften (Oberfläche, Volumen, Material etc.)
* Direkte Darstellung - **Darstellung von Volumen**
* Indirekte Darstellung - **Darstellung von Aussenseite** bspw. Computerspiele
* Strukturiertes Gitter - Wenn Objekt in X und Y Achse geschnitten wird und danach **gleich grosse Stücke resultieren**

[comment]: # (!!!)


## Rigid Body (Starre Körper)
* Keine Löcher, geschlossene Oberfläche
* Keine Probleme beim Flood Fill Algorithmus (Algorithmus weiss immer wo die Aussen und Innenseite ist)
* Orientierbar
* Mannigfaltigkeit möglich

[comment]: # (!!!)

## Mannigfaltikgeit
* Eine Kante gehört im Normalfall immer zu einer Fläche
* Bei der Mannigfaltigkeit gehört jedoch eine Kante zu **zwei Flächen**, bspw. wenn sich zwei Würfel eine Kante teilen

[comment]: # (!!!)

## Indirekte Darstellung
* Wird in Computergrafiken verwendet
* Modelle bestehen aus Vertices (V), Edges (E) und Faces (F)
* Es gilt die Eulersche Formel Nv-Ne+Nf = 2
* Diese gilt auch bei Vierecken
* Vertices speichern **geometrische Information**, Edges und Faces nur topologische Informationen

[comment]: # (!!!)

## VEF Graph
* Kanten können weggelassen werden
* Vertices werden dann im Uhrzeiger oder Gegenuhrzeigersinn angegeben

## Konvex vs. Konkav
* Bei Konvexen Körpern kann man irgendwo zwei Punkte wählen und eine Linie ziehen
* Die Linie verlässt dabei nie den Körper
* Konvexe Körper können sich auch nicht im gegensatz zu konkaven Körpern teilweise verdecken
* War wichtig in Computerspielen aus Performancegründen

[comment]: # (!!!)

## Volumenmodell (direkte Darstellung)
* Beschreibt wie viel Volumen das Modell einnimmt
* Ist ein bestimmer Punkt innerhalb oder Ausserhalb des Objektes?
* Wird auf Basis des Oberflächemodells erstellt
* Das Volumenmodell wird für die Berechnung benötigt

[comment]: # (!!!)
