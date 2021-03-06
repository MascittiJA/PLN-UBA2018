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


Ejercicio 4: Maximum Entropy Markov Models
------------------------------------------

#### Comparación de la Accuracy de los distintos modelos entrenados con MEMM, con su tiempo de evaluación y usando distintos clasificadores


##### Clasificador *"Logistic Regression"*

| N |Accuracy todas las palabras|Accuracy palabras conocidas|Accuracy palabras desconocidas|Tiempo de Entrenamiento|Tiempo de Evaluación|
|:-:|:-------------------------:|:-------------------------:|:----------------------------:|:---------------------:|:------------------:|
| 1 |          91.53 %          |          95.04 %          |           59.68 %            |       8m 12,811s      |       19,308s      |
| 2 |          91.36 %          |          94.74 %          |           60.75 %            |      11m 3,149s       |       21,888s      |
| 3 |          91.23 %          |          94.35 %          |           62.97 %            |      13m 4,572s       |       20,904s      |
| 4 |          90.80 %          |          94.08 %          |           61.15 %            |      14m 8,047s       |       22,338s      |

##### Clasificador *"Linear SVC"*

| N |Accuracy todas las palabras|Accuracy palabras conocidas|Accuracy palabras desconocidas|Tiempo de Entrenamiento|Tiempo de Evaluación|
|:-:|:-------------------------:|:-------------------------:|:----------------------------:|:---------------------:|:------------------:|
| 1 |          93.76 %          |          97.51 %          |           59.82 %            |       5m 9,889s       |       19,969s      |
| 2 |          93.90 %          |          97.45 %          |           61.78 %            |       5m 51,705s      |       20,179s      |
| 3 |          94.24 %          |          97.48 %          |           64.92 %            |       5m 52,733s      |       21,402s      |
| 4 |          93.87 %          |          97.22 %          |           62.47 %            |       7m 8,440s       |       21,878s      |

##### Clasificador *"Multinomial NB"*

| N |Accuracy todas las palabras|Accuracy palabras conocidas|Accuracy palabras desconocidas|Tiempo de Entrenamiento|Tiempo de Evaluación|
|:-:|:-------------------------:|:-------------------------:|:----------------------------:|:---------------------:|:------------------:|
| 1 |          76.50 %          |          79.73 %          |           47.21 %            |         39,847s       |     54m 32,729s    |
| 2 |          67.55 %          |          70.28 %          |           42.83 %            |         46,070s       |     57m 57,582s    |
| 3 |          55.97 %          |          58.41 %          |           33.89 %            |       1m 1,143s       |     70m 13,151s    |
| 4 |          64.96 %          |          67.59 %          |           41.07 %            |       1m 7,083s       |     82m 13,572s    |



