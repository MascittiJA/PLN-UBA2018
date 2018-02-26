Trabajo Práctico 2 - Etiquetado de Secuencias
=============================================

Mascitti, Julio Augusto
=================

Ejercicio 1: Corpus AnCora - Estadísticas de etiquetas POS
----------------------------------------------------------
Se modificó el script *stats.py*, que se encarga de mostrar las siguientes estadísticas del corpus AnCora:

#### Basic Statistics

* Sents: 17378
* Tokens: 517194
* Words: 46501
* Tags: 85


#### Most Frequent POS Tags

##### Etiquetas

|   Tag   |         Descripción         |
|:-------:|:---------------------------:|
|  sp000  |         Preposición         |
| nc0s000 | Sustantivo común (singular) |
| da0000  |     Artículo (definido)     |
| aq0000  |   Adjetivo (descriptivo)    |
|   fc    |            Coma             |
| np00000 |      Sustantivo propio      |
| nc0p000 |  Sustantivo común (plural)  |
|   fp    |            Punto            |
|   rg    |     Adverbio (general)      |
|   cc    |   Conjunción (coordinada)   |

##### Estadísticas

|   Tag    | Frecuencia | Porcentaje |         5 Palabras mas frecuentes         |
|:--------:|:----------:|:----------:|:-----------------------------------------:|
|  sp000   |   79884    |   15.45 %  |           (de, en, a, del, con)           |
| nc0s000  |   63452    |   12.27 %  |  (presidente, equipo, partido, país, año) |
|  da0000  |   54549    |   10.55 %  |           (la, el, los, las, El)          |
|  aq0000  |   33906    |   6.56 %   |    (pasado, gran, mayor, nuevo, próximo)  |
|    fc    |   30147    |   5.83 %   |                    (,)                    |
| np00000  |   29111    |   5.63 %   | (Gobierno, España, PP, Barcelona, Madrid) |
| nc0p000  |   27736    |   5.36 %   |  (años, millones, personas, países, días) |
|    fp    |   17512    |   3.39 %   |                    (.)                    |
|    rg    |   15336    |   2.97 %   |        (más, hoy, también, ayer, ya)      |
|    cc    |   15023    |   2.90 %   |           (y, pero, o, Pero, e)           |


#### Word Ambiguity Levels

| Nivel de Ambigüedad  | #Palabras | Porcentaje |     5 Palabras mas frecuentes      |
|:--------------------:|:---------:|:----------:|:----------------------------------:|
|          1           |   43972   |   94.56 %  |        (,, con, por, su, El)       |
|          2           |   2318    |   4.98 %   |         (el, en, y, ", los)        |
|          3           |    180    |   0.39 %   |         (de, la, ., un, no)        |
|          4           |    23     |   0.05 %   |      (que, a, dos, este, fue)      |
|          5           |     5     |   0.01 %   | (mismo, cinco, medio, ocho, vista) |
|          6           |     3     |   0.01 %   |          (una, como, uno)          |
|          7           |     0     |    0.0 %   |              ()                    |
|          8           |     0     |    0.0 %   |              ()                    |
|          9           |     0     |    0.0 %   |              ()                    |


Ejercicio 2: Baseline Tagger
----------------------------
Se implemento en el archivo *baseline.py* un "Etiquetador Baseline", el cual se encarga de etiquetar cada palabra con su etiqueta más frecuente observada en entrenamiento y a las palabras desconocidas, es decir, aquellas no vistas en el entrenamiento, las etiquetamos con la etiqueta **nc0s000**.
Se realizan comparaciones contra el "Etiquetador BadBaseline" provisto por la cátedra.

## BadBaseline

### Evaluación del "Etiquetador BadBaseline"
* Accuracy sobre todas las palabras = 12.65 %
* Accuracy sobre las palabras conocidas = 0.00 %
* Accuracy sobre las palabras desconocidas = 12.65 %

#### Matriz de confusión para los 10 tags más frecuentes

|  g\m    |  sp000  | nc0s000 | da0000  | aq0000  |   fc    | nc0p000 |   rg    | np00000 |   fp    |   cc    |
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|  sp000  |    -    |  14.39  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
| nc0s000 |    -    |  12.65  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
| da0000  |    -    |   9.70  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
| aq0000  |    -    |   7.28  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
|   fc    |    -    |   5.85  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
| nc0p000 |    -    |   5.53  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
|   rg    |    -    |   3.73  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
| np00000 |    -    |   3.58  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
|   fp    |    -    |   3.55  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
|   cc    |    -    |   3.41  |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |


## Baseline

### Evaluación del "Etiquetador Baseline"
* Accuracy sobre todas las palabras = 87.58 %
* Accuracy sobre las palabras conocidas = 95.27 %
* Accuracy sobre las palabras desconocidas = 18.01 %

#### Matriz de confusión para los 10 tags más frecuentes



|  g\m    |  sp000  | nc0s000 | da0000  | aq0000  |   fc    | nc0p000 |   rg    | np00000 |   fp    |   cc    |
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|  sp000  |  14.28  |  0.05   |    -    |    -    |    -    |    -    |  0.01   |    -    |    -    |    -    |
| nc0s000 |    -    |  12.22  |    -    |  0.25   |    -    |    -    |  0.03   |    -    |    -    |    -    |
| da0000  |    -    |  0.15   |  9.54   |    -    |    -    |    -    |    -    |    -    |    -    |    -    |
| aq0000  |  0.01   |  2.05   |    -    |  4.84   |    -    |  0.13   |    -    |    -    |    -    |    -    |
|   fc    |    -    |    -    |    -    |    -    |  5.85   |    -    |    -    |    -    |    -    |    -    |
| nc0p000 |    -    |  1.24   |    -    |  0.20   |    -    |  4.09   |    -    |    -    |    -    |    -    |
|   rg    |  0.02   |  0.31   |    -    |  0.04   |    -    |    -    |  3.27   |    -    |    -    |  0.02   |
| np00000 |    -    |  2.05   |    -    |    -    |    -    |    -    |    -    |  1.52   |    -    |    -    |
|   fp    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |    -    |  3.55   |    -    |
|   cc    |    -    |  0.01   |    -    |    -    |    -    |    -    |  0.05   |    -    |    -    |  3.34   |


Ejercicio 3: Features para Etiquetado de Secuencias
----------------------------

Se implementaron en features.py los siguientes features básicos:
* word_lower: la palabra actual en minúsculas.
* word_istitle: la palabra actual empieza en mayúsculas.
* word_isupper: la palabra actual está en mayúsculas.
* word_isdigit: la palabra actual es un número.

También se implementaron los siguientes features paramétricos:
* NPrevTags(n): la tupla de los últimos n tags.
* PrevWord(f): Dado un feature f, aplicarlo sobre la palabra anterior en lugar de la actual.

