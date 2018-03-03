Trabajo Práctico 4 - Sentiment Analysis at Tweet
================================================

Mascitti, Julio Augusto
================= 


Ejercicio 1: Corpus de Tweets: Estadísticas Básicas
----------------------------------------------------------

El corpus InterTASS se compone de un conjunto de tweets en español, cada uno anotado con su polaridad general. Los valores posibles para la polaridad son los siguientes:

* P: Polaridad positiva.
* N: Polaridad negativa.
* NEU: Polaridad neutra.
* NONE: Sin polaridad.

Puede encontrar una descripción más detallada del significado de cada etiqueta en este [documento].

[documento]: https://cs.famaf.unc.edu.ar/~francolq/criterios_polaridad.pdf

Programamos un script stats.py que muestre las siguientes estadísticas básicas de la sección de entrenamiento del corpus InterTASS, y por separado para la sección de entrenamiento del corpus GeneralTASS:



### Basic Statistics  InterTASSReader
|                | Cantidad de Tweets |
|:--------------:|:------------------:|
| Tweets Totales |        1008        |
| Sentiment P    |         318        |
| Sentiment N    |         418        |
| Sentiment NEU  |         133        |
| Sentiment NONE |         139        |


### Basic Statistics  GeneralTASSReader
|                | Cantidad de Tweets |
|:--------------:|:------------------:|
| Tweets Totales |        7219        |
| Sentiment P    |        1232        |
| Sentiment N    |        1335        |
| Sentiment NEU  |         670        |
| Sentiment NONE |        1483        |




Curvas de aprendizaje para los tres clasificadores (mnb, maxent y svm). Usar el script curve.py.
Resultado de la evaluación sobre el corpus de development de InterTASS. Usar el script eval.py.
Para una sola de las mejoras, usando maxent, reportar además:

Features más relevantes para cada sentimiento. Usar print_maxent_features del módulo sentiment.analysis.
Tweet de ejemplo, con todos los features que intervienen y sus respectivos pesos para cada clase. Usar pprint_feature_weights_for_item del módulo sentiment.analysis.
Mejor Tokenizer
El tokenizer por defecto del CountVectorizer filtra toda la puntuación y los emojis. Sin embargo los emojis y algunas puntuaciones son indicadoras de sentimiento (e.g. “!” y “?”). Cambiar el tokenizer por uno que no elimine emojis y puntuación. Una opción posible es el tokenizador de NLTK.


Ejercicio 2: Mejoras al Clasificador Básico de Polaridad
----------------------------------------------------------

Implementamos, en el clasificador de sentimientos, las siguientes mejoras.

##### Binarización de Conteos
Modificamos la configuración del CountVectorizer para que ignore las repeticiones de palabras.

##### Normalización Básica de Tweets
Preprocesamos los textos de los tweets de la siguiente manera:

* Eliminamos menciones de usuarios.
* Eliminamos URLs.
* Contrajimos repeticiones de 3 o más vocales.

##### Filtrado de stopwords
Modificamos el CountVectorizer para que ignore stopwords del castellano (palabras sin carga semántica como artículos, preposiciones, etc.).

##### Manejo de Negaciones
Modificar el tokenizador del CountVectorizer para que además maneje negaciones. Al encontrar una negación ('no', 'tampoco', etc.), deben modificarse las siete palabras siguientes o hasta el siguiente signo de puntuación, agregándoles el prefijo NOT_.

##### Lematización
Modificamos el tokenizador del CountVectorizer para que además haga lematización de las palabras.


## Experimentación

Vamos a ir agregando incrementalmente las distintas mejoras y ver como se modifican los resultados para el calsificador.


### *Binarización de Conteos*

#### LogisticRegression

##### Curva de Aprendizaje

|   N   | Accuarcy |   F1   |
|:-----:|:--------:|:------:|
|   64  |  45.06%  | 30.64% |
|  128  |  44.27%  | 26.65% |
|  257  |  48.62%  | 33.76% |
|  514  |  49.01%  | 34.27% |
| 1028  |  52.17%  | 37.51% |
| 2056  |  53.36%  | 42.94% |
| 4113  |  53.75%  | 41.27% |
| 8227  |  51.19%  | 38.35% |

##### Resultados de Evaluación

| Polaridad | Cantidad de Tweets |     Precision    |       Recall     |   F1   |
|:---------:|:------------------:|:----------------:|:----------------:|:------:|
|     P     |        227         | 51.98% (118/227) | 75.64% (118/156) | 61.62% |
|     N     |        214         | 58.88% (126/214) | 57.53% (126/219) | 58.20% |
|    NEU    |         16         | 12.50% (2/16)    |  2.90% (2/69)    |  4.71% |
|   NONE    |         49         | 26.53% (13/49)   | 23.42% (13/62)   | 23.42% |

