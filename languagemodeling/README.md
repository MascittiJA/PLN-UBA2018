 
Trabajo Práctico 1 - Modelado de Lenguaje
=========================================

Mascitti, Julio Augusto
=================


Ejercicio 1: Corpus
-------------------

Para este corpus utilizamos las obras del poeta español Antonio Machado que se encontraban dentro de las librerias de NLTK. Luego nos dimos cuenta que las mismas estaban en portugues, pero esto no interfiere en el desarrollo del TP en si mismo, salvo que los resultados estaràn en portugues.  
En este ejercicio se trabajo sobre el script *train.py*, se importaron las obras de machado y luego, más adelante, tuvimos que modificarlo par separa la información en archivos de entrenamiento y test.  


Ejercicio 2: Modelo de n-gramas
-------------------------------

En este ejercicio, teníamos una base implementada por al catedra en la cual se pedía modificar las funciones correspondientes a la clase NGram.  

Se implementaron los siguientes métodos:

    * count
    * cond_prob
    * sent_prob
    * sent_log_prob


Ejercicio 3: Generación de Texto
--------------------------------

En este punto, trabajamos sobre la clase NGramGenerator, implementando las funciones solicitadas.  

Se implementaron los siguientes métodos:

    * generate_token
    * generate_sent
    
Luego utilizamos el script *generate.py* para que carga el modelo de n-grama genreado con el script de *train.py* y arma una frase aleatorea.  


## Oraciones generadas

| n-gram | Oraciones                                                                                           |
|:------:|-----------------------------------------------------------------------------------------------------|
|   1    | dos que  ficavam sinceramente . ventura , vestuário filho até há los ; soltas embora poupou , compor falava . notícia deste o olhos com tempos entregasse nesta o , que condenado a que , empalideceu . .                                                     |
|        | de muita do O !... que . meu ; - , , anedotas Rezava as perguntou                                   |
|        | o olhava cai graça que . amor Deus Nosso                                                            |
|        | Emílio , passagem , de no os                                                                        |
|   2    | Amas deveras seminarista .
|        | Isto vai para Daniel encontrou um cafarnaum de Anacreonte                                           |
|        | Tanto que eu quisera conter - á a menor sombra ; que podem aceitar do pai não é que foi ter crido , falava Teresa e até os que levantasse dizendo francamente o murmúrio de vaidade , pareceu Flora se todos adoram , tão rasteira .                             |
|        | O cálculo , que era uma mão , pode representar os homens , mais que eles escutam                    |
|   3    | Desta Gazeta de Noticias , como era também uma cabeça verdadeiramente satânica .                    |
|        | Contudo , era tragédia o tirano do sétimo dia .                                                     |
|        |  Não lhe conto o que poderá com vantagem do Governo '.                                              |
|        | Foi nessa mesma tarde uma cruz do claustro , as reminiscências de criança , sem embargo de reconhecer - lhes os parabéns ao poeta quando se referia ao pai .                                                                                               |
|   4    | No dia 20 achei , com efeito , um grande centro populoso que lhe servisse de grande deserto para o coração virgem e modesto que só vê duas estrelas no futuro : a arte ou a família rejeita Helena , e aceitou o convite de Rodrigo e de D . Teresa não entende a metáfora , e disse - lhe no rosto o texto da Escritura : muitos são os chamados , poucos os escolhidos '.                                          |
|        | Era mentira ; mas eu não posso admitir que não tenhas coração; é faceirice de moça bonita e namorada , enfim ciúmes , ciúmes que ela sentia roerem - lhe o amor que há na alma humana que Labão é que faz de melhor , esse parvenu sem gosto , só por saber .     |
|        | -- Podia fazer isto mesmo quando chegasse à casa .                                                  |
|        | Duas parecem ser as principais .                                                                    |

Salvando el idioma, parece ser que a medida que se utilizan n-gramas de mayor tamaño, las frase comienzan atener más sentido.


Ejercicio 4: Suavizado "Add-One"
--------------------------------

En el archivo *ngram.py* tuvimos que modificar la clase AddOneNGram.  

Se implementaron los siguientes métodos:

    * countWordTypes
    * V
    * cond_prob

Utilizamos herencia para tener todos lo metodos de la clase NGram y modificamoes aquellos aspectos necesarios para la particularidad de AddOneNGram.

Ejercicio 5: Evaluación de Modelos de Lenguaje
----------------------------------------------

En este ejercicio se separo nuestro corpus en dos partes:
* corpus_train: para entrenamiento (90%)
* corpus_test: para pruebas (10%)

Para esto modificamos el script *train.py* y luego se utilizo el script *eval.py* para calcular la perplejidad de cada modelo de n-gramas entrenados con el suavizado addone sobre el conjunto resrevado para test.  

### Perplejidad de los modelos entrenados con el Suavizado Add-One

| n-gram | Perplexity |
|:------:|:----------:|
|   1    |    1219.3006500114234    |
|   2    |    3346.9848964422067    |
|   3    |   23057.28894979586      |
|   4    |   39455.24567433803      |

Al ver estos resultados, vemos que mientras el n se hace más grande, la perplexity aumenta.  
Por lo que podemos decir que el suavizado Add-One no es bueno, porque mientras más chica sea la perplexity mejor.


Ejercicio 6: Suavizado por Interpolación
----------------------------------------


### Perplejidad de los modelos entrenados con el Suavizado por Interpolación

| n-gram | Perplexity |
|:------:|:----------:|
|   1    |    1218.9872188272216  |
|   2    |    524.9305110000843   |
|   3    |    1665.9019988066066  |
|   4    |    7978.2720725965     |

Calculamos la perplexity usando como modelo el Suavizado por Interpolación y nuestra hipótesis era que a medida que aumentaba el n, iba a disminuir la perple, pero no vemos esto reflejado en los experimentos. No llegamos a hacer un análisis más profundo de que puede ser que sté pasando.  

