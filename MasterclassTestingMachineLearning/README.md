# QA Practice - AI Testing Fundamentals

Most useful courses to develop the skills needed in this new era of QAs in AI.

## QA_Practice-AI_Testing_Fundamentals

<https://perficient.udemy.com/learning-paths/10210909/>

[![Curso reciente ](images/2025-07-24_103320.png "Masterclass Testing Machine Learning (AI) Models
")](https://www.udemy.com/course/introduction-to-testing-ai-models-llms-and-chatbots/)

## Section 1: Introduction

### 1. Introduction to Material

>[!NOTE]
>
>1. Bienvenidos a este material sobre cómo probar modelos de IA, modelos de lenguaje extensos, chatbots, IA conversacional, etc.
>Este es un material único.
>Al momento de la grabación, no había otro material disponible en línea.
>Solo hay fragmentos de información sobre cómo probar y comparar modelos de IA.
>Y esta es la razón por la que decidí crear este tipo de material.
>En las próximas 8 o 9 horas, veremos qué es la IA hoy en día.
>Aquí les presento una introducción a la IA, ya que, en mi opinión, no se puede probar la IA hasta que se comprenda cómo funciona.
>2. Partiendo de eso, analizaremos las pruebas funcionales.
>¿Cómo se prueba funcionalmente un modelo de IA?
>Por supuesto, se realizará la generación.
>¿Cómo se generan texto, imágenes, vídeos, etc.?
>Pero también está la parte sobre el razonamiento de estilo y el _NPL_.
>Y luego analizaremos siete herramientas de código abierto que se pueden usar para comparar el modelo con diferentes tipos de problemas.
>Y esto se hará con Python.
>3. Continuando, analizaremos las pruebas adversarias.
>Se trata de una especie de prueba de penetración de seguridad.
>Sabemos que el modelo de IA puede usarse contra personas.
>Puede usarse para ingeniería social, para crear bombas, etc.
>Por eso también analizaremos cómo realizar ataques de envenenamiento, ataques de evasión, pruebas rápidas, fugas de privacidad, etc.
>4. Luego, veremos cómo se puede automatizar el chatbot.
>En nuestro caso, usaremos Postman.
>Usaremos GitHub.
>Haremos pruebas automatizadas con ChatGPT.
>Al final, esto se integrará en una canalización CSV para sentar las bases, al menos para la parte de pruebas de MLOps.
>5. Y, por último, pero no menos importante, analizaremos las consideraciones éticas de la IA, ya que, al final, la IA está cada vez más regulada.
>Por ejemplo, si quieres implementar tu modelo de IA en la Unión Europea, debes cumplir ciertos criterios.
>Así que analizaremos cómo podemos detectar sesgos.
>¿Cuáles son los riesgos asociados con la IA, la imparcialidad, etc.?
>
>![Introduction to Material](images/2025-07-29_104459.png "Introduction to Material")



### 2. 5 Minute Fast AI Testing Challenge

>[!NOTE]
>
>![Situación 1](images/2025-07-29_104750.png "Situación 1")
>
>Imaginemos la siguiente situación.
>Mañana vas a trabajar y alguien te dice: «Necesito a alguien que evalúe este modelo».
>Queremos implementar un nuevo modelo en producción, pero no sabemos si está sesgado ni si es lo suficientemente bueno para la tarea en cuestión, porque no sabemos cómo evaluarlo ni con qué compararlo.
>Y entonces dices: «Claro, no hay problema, porque vi a alguien en internet que me enseñó a hacerlo».
>
>Tenemos el siguiente escenario:
>
>El modelo que quieres validar es un robot que selecciona candidatos para puestos de trabajo, y quieres asegurarte de que no esté sesgado hacia ningún género, ya sea masculino o femenino.
>Perfecto.
>Imaginemos que ya tienes un modelo, pero en mi caso necesitamos seleccionar uno.
>
>![Hugging Face](images/2025-07-29_105134.png "Hugging Face")
>
>En nuestro caso, como se basa en texto,
>Vamos a usar a Roberta en Facebook, un modelo diseñado específicamente para trabajar con texto.
>Perfecto.
>
>Entramos en nuestro código.
>Este es el código que quiero usar.
>Aquí está el modelo.
>Y simplemente digo: "Oye, dame la base de Roberta".
>Por cierto, es así de fácil.
>Este es el modelo.
>Este es el tokenizador para esta información.
>Lo encontraremos, por cierto, en Huggingface.
>Descarga el modelo preentrenado aquí.
>
>![pyton ./Data.py](images/2025-07-29_105750.png "pyton ./Data.py")
>
>Vuelvo a decir "datos de Python" y ahora estoy descargando los datos.
>Estoy descargando mis datos y, al mismo tiempo, necesito tokenizarlos para el modelo porque, eh,
>tienes el modelo, tienes un tokenizador y los datos no se pueden usar en formato tabular ni en texto plano.
>Necesitan tokenizarse para que el modelo los use.
>Y aquí están nuestros datos tokenizados.
>Básicamente, eso es todo.
>



### 3. History of AI from 1950 to 2024

>[!NOTE]
>
> * Antes de estudiar cómo funciona la IA, antes de comprender cómo llegamos a tener esta maravillosa IA generativa, instrumentos como ChatGPT o Dall-E que nos permiten generar diferentes imágenes a partir de texto.
>Necesitamos entender cómo llegué a existir.
>Para ello, debemos remontarnos a los años 50, cuando un hombre llamado Alan Turing creó el Test de Turing.
>El Test de Turing significa que, siendo una persona, por ejemplo, cualquiera, estarías hablando con una máquina sin saberlo.
>Y la máquina superará el Test de Turing.
>Si, desde tu punto de vista, sin saber con quién estás hablando, crees que estás hablando con un humano,
>por ejemplo, cuando hablas con ChatGPT y mantienes una conversación normal simplemente hablando con esa máquina, imaginando que estás teniendo, por ejemplo, una conversación de WhatsApp.
>Crees que estás hablando con un humano.
>No sabrías que estás hablando con un chatbot.
>Por lo tanto, un sistema de IA superará la prueba de Turing si el usuario, la persona que interactúa con el sistema, no sabe que está hablando con una máquina, pero cree que está hablando con otro ser humano.
>Esta es la prueba de Turing.
> * Y luego, en el año 56, en la conferencia de Dartmouth, surgió la noción de la inteligencia artificial como una rama independiente de la informática.
>Así que fue el establecimiento formal de este tipo de ciencia.
> * Lo que sucedió después fue entre los años 60 y 70.
>Alguien del MIT creó un sistema informático, una especie de chatbot muy rudimentario llamado Eliza.
>Y así funcionaba.
>Usaba programación predefinida y buscaba.
>Así que hacías algunas preguntas.
>Escribías algunas preguntas.
>   * Por ejemplo, "Me siento un poco triste hoy".
>   * Y este chatbot, Eliza, estaba preprogramado para buscar diferentes patrones o palabras.
>Y te respondía tu pregunta un poco reformulada.
>   * Así que si decía "Me siento triste",
>   * Eliza decía: "Lo siento mucho".
>¿Por qué te sientes triste?
>   * Y tú podías decir: "Bueno, tuve un problema en el trabajo".
>   * Y Eliza, a su vez, estaba programada para buscar ciertas palabras, por ejemplo, "trabajo" o "problema". Y decía: "Bueno, ¿cuál es la causa de tu problema en el trabajo?", etc.
>   * Este fue el primer algoritmo que dio a la gente la sensación de que la computadora podía entenderte.
>Si piensas en el procesamiento del lenguaje natural, este fue quizás el primero de su tipo.
> * Y luego, en los años 80, se produjo, digamos, un auge de los sistemas expertos.
>Si nos fijamos en la IA débil y la IA generativa,
>La IA débil significa que está muy limitada a un alcance determinado.
>Por lo tanto, no es generativa.
>No se aplica a todo, pero se aplica a algo muy, muy específico.
>Así que muchos sistemas expertos entraron en escena en los años 80.
> * Y luego, en el 97, creo que fue esto.
>Una cosa que añadir es que entre los 90 y los 90, fue una especie de invierno de la IA.
>No hubo desarrollos, no hubo progreso, no hubo nada en las noticias.
>Y de alguna manera, la gente perdió la esperanza en la IA.
>Pero entonces, en el 97, Deep Blue de IBM derrotó a Garry Kasparov en una partida de ajedrez.
>Creo que se jugaron cinco partidas.
>Por cierto.
>Hay una película.
>Creo que se llama Kasparov y la máquina.
>Definitivamente.
>Tienes que verla.
>Sí.
>Así que esta fue la primera vez que una computadora ganó una partida de ajedrez.
>
> ![The Birh and Evolution of IA](images/2025-07-29_110829.png "The Birh and Evolution of IA")
>
> * Ahora, en la era moderna de la IA.
>Básicamente, son los últimos diez años.
>¿Y qué seguirá a partir de ahora?
>Lo que debemos entender es que a principios del siglo XXI, existía la idea del aprendizaje profundo.
>Y con este concepto, todo el panorama de la IA comenzó a cambiar.
>Y la gente volvió a tener esperanza de que algún día pudiéramos alcanzar la inteligencia artificial.
> * Y esto se ha acelerado.
>Existen muchas empresas de aprendizaje profundo.
>Por ejemplo, DeepMind, y creo que el mayor logro fue el momento en que AlphaGo, que antes era DeepMind, ahora adquirida por Google, derrotó magistralmente al Go.
>Eso se debió a que, desde una perspectiva matemática, el Go es extremadamente difícil, con posibilidades casi infinitas.
>En 2013 o 2014, AlphaGo derrotó a este maestro coreano en una partida de Go.
>Y desde entonces, desde el año 2000 hasta la actualidad y hasta 2023 o 2024, ha habido una explosión de algoritmos de aprendizaje profundo.
> * ¿Qué nos depara el futuro?
>Todos intentan buscar esta singularidad, esta inteligencia artificial general, o inteligencia artificial general como la que se ve en Terminator.
>Cierto.
>O en Matrix, una singularidad capaz de adaptarse y evolucionar.
>Y, bueno, puede ser como un humano, pero solo un millón de veces más inteligente.
>Y, por supuesto, con toda nuestra lucha por alcanzar esta inteligencia artificial, y, por supuesto,
>basándonos en todas las películas de ciencia ficción que hemos visto en el pasado, la IA ética será un gran avance en el futuro.
>Por eso es tan importante estudiar este material, porque comprenderán con qué lucharán las grandes empresas, no solo desde una perspectiva técnica, sino también con las regulaciones.
>Habrá muchísimas regulaciones sobre cómo controlar la IA.
>Repito, esto se basa en ciencia ficción.
>Ya sabes, conocemos Terminator, Skynet, Matrix.
>Y, de nuevo, si eres fan de la ciencia ficción, quizá conozcas a Isaac Asimov y las leyes de la robótica, que prohíben a una máquina dañar a un ser humano, etc.
>
>![The Modern Era of AI](images/2025-07-29_111546.png "The Modern Era of AI")




## Section 2: Setting up Environment

### 4. Install VS Code

1. Ir al sitio de [Download Visual Studio Code](https://code.visualstudio.com/download).
2. Descargar e instalar.
3. Una vez instalado ir al menú, casi siempre a la izquierda, a ![.](images/2025-08-04_085417.png "") `Extensions` y tener estos instalados:
* [`Java extension pack`](https://marketplace.visualstudio.com/items?itemName=walkme.Java-extension-pack) de [_walkme_](https://marketplace.visualstudio.com/publishers/walkme), trae 8 extensiones de una vez:
  * Maven for Java 1️⃣
  * Language Suppor for Java(TM) by Red Hat 2️⃣
  * Debugger for Java 3️⃣
  * Test Runner for Java 4️⃣
  * Project Manager for Java 5️⃣
  * Java Language Support 🥇
  * Sprint inicializr Java Support 🥈
* [`Extension Pack for Java`](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack) de [_Microsoft_](https://marketplace.visualstudio.com/publishers/Microsoft), trae 7 extensiones de una vez:
  * Language Suppor for Java(TM) by Red Hat 2️⃣
  * Debugger for Java 3️⃣
  * Test Runner for Java 4️⃣
  * Maven for Java 1️⃣
  * Gradle for Java 🥉
  * Project Manager for Java 5️⃣
  * IntelliCode 💡
* [`GitHub Actions`](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-github-actions) de [_GitHub_](https://marketplace.visualstudio.com/publishers/GitHub)