* Accuracy: 51.19% (259/506)
* Macro-Precision: 37.47%
* Macro-Recall: 39.26%
* Macro-F1: 38.35%

#### LinearSVC

##### Curva de Aprendizaje

|   N   | Accuarcy |   F1   |
|:-----:|:--------:|:------:|
|   64  |  44.66%  | 30.54% |
|  128  |  43.48%  | 30.47% |
|  257  |  46.64%  | 31.98% |
|  514  |  47.63%  | 35.52% |
| 1028  |  50.99%  | 40.30% |
| 2056  |  50.00%  | 40.07% |
| 4113  |  51.58%  | 40.68% |
| 8227  |  50.40%  | 40.30% |

##### Resultados de Evaluación

| Polaridad | Cantidad de Tweets |     Precision    |       Recall     |   F1   |
|:---------:|:------------------:|:----------------:|:----------------:|:------:|
|     P     |        198         | 54.55% (108/198) | 69.23% (108/156) | 61.02% |
|     N     |        193         | 63.21% (122/193) | 55.71% (122/219) | 59.29% |
|    NEU    |         38         | 15.79% (6/38)    |  8.70% (6/69)    | 11.21% |
|   NONE    |         77         | 24.68% (19/77)   | 30.65% (19/62)   | 27.34% |

* Accuracy: 50.40% (255/506)
* Macro-Precision: 39.56%
* Macro-Recall: 41.07%
* Macro-F1: 40.30%

#### MultinomialNB

##### Curva de Aprendizaje

|   N   | Accuarcy |   F1   |
|:-----:|:--------:|:------:|
|   64  |  46.05%  | 35.98% |
|  128  |  46.64%  | 36.45% |
|  257  |  49.41%  | 38.38% |
|  514  |  54.55%  | 48.62% |
| 1028  |  54.94%  | 42.70% |
| 2056  |  52.96%  | 41.44% |
| 4113  |  51.78%  | 46.76% |
| 8227  |  53.36%  | 46.95% |

##### Resultados de Evaluación

| Polaridad | Cantidad de Tweets |     Precision     |       Recall     |   F1   |
|:---------:|:------------------:|:-----------------:|:----------------:|:------:|
|     P     |        264         |  48.11% (127/264) | 81.41% (127/156) | 60.48% |
|     N     |        240         |  59.17% (142/240) | 64.84% (142/219) | 61.87% |
|    NEU    |          0         | 100.00% (0/0)     |  0.00% (0/69)    |  0.00% |
|   NONE    |          2         |  50.00% (1/2)     |  1.61% (1/62)    |  3.12% |

* Accuracy: 53.36% (270/506)
* Macro-Precision: 64.32%
* Macro-Recall: 36.97%
* Macro-F1: 46.95%

### Binarización de Conteos + *Normalización, Tokenización, STOP Words, Negación*

#### LogisticRegression

##### Curva de Aprendizaje

|   N   | Accuarcy |   F1   |
|:-----:|:--------:|:------:|
|   64  |  51.19%  | 46.09% |
|  128  |  50.79%  | 35.58% |
|  257  |  51.98%  | 34.85% |
|  514  |  52.17%  | 37.89% |
| 1028  |  55.53%  | 40.33% |
| 2056  |  53.95%  | 39.29% |
| 4113  |  55.14%  | 42.90% |
| 8227  |  53.16%  | 42.37% |

##### Resultados de Evaluación

| Polaridad | Cantidad de Tweets |     Precision    |       Recall     |   F1   |
|:---------:|:------------------:|:----------------:|:----------------:|:------:|
|     P     |        193         | 55.44% (107/193) | 68.59% (107/156) | 61.32% |
|     N     |        219         | 63.47% (139/219) | 63.47% (139/219) | 63.47% |
|    NEU    |         11         | 27.27% (3/11)    |  4.35% (3/69)    |  7.50% |
|   NONE    |         83         | 24.10% (20/83)   | 32.26% (20/62)   | 27.59% |

* Accuracy: 53.16% (269/506)
* Macro-Precision: 42.57%
* Macro-Recall: 42.17%
* Macro-F1: 42.37%

#### LinearSVC

##### Curva de Aprendizaje

|   N   | Accuarcy |   F1   |
|:-----:|:--------:|:------:|
|   64  |  51.19%  | 46.09% |
|  128  |  50.79%  | 35.58% |
|  257  |  51.98%  | 34.85% |
|  514  |  52.17%  | 37.89% |
| 1028  |  55.53%  | 40.33% |
| 2056  |  53.95%  | 39.29% |
| 4113  |  55.14%  | 42.90% |
| 8227  |  53.16%  | 42.37% |

##### Resultados de Evaluación

| Polaridad | Cantidad de Tweets |     Precision    |       Recall     |   F1   |
|:---------:|:------------------:|:----------------:|:----------------:|:------:|
|     P     |        184         | 58.15% (107/184) | 68.59% (107/156) | 62.94% |
|     N     |        184         | 66.85% (123/184) | 56.16% (123/219) | 61.04% |
|    NEU    |         33         | 18.18% (6/33)    |  8.70% (6/69)    | 11.76% |
|   NONE    |        105         | 20.00% (21/105)  | 33.87% (21/62)   | 25.15% |

* Accuracy: 50.79% (257/506)
* Macro-Precision: 40.80%
* Macro-Recall: 41.83%
* Macro-F1: 41.31%

#### MultinomialNB

##### Curva de Aprendizaje

|   N   | Accuarcy |   F1   |
|:-----:|:--------:|:------:|
|   64  |  51.19%  | 46.09% |
|  128  |  50.79%  | 35.58% |
|  257  |  51.98%  | 34.85% |
|  514  |  52.17%  | 37.89% |
| 1028  |  55.53%  | 40.33% |
| 2056  |  53.95%  | 39.29% |
| 4113  |  55.14%  | 42.90% |
| 8227  |  53.16%  | 42.37% |

##### Resultados de Evaluación

| Polaridad | Cantidad de Tweets |     Precision     |       Recall     |   F1   |
|:---------:|:------------------:|:-----------------:|:----------------:|:------:|
|     P     |        289         |  46.71% (135/289) | 86.54% (135/156) | 60.67% |
|     N     |        203         |  63.55% (129/203) | 58.90% (129/219) | 61.14% |
|    NEU    |          5         |  40.00% (2/5)     |  2.90% (2/69)    |  5.41% |
|   NONE    |          9         |  55.56% (5/9)     |  8.06% (5/62)    | 14.08% |

* Accuracy: 53.56% (271/506)
* Macro-Precision: 51.54%
* Macro-Recall: 39.10%
* Macro-F1: 44.44%

### Binarización de Conteos + Normalización, Tokenización, STOP Words, Negación + *Lematización*

#### LogisticRegression

##### Curva de Aprendizaje

|   N   | Accuarcy |   F1   |
|:-----:|:--------:|:------:|
|   64  |  49.41%  | 39.09% |
|  128  |  50.99%  | 35.71% |
|  257  |  51.78%  | 34.40% |
|  514  |  52.37%  | 38.96% |
| 1028  |  55.14%  | 40.45% |
| 2056  |  53.95%  | 39.60% |
| 4113  |  54.37%  | 42.40% |
| 8227  |  52.57%  | 41.54% |

##### Resultados de Evaluación

| Polaridad | Cantidad de Tweets |     Precision    |       Recall     |   F1   |
|:---------:|:------------------:|:----------------:|:----------------:|:------:|
|     P     |        193         | 55.44% (107/193) | 68.59% (107/156) | 61.32% |
|     N     |        217         | 63.13% (137/217) | 62.56% (137/219) | 62.84% |
|    NEU    |         12         | 25.00% (3/12)    |  4.35% (3/69)    |  7.41% |
|   NONE    |         84         | 22.62% (19/84)   | 30.65% (19/62)   | 26.03% |

* Accuracy: 52.57% (266/506)
* Macro-Precision: 41.55%
* Macro-Recall: 41.53%
* Macro-F1: 41.54%

#### LinearSVC

##### Curva de Aprendizaje

|   N   | Accuarcy |   F1   |
|:-----:|:--------:|:------:|
|   64  |  47.43%  | 32.52% |
|  128  |  50.40%  | 38.35% |
|  257  |  48.22%  | 33.83% |
|  514  |  51.19%  | 40.16% |
| 1028  |  50.79%  | 39.56% |
| 2056  |  49.21%  | 40.16% |
| 4113  |  51.78%  | 42.21% |
| 8227  |  50.99%  | 42.12% |

##### Resultados de Evaluación

| Polaridad | Cantidad de Tweets |     Precision    |       Recall     |   F1   |
|:---------:|:------------------:|:----------------:|:----------------:|:------:|
|     P     |        184         | 58.15% (107/184) | 68.59% (107/156) | 62.94% |
|     N     |        184         | 66.30% (122/184) | 55.71% (122/219) | 60.55% |
|    NEU    |         32         | 21.88% (7/32)    | 10.14% (7/69)    | 13.86% |
|   NONE    |        106         | 20.75% (22/106)  | 35.48% (22/62)   | 26.19% |

* Accuracy: 50.99% (258/506)
* Macro-Precision: 41.770%
* Macro-Recall: 42.48%
* Macro-F1: 42.12%

#### MultinomialNB

##### Curva de Aprendizaje

|   N   | Accuarcy |   F1   |
|:-----:|:--------:|:------:|
|   64  |  47.43%  | 37.54% |
|  128  |  48.81%  | 32.52% |
|  257  |  53.75%  | 34.94% |
|  514  |  52.77%  | 33.18% |
| 1028  |  55.73%  | 38.23% |
| 2056  |  54.15%  | 37.20% |
| 4113  |  54.55%  | 45.91% |
| 8227  |  53.56%  | 43.92% |

##### Resultados de Evaluación

| Polaridad | Cantidad de Tweets |     Precision     |       Recall     |   F1   |
|:---------:|:------------------:|:-----------------:|:----------------:|:------:|
|     P     |        288         |  46.88% (135/288) | 86.54% (135/156) | 60.81% |
|     N     |        203         |  63.55% (129/203) | 58.90% (129/219) | 61.14% |
|    NEU    |          5         |  40.00% (2/5)     |  2.90% (2/69)    |  5.41% |
|   NONE    |         10         |  50.00% (5/10)    |  8.06% (5/62)    | 13.89% |

* Accuracy: 53.56% (271/506)
* Macro-Precision: 50.11%
* Macro-Recall: 39.10%
* Macro-F1: 43.92%


## Most relevant features for each class (logistic regression)
N:
* ;-) portada cont @ enhorabuena ([-1.9780129  -1.8682134  -1.55251974 -1.4973573  -1.46745479])
* odio peor corrupción muertos triste ([ 1.74157513  1.74395633  1.82044557  2.00196359  2.54580209])

NEU:
* parados portada enhorabuena puedes 6 ([-1.14602187 -1.08474828 -0.97504888 -0.8976541  -0.89028946])
* preguntamos gana expectación vicepresidenta broma ([ 1.30355993  1.31614667  1.33063504  1.38722546  1.43085216])

NONE:
* ;-) feliz gracias gran enhorabuena ([-2.23158739 -1.94235318 -1.90365041 -1.79526488 -1.71906066])
* reunión periódico #eperiódico @ portada ([ 1.24005603  1.27203672  1.31109169  1.41167461  2.43315639])

P:
* triste culpa urdangarin portada #griñan ([-1.57644839 -1.39185792 -1.34031194 -1.31188865 -1.19427057])
* :-) gracias homenaje ;-) enhorabuena ([ 1.99451619  2.05361368  2.13567493  2.44524985  2.57103435])



## Active features and their weight for a specific item
Tweet:  @Rafuki21 178. Sabes que me caes muy muy bien, y que en un futuro te daré un poco el coñazo con dudas de Diseño Gráfico 
Sntiment: Positivo

|   Token   |                         Wheight [N NEU NONE P]                        |
|:---------:|:---------------------------------------------------------------------:|
|     ,     |          [-0.02094202  0.10433742 -0.21106543  0.01421806]            |
|     .     |          [ 0.17543367  0.0565374  -0.46426042  0.02303487]            |
|  bien     |          [-0.50069804 -0.62630142 -1.405356    1.5405778 ]            |
|  caes     |          [-0.16846449 -0.0813297   0.44710004 -0.09607331]            |
|  coñazo   |          [ 0.48009137  0.3857831  -0.31392042 -0.46129672]            |
|  daré     | [ -3.98619747e-04  -2.65837115e-02  -6.20962575e-05  -2.95098878e-04] |
|  diseño   |          [ 0.22601443 -0.08535584 -0.02853186 -0.09502849]            |
|  dudas    |          [ 0.40287318 -0.15984348 -0.38897783  0.19514305]            |
|  futuro   |          [-0.66968169 -0.18222152 -0.10126743  0.76984224]            |
|  sabes    |          [-0.43809999  0.63762347 -0.14829316  0.14558753]            |



Ejercicio 3: Evaluación Final
----------------------------------------------------------

El clasificador que dió mejores resultados fue el *MultinomialNB* y los resultados del corpus de test final fueron:


##### Resultados de Evaluación

| Polaridad | Cantidad de Tweets |      Precision     |       Recall     |   F1   |
|:---------:|:------------------:|:------------------:|:----------------:|:------:|
|     P     |       1122         |  48.40% (543/1122) | 84.58% (543/642) | 61.56% |
|     N     |        725         |  64.14% (465/725)  | 60.63% (465/767) | 62.33% |
|    NEU    |          7         |  14.29% (1/7)      |  0.46% (1/216)   |  0.90% |
|   NONE    |         45         |  31.11% (14/45)    |  5.11% (14/274)  |  8.78% |

* Accuracy: 53.87% (1023/1899)
* Macro-Precision: 39.48%
* Macro-Recall: 37.69%
* Macro-F1: 38.57%

