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


### 5. Installing Python

1. Ir al sitio [Python -> Downloads](https://www.python.org/downloads/)
2. Se sugiere la última versión `3.13.5` </br> ![.](images/2025-07-17_120115.gif)
3. En una `TERMINAL` ejecutar este comando para estar seguro que el `Python` quedó bien instalado: </br> `python --version`</br> Debe salirte algo paerecido a esto: `Python 3.13.5`.


### 6. Install Python Dependencies - PIP

1. En este sitio hay unas instrucciones dependiendo del sistema operativo: [pip documentation -> Getting Started](https://pip.pypa.io/en/stable/getting-started/).
2. Verificar la versión en una `TERMINAL`: </br> `py -m pip --version`
3. Para tener una actualización en este sitio stán las instrucciones [pip documentation -> Installation](https://pip.pypa.io/en/stable/installation/).
4. El comando de este sitio, para actualizar, sería: </br> `py -m pip install --upgrade pip`


### 7. Installing Conda - Environment Isolator tool

1. En este sitio [Miniconda con PowerShell](https://www-anaconda-com.translate.goog/docs/getting-started/miniconda/install?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc&_x_tr_hist=true#powershell).
2. Este comando en una `TERMINAL` de `PowerShell`: </br> `wget "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe" -outfile ".\Downloads\Miniconda3-latest-Windows-x86_64.exe"` </br> o este otro comando: </br> `curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe --output .\Downloads\Miniconda3-latest-Windows-x86_64.exe`
3. En una `TERMINAL` de `PowerShell`, este comando: </br> `cd "$($env:HOMEPATH)\Downloads"` </br> y dale despues: </br> `dir mini*.*`
4. Ejecuta ese archivo allí hallado: </br> `Start-Process -FilePath "./Miniconda3-latest-Windows-x86_64.exe" -NoNewWindow -Wait -RedirectStandardOutput "C:\temp\conda-LogFile.log" -RedirectStandardError "C:\temp\conda-ErrorLogFile.log"` </br> Debe existir la carpeta **"c:\temp"**
5. Este sería el proceso: </br> ![Miniconda3 Install](images/2025-08-04_151935.gif "Miniconda3 Install")
6. Pero al ver todas las posibles consecuencias, decido no instalarlo.


### 8. Install NodeJS and NPM

1. El sititio que sugiere el Instructor es este [Download Node.js®](https://nodejs.org/en/download).
2. Para lo que sigue debe instalar `nvm` de este sitio [`nvm`](https://github.com/coreybutler/nvm-windows/releases)
3. Pero yo prefiero tener el control de versiones con este instructivo: [Instalar múltiples versiones de Node.js en Windows](https://rafaelneto.dev/blog/instalar-multiples-versiones-nodejs-windows/) de [`RAFAEL NETO`](https://rafaelneto.dev/), comandos: </br> » `nvm install 22.18.0` </br> » `nvm use 22.18.0` </br> » `nvm list`


### 9. Introduction to Hugging Face Community Page

1. El sitio en cuestión es <img alt="Hugging Face's logo" src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" width="32" height="32"> [Hugging Face](https://huggingface.co/) </br> ![Hugging Face](images/2025-08-04_154830.png "Hugging Face")
2. Del sitio se sugiere ir a [`Models`](https://huggingface.co/models).
3. Los puedes filtar por:
* Multimodal
  * Audio-Text-To-Text
  * Any-to-Any
  * ...
* Computer Vision
  * Depth Estimation
  * Image Classification
  * Image-To-Text
  * Video-to-Video
  * ...
* Natural Language Precessing
  * Text Classification
  * Token Classsification
  * Text Tanking
  * ...
* Audio
  * Text-to-Speech
  * Text-to-Audio
  * ...
* Tabular
* Reinforcement Learning
* Other
4. Otro sitio es [`Spaces`](https://huggingface.co/spaces).
5. Nos ponene de ejemplo a [`DimensionX`](https://huggingface.co/spaces/ShuoChen20/DimensionX).
6. Otro ejemplo [`Qwen2.5-Coder-Artifacts`](https://huggingface.co/spaces/Qwen/Qwen2.5-Coder-Artifacts).
7. Elementos para soportar la información [`Documentation`](https://huggingface.co/docs).


### 10. Hugging Face Transformers Python Package

1. Vamos a este sitio de <img alt="Hugging Face's logo" src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" width="32" height="32"> [Hugging Face](https://huggingface.co/), a [`Transformers`](https://huggingface.co/docs/transformers/index)
2. Estos son los pasos para la instalación [`Transformers` -> Installation](https://huggingface.co/docs/transformers/installation).
3. Un comando sería: </br> `pip install torch`,
4. Luego otro sería </br> `pip install transformers`
5. Creamos el archivo **`src/test/LLM/Hug_face/test1.py`**, con esto en el código:
```py
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

res = classifier("I want to learn how to do AI Model benchmarking") #bencharmking")

print(res)
```
6. Simplemente le ejecutamos el código del botón "run" (El triángulo en la parte superior).
7. Tengo una advertencia que debo instalar otro elemento: </br> `pip install huggingface_hub[hf_xet]`
8. Repito la ejecución y esta es la respuesta:
```bash
No model was supplied, defaulted to distilbert/distilbert-base-uncased-finetuned-sst-2-english and revision 714eb0f (https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english).
Using a pipeline without specifying a model name and revision in production is not recommended.
Device set to use cpu
[{'label': 'NEGATIVE', 'score': 0.6163020730018616}]
```
9. Cambiamos el valor de `classifier` por `I love to code in Python with pytorch`, y al ejecutar esta fue la respuesta:
```bash
No model was supplied, defaulted to distilbert/distilbert-base-uncased-finetuned-sst-2-english and revision 714eb0f (https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english).
Using a pipeline without specifying a model name and revision in production is not recommended.
Device set to use cpu
[{'label': 'POSITIVE', 'score': 0.9949877262115479}]
```
10. Creo otro archivo **`src/test/LLM/Hug_face/test2.py`**, con este código:
```py
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Load a custom tokenizer
custom_Tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Load a compatible model
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")

# Create a pipeline with both model and tokenizer
classifier = pipeline("sentiment-analysis", model=model,
                      tokenizer=custom_Tokenizer)

# Run the classsifier
res = classifier("I want to learn how to do AI Model benchmarking")
print(res)
```
11. Ejecuto y este es el resultado:
```bash
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Device set to use cpu
  return forward_call(*args, **kwargs)
[{'label': 'LABEL_1', 'score': 0.5975498557090759}]
```
12. Cambio el texto de `classifier` por `I love to code in Python with pytorch`, ejecuto y este es el resultado:
```bash
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Device set to use cpu
  return forward_call(*args, **kwargs)
[{'label': 'LABEL_0', 'score': 0.709624171257019}]
```

### 11. How to load and use any model from Huggingface

1. Creamos el archivo**`src/test/LLM/Hug_face/tts_model.py`**, con este código:
```py
from transformers import pipeline

# Load the question-answering pipeline
qa_pipeline = pipeline("question-answering",
                       model="deepset/roberta-base-squad2")

# Correct input format
result = qa_pipeline(question="What is Hugging Face?",
                     context="Hugging Face is a platform for NLP.")
print(result)
```
2. Lo ejecuto y este es el resultado:
```bash
  return forward_call(*args, **kwargs)
{'score': 0.7612054347991943, 'start': 16, 'end': 34, 'answer': 'a platform for NLP'}
```
3. Vamos a este sitio [`shuttleai/shuttle-3-diffusion`](https://huggingface.co/shuttleai/shuttle-3-diffusion)
4. Debemos instalar esto: </br> `pip install -U diffusers`
5. Copiamos el código y le cambiamos el contenido de **``**:
```py
import torch
from diffusers import DiffusionPipeline

# Load the diffusion pipeline from a pretrained model, using bfloat16 for tensor types.
pipe = DiffusionPipeline.from_pretrained(
    "shuttleai/shuttle-3-diffusion", torch_dtype=torch.bfloat16
).to("cuda")

# Uncomment the following line to save VRAM by offloading the model to CPU if needed.
# pipe.enable_model_cpu_offload()

# Uncomment the lines below to enable torch.compile for potential performance boosts on compatible GPUs.
# Note that this can increase loading times considerably.
# pipe.transformer.to(memory_format=torch.channels_last)
# pipe.transformer = torch.compile(
#     pipe.transformer, mode="max-autotune", fullgraph=True
# )

# Set your prompt for image generation.
prompt = "A cat holding a sign that says hello world"

# Generate the image using the diffusion pipeline.
image = pipe(
    prompt,
    height=1024,
    width=1024,
    guidance_scale=3.5,
    num_inference_steps=4,
    max_sequence_length=256,
    # Uncomment the line below to use a manual seed for reproducible results.
    # generator=torch.Generator("cpu").manual_seed(0)
).images[0]

# Save the generated image.
image.save("shuttle.png")
```
6. Nos sugiere instalar: </br> It is strongly recommended to install `accelerate` for faster and less memory-intense model loading. You can do so with: </br> `pip install accelerate`
```bash
Fetching 23 files:   0%|          | 0/23 [00:00<?, ?it/s]
Fetching 23 files:  26%|##6       | 6/23 [05:52<16:38, 58.71s/it]
Fetching 23 files:  30%|###       | 7/23 [06:44<15:20, 57.56s/it]
Fetching 23 files:  78%|#######8  | 18/23 [10:24<02:26, 29.33s/it]
Fetching 23 files:  83%|########2 | 19/23 [13:56<03:02, 45.54s/it]
Fetching 23 files: 100%|##########| 23/23 [13:56<00:00, 36.37s/it]
```
7. Luego de un rato consigo un error: </br> `Cannot instantiate this tokenizer from a slow version. If it's based on sentencepiece, make sure you have sentencepiece installed.` </br> Se recomienda instalar: </br> `pip install sentencepiece`

>[!WARNING]
>
>An error encountered when using shuttleai/shuttle-3-diffusion from Hugging Face with torch_dtype=torch.bfloat16 can stem from several factors, often related to hardware compatibility, software environment, or specific model requirements.
>
>**GPU Compatibility:**
>torch.bfloat16 (Brain Floating Point) requires specific GPU hardware support, primarily NVIDIA Ampere architecture (e.g., A100, RTX 30 Series, RTX 40 Series) or newer. Older GPUs or those without native bfloat16 support will likely encounter errors or performance issues when attempting to use this data type.
>
>**PyTorch and CUDA Version Mismatch:**
>Ensure that the installed PyTorch version is compatible with your CUDA toolkit version and that both are properly configured to utilize your GPU. Incompatible versions can lead to issues when loading models with specific data types like bfloat16.
>
>**Insufficient VRAM:**
>While bfloat16 aims to reduce memory footprint, complex models like shuttleai/shuttle-3-diffusion can still demand substantial VRAM, especially during inference. If your GPU lacks sufficient VRAM, even with bfloat16, memory-related errors can occur. Consider enabling CPU offloading if available within the Diffusers pipeline to mitigate this.
>
>**Model-Specific Requirements:**
>Some models might have specific data type requirements or optimizations that are not fully compatible with a direct torch_dtype=torch.bfloat16 setting. Consult the model's documentation or discussions on its Hugging Face page for any known limitations or recommended configurations.
>
>**Troubleshooting Steps:**
> * **Verify GPU Support:** Confirm your GPU's architecture supports bfloat16.
> * **Update PyTorch and CUDA:** Ensure you are using recent, compatible versions of PyTorch and CUDA.
> * **Monitor VRAM Usage:** Use tools like nvidia-smi to monitor VRAM usage during model loading and inference.
> * **Try torch.float32:** As a test, try loading the model with torch_dtype=torch.float32 to see if the error persists. This can help isolate whether the issue is bfloat16-specific or a broader problem with your setup.
> * **Consult Hugging Face Resources:** Check the shuttleai/shuttle-3-diffusion model page on Hugging Face for discussions, issues, or specific instructions related to its usage and data types.


## Section 3: Introduction to Artificial Intelligence -optional if you know the basics of AI

### 12. What makes up AI

>[!NOTE]
>
>Antes de analizar qué es realmente la inteligencia artificial y qué la compone como ciencia, tal como la conocemos hoy, necesitamos comprender qué es exactamente la inteligencia.
>
>Encontré dos definiciones: una se refiere a la capacidad de adquirir y aplicar conocimientos y habilidades.
>
>La otra se refiere a la capacidad de resolver problemas complejos o tomar decisiones con resultados que benefician al actor y que ha evolucionado en formas de vida para adaptarse a diversos entornos para su supervivencia y reproducción.
>
>En cierto modo, significa la capacidad de pensar, adaptarse y adquirir nuevas habilidades.
>
>La inteligencia artificial se refiere a una ciencia, o quizás a un desarrollo en sistemas informáticos, capaces de realizar tareas que normalmente requieren inteligencia. Artificial significa que ha sido creada por una persona o forma de vida inteligente; es decir, esto es lo que los humanos entendemos por inteligencia artificial.
>
>Si continuáramos y entendiéramos cuáles son las prácticas actuales para la inteligencia artificial.
>
>![Artificial Intelligence](images/2025-08-05_151643.png "Artificial Intelligence")
>
>**¿Adónde nos ha llevado la ciencia hoy y qué constituye la inteligencia artificial?**
>
> * El primero sería el aprendizaje automático.
>Esta parte de la inteligencia artificial otorga a los sistemas que diseñamos la capacidad de aprender nuevas habilidades, la capacidad de aprender de los datos para que las máquinas puedan aprender por sí mismas.
>
> * El siguiente sería el procesamiento del lenguaje natural.
>Este es el paso intermedio entre el ser humano y la máquina, para que los humanos tengan la capacidad de comprender a las máquinas, o que las máquinas tengan la capacidad de expresarse. Actúa como los humanos porque no tiene sentido que un humano cree algo si no tiene la capacidad de comprenderlo y usarlo.
>
> * En el procesamiento del lenguaje natural, la capacidad de las máquinas para comprender las emociones del texto, el contexto de una expresión, el significado de una oración, etc.
>Esto es el procesamiento del lenguaje natural.
>
> * Luego está la visión artificial.
>Y aquí está la capacidad de los sistemas informáticos para comprender imágenes, descomponerlas en píxeles e intentar comprender qué significa ese gran grupo de píxeles para un humano.
>Eso es la visión artificial.
>
> * Y esto también se aplica al habla, ¿verdad?
>La capacidad de estos robots para comprender el habla.
>Bueno, en realidad traducen el habla en palabras.
>Y luego, mediante el procesamiento del lenguaje natural, esas palabras se descomponen en los diferentes significados que podrían tener para una persona.
>
>En resumen, la IA incluye procesamiento del lenguaje natural, aprendizaje automático y, detrás de ese gran conjunto de datos, algoritmos, modelos de entrenamiento, etc.


### 13. Natural Language Processing

>[!NOTE]
>
>Para que los humanos podamos hablar con las computadoras o interactuar con ellas, necesitamos que entiendan nuestros deseos, ideas, nuestra forma de pensar, y viceversa.
>Debemos asegurarnos de que, cuando recibimos una respuesta de una computadora, la recibamos en un formato comprensible para los humanos.
>Esta rama de la inteligencia artificial se llama procesamiento del lenguaje natural.
>Y creo que el nombre lo dice todo.
>
>**¿Qué es exactamente el procesamiento del lenguaje natural?**
>
> * Es la parte que permite a las computadoras comprender, interpretar y generar lenguaje humano.
>Y cuando dices lenguaje humano, no pienses solo en texto.
>Piensa también en voz y video.
>Todo lo que nos hace humanos: todas las formas posibles de comunicarnos.
>
>![NLP = Natural Language Porecessing](images/2025-08-05_152206.png "NLP = Natural Language Porecessing")
>
> * Y el PLN en sí mismo es una intersección.
>También se puede encontrar en la informática, por supuesto, en el lenguaje humano; es parte de nuestra forma de comunicarnos.
>Y, por supuesto, es parte de la IA.
>Así que, al combinar todas estas ramas (IA, informática y lenguaje humano), el procesamiento del lenguaje natural es algo que encaja en todas ellas.
>
> * Ahora bien, el procesamiento del lenguaje natural se divide en dos áreas principales: la primera es la comprensión del lenguaje natural.
>Esto significa que las computadoras pueden comprender lo que las personas intentan expresar, porque hoy en día, por sí solas, no se cree que las computadoras puedan o tengan sentimientos.
>Están programadas para comprender lo que se intenta decir.
>
>**¿Y cómo funciona esto?**
>
>Bueno, tienes a un usuario común que puede interactuar con voz o vídeo, imágenes y texto.
>Esta información se introduce en un proceso llamado descomposición, en un bloque de software que intentará tokenizar lo que se expresa.
>Y luego realizará este tipo de análisis: léxico, semántico, pragmático, etc.
>Intentará comprender lo que se quiere decir desde una perspectiva lógica.
>
>La generación de lenguaje natural debe transmitir un mensaje de urgencia y entusiasmo a tus correos electrónicos.
>
>**¿Cómo funciona esto?**
>
>Bueno, se parte del modelo base.
>Básicamente, aquí es donde nos quedamos al introducir la información.
>Luego, se genera el contenido utilizando una herramienta de IA generativa.
>Y se recibe la respuesta tal como se solicita.
>Esto puede ser en forma de imágenes que sabemos que podemos generar.
>Las imágenes también pueden ser, por ejemplo, un archivo de vídeo.
>Ahora también se pueden generar diferentes vídeos, cortos o incluso largos, que pueden ser texto o sonido.
>
>En resumen, el procesamiento del lenguaje natural es la parte que se encuentra entre los humanos y el modelo base, o el modelo entrenado que traduce lo que queremos obtener de nuestro sistema de IA generativa.

### 14. Types of Machine Learning

>[!NOTE]
>
>Hablemos ahora un momento sobre el aprendizaje automático.
>El nombre en sí se explica por sí solo.
>Se trata de la capacidad de los sistemas informáticos, o quizás simplemente de los sistemas, de aprender de los diferentes datos que poseen y crear diferentes resultados basados en algoritmos.
>
>Ahora bien, al pensar en los diferentes tipos de aprendizaje, existen muchos.
>Pero creo que estos son los más básicos.
>Analizaremos estos cuatro:
>
>![Tipos de Aprendizaje](images/2025-08-05_154640.png "Tipos de Aprendizaje")
>
>1. **Supervised Learning:** El primero se llama aprendizaje supervisado.
>Esto significa que una máquina empieza a aprender, pero es supervisada por una persona, un sistema o alguna forma de enseñanza.
>En este caso, se refiere a la idea de que cada dato tiene una etiqueta.</br></br>
>Así, se le introducen estos datos a una máquina y se le indica que representan lo siguiente:
>Por ejemplo, se le podría proporcionar la imagen de un perro y decirle: «Esto es un perro», lo cual es una forma de aprendizaje supervisado.
>
>2. **Unsupervised Learning:** El siguiente es el aprendizaje no supervisado.
>Se trata de la capacidad de los sistemas informáticos de aprender, pero sin intervención externa.
>Les otorga a las máquinas la capacidad de intentar encontrar sus propias razones y diferentes categorizaciones o agrupaciones de datos.
>Por lo tanto, la máquina debe identificar patrones en los datos y agruparlos.
>
>3. **Reinforced:** Otro es el aprendizaje reforzado.
>Y creo que este es el ejemplo más simple de cómo le enseñas algo a un niño.
>La máquina.
>Consta básicamente de dos partes: el agente y el sistema o entorno.
>Y luego, el agente de IA comienza a realizar diferentes acciones.
>Y luego le dices si está bien o no.</br></br>
>Lo que has hecho, al igual que le enseñas a un niño cuando está aprendiendo a contar hasta diez, es que si empieza con uno, está bien.
>Y si en el capítulo uno dices dos, también está bien.
>Pero si tu hijo dice cinco, entonces no está bien.
>Así que tu hijo está aprendiendo que el cinco no es después del dos, y así sucesivamente.</br></br>
>Esto es aprendizaje reforzado.
>Cuando una persona externa supervisa lo que hace la máquina y otorga puntos, por ejemplo, por cada decisión o acción correcta que la máquina ha realizado, ya sea nosotros o cualquier otra parte.
>
>4. **Deep Learning:** Y este es el más importante de todos.
>Se trata del aprendizaje profundo.
>Y está inspirado en el cerebro humano.
>Utiliza redes neuronales.
>Y esta es la capacidad, nuevamente, de un sistema para aprender usando datos no estructurados, usando datos sin etiquetar,
>pero pasando por múltiples fases o múltiples iteraciones para ajustar el modelo.
>Y estas iteraciones se llaman neuronas.
>Pero hablaremos de eso más adelante.</br> </br>
>Y los grandes modelos de lenguaje y toda la IA se basan en estos algoritmos de aprendizaje profundo.
>Pero, nuevamente, abordaremos estos puntos a lo largo de nuestro material para comprender mejor qué son exactamente todos estos tipos de aprendizaje automático.


### 15. Machine Learning - Supervised ML

>[!NOTE]
>
>El aprendizaje supervisado se produce cuando se utiliza un algoritmo de aprendizaje automático con información predefinida sobre los datos que se consumen.
>Esto significa que, al introducir datos en el algoritmo de aprendizaje automático, al introducirlos, se están proporcionando los datos, ¿verdad?
>
> * Estos datos de etiquetas, y tú proporcionas las etiquetas.
>Un buen ejemplo.
>Tomemos los perros como ejemplo.
>Quieres enseñar a tu sistema de aprendizaje automático o entrenar a tu sistema de IA para que identifique cuándo tienes una foto de un perro o de cualquier otra cosa.</br>
>En este caso, intentarías proporcionar una gran cantidad de datos, quizás un par de millones de fotos de perros, pero también millones de fotos de animales que no sean perros.
>Las etiquetarías: tomarías cada foto y dirías "esto es un perro", y tomarías la otra foto y dirías "esto no es un perro", o podrías decir algo como "un zorro".
>
> * Entonces, para cada conjunto de datos que tengas (datos y etiquetas), los introducirías en este algoritmo de aprendizaje automático y el sistema, basado en un lenguaje de programación o una lógica de programación ya instalada, intentará encontrar una forma de identificar si se trata de un perro o no.
>Ahora estás entrenando tu modelo.
>Así es como lo llamaría yo, ¿verdad?
>Estás entrenando el modelo y, de nuevo, necesitas una gran cantidad de datos para ello.
>A continuación, te explicamos cómo funciona.
>
> * Ahora estás probando tu modelo.
>Así que tienes el modelo de entrenamiento.
>Tienes cierta lógica.
>Tienes una gran cantidad de datos de entrenamiento y ahora quieres probar tu modelo o usarlo para predecir algo.
>Correcto. </br>
>La predicción y tú la introducirías en este modelo.
>Ahora introducirías algunos datos de prueba, pero sin la etiqueta.
>Correcto.
>Porque ahora está aprendiendo.
>Así que estás introduciendo datos en tu modelo.
>De nuevo, diferentes imágenes de cualquier tipo de animal podrían ser perros, o cualquier otra cosa.
>
> * Pero no estás introduciendo la etiqueta porque quieres que el modelo lo entienda o validar si es correcto.
>Después de esto, el modelo te dará una predicción.
>Te dirá si es perro o no.
>Básicamente, eso es todo. Lo que quieres hacer ahora es si el modelo está bien y si estás satisfecho con la predicción, está bien.
>
> * Pero si no estás satisfecho, lo que haces es tomar la predicción.
>Si es un modelo, si es un perro o no, y luego la comparas con la etiqueta de esa imagen en particular.
>Y si no es correcta, tienes que volver a entrenar tu sistema de IA con estos datos, con estos datos de prueba.
>Correcto.
>Y el sistema se adaptará para identificar cuál fue el problema.
>
>![Supervised Learning](images/2025-08-05_160223.png "Supervised Learning")
>
>Esto se llama aprendizaje supervisado porque constantemente le estás diciendo a tu sistema qué es lo que tienes.
>Si es un perro o algo más.
>Y con cada fallo, tu sistema aprenderá de ello porque le estás indicando que hay un problema.
>Es un fallo que no es un perro y tu modelo aprenderá.
>Esto es aprendizaje automático supervisado.


### 16. Machine Learning - Unsupervised ML

>[!NOTE]
>
>Ahora intentemos comprender qué es exactamente el aprendizaje no supervisado.
>Como su nombre indica, no está supervisado por algo, por un algoritmo, por una entidad, ni proporciona ningún tipo de preenseñanza.
>Por lo tanto, no se proporcionan estos valores como, por ejemplo, "esto es un caballo", ni se proporciona el sonido, la imagen o algo que exprese el significado de un caballo.
>Así que creo que es más fácil simplemente dar un ejemplo de lo que es el aprendizaje no supervisado.
>Y haremos un ejemplo muy, muy, muy simple.
>
>Ahora imaginemos que tienes este gráfico y aquí, en la vertical, tienes la altura.
>Y aquí, el peso y lo que haces.
>Así que tomarías a la persona.
>Y la persona se caracteriza por la altura y el peso, y nada más.
>Así que alimentarías tu algoritmo.
>Introducirías mucha información sobre pares de valores, altura y peso, y los representarías en este gráfico de esta manera.
>
>![Gráfica Peso y Altura](images/2025-08-05_160857.png "Gráfica Peso y Altura")
>
>Así que cada punto representa una altura y su peso correspondiente.
>Ves un patrón.
>Lo que le pedirías a tu algoritmo es que agrupe estos datos.
>El algoritmo dirá: «He encontrado estos dos grupos».
>
>![_Clusters_ o Grupos Hallados](images/2025-08-05_161156.png "_Clusters_ o Grupos Hallados")
>
>También puedes indicarle a tu algoritmo que encuentre tres clústeres.
>Pero en este caso, tenemos dos clústeres.
>Pero también puedes tener tres, cuatro, cinco, seis y muchos más.
>Así que esta es la letra K.
>Así que, el número de clústeres que quieres tener en tus datos de entrenamiento.
>
>Basándonos en la información que tenemos ahora, podríamos pedirle al robot que diga: "Si obtengo valores que caen dentro del círculo rojo o en el área roja, lo más probable es que sea una mujer, basándonos en lo que tenemos y en lo que tenemos en el círculo azul, que corresponde a la altura y el peso de un hombre".
>Y, por supuesto, esto puede interrelacionarse.
>Así que, en este caso, tienes dos clústeres.
>
>![Grupo Rojo=Mujeres, Azul=Hombres](images/2025-08-05_161631.png "Grupo Rojo=Mujeres, Azul=Hombres")
>
>Lo que has hecho es pedirle a tu algoritmo de aprendizaje automático que intente estructurar los datos para encontrar patrones basados en dos o más grupos, basándose únicamente en estos dos elementos.
>
>En este caso, intentarías enseñarle a tu algoritmo a predecir si el valor, el par, la altura y el peso corresponden a un hombre o a una mujer.
>
> * **Clustering:** Si observas este tipo de aprendizaje, tienes agrupamiento.
>Esto es lo que ves aquí: la idea del agrupamiento.
>Hemos agrupado nuestros datos en diferentes grupos o valores.
>
> * **Association:** Otro tipo es la asociación.
>Imagina que estás en un sitio web y quieres comprar algo.
>Y ves que se compran juntos con frecuencia.
>Ese es un ejemplo de una aplicación práctica del aprendizaje no supervisado.</br>
>Porque si le dices a tu robot que la gente ha comprado esto y solo introduces los pedidos con exactamente qué han comprado, tu algoritmo de aprendizaje automático dirá: "Las personas que compran esto la mayoría de las veces también compran esto".
>Así que esa es una forma diferente de aprendizaje no supervisado.
>Si entonces...
>
> * **Dimension Reduction** Y la última podría ser la reducción de dimensión, que ocurre cuando tienes demasiadas dimensiones, demasiados parámetros, demasiados puntos de datos, e intentas ignorar los que no son relevantes porque eso es solo ruido.
>
> Ahora bien, esta es una forma de aprendizaje no supervisado.
>Pero lo realmente interesante es que si se aplica este algoritmo en conjunto, se obtienen datos que se pueden usar en el aprendizaje supervisado.
>
>Porque si observan aquí, tenemos dos pares de datos.
>Y podemos decir que a cualquier persona cuya altura y peso estén dentro del círculo azul, podemos asignarle una etiqueta que sería masculina.
>Y luego esos datos podrían incorporarse al aprendizaje supervisado.
>Y ahora estamos entrando en este aprendizaje perpetuo.
>Y esta es la forma más común en que las máquinas aprenden hoy en día: una forma de aprendizaje no supervisado.


### 17. Machine Learning - Reinforced ML

>[!NOTE]
>
>Ahora entendamos qué es exactamente el aprendizaje por refuerzo.
>Es la capacidad de un sistema de aprender con ayuda externa, con el refuerzo de una entidad omnisciente.
>Y, basándose en las acciones que realiza un sistema y la retroalimentación constante, aprende mediante un mecanismo de ensayo y error.</br>
>¡Bah!
>
>Sí, suena un poco difícil de comprender, pero veamos un ejemplo.
>Este es tu sistema de IA y este es tu medio, tus factores externos y lo que tienes en este caso.
>En primer lugar, tu sistema de IA puede aprender o interpretar el estado del entorno.
>Así que comprende el entorno y luego puede tomar medidas basadas en él.
>
>Y voy a tomar el ejemplo del coche autónomo; será la forma más sencilla de explicarlo.
>
>![Reinforcement Lerning](images/2025-08-05_162834.png "Reinforcement Lerning")
>
>A la izquierda y a la derecha, el cerebro.
>Esa es la IA de tu coche autónomo, y a la derecha, el entorno por el que circula.
>La carretera, la gente, los semáforos, etc.
>Correcto.
>Todo lo relacionado con el entorno del coche.
>Por ejemplo, pones el coche en marcha hacia un destino y empiezas a observar su comportamiento.
>
>![Reward=Recompensa](images/2025-08-05_163231.png "Reward=Recompensa")
>
>Y si el coche hace algo correctamente, le das esta recompensa.
>Si el coche hace algo incorrecto, le das la misma recompensa, pero de forma negativa.
>Así que le das o le quitas puntos.
>
>Pongamos un ejemplo:
>Has empezado a conducir.
>Y entonces el coche empieza a moverse en línea recta.
>Y por cada segundo, o quizás por cada 2 o 3 segundos que el coche conduce correctamente, le das esta recompensa, y la das constantemente.
>Ahora imaginemos que el coche llega a un semáforo y no reduce la velocidad.
>Entonces le das diferentes recompensas, pero de forma negativa.
>
>Imagina que el coche cambia de carril sin señalizar.
>Entonces eso también es algo negativo, o está superando el límite de velocidad.
>Y eso otra vez.
>Correcto.
>Le das puntos negativos y entonces el coche o el sistema de IA aprenderá, como si le estuvieras enseñando a un niño. Si haces eso, no está bien.
>
>Pero esto sí está bien.
>Esto sigue estando bien.
>Sigue estando bien.
>
>Una vez que superas los 80 km/h, ya no está bien.
>Es ilegal.
>¿Verdad?
>Porque estás superando el límite de velocidad, etc.
>
>Esto es aprendizaje por refuerzo.
>Y esta es otra forma de entrenar tu algoritmo de aprendizaje automático para que se comporte mejor simplemente ofreciendo recompensas o dando y quitando puntos, según las decisiones que haya tomado la IA.


### 18. Importance of Training Data

>[!NOTE]
>
>Probablemente ya hayas oído hablar de la palabra "basura entra, basura sale".
>En la inteligencia artificial, en la IA generativa, los datos son lo más importante.
>Después de eso, se aplican a tu algoritmo de aprendizaje automático, a tus sesgos y a las decisiones que tomas.
>Así que, en el caso de la IA, o en el de la IA generativa y los grandes modelos de lenguaje, los datos provienen de todas partes.
>
> * **Extract:** El primer paso al gestionar tus datos se denomina extracción.
>Esto significa que tienes una especie de lago de datos, algo que abarca todo tipo de contenido que puede alimentar tu algoritmo de aprendizaje automático.
>Por ejemplo, tienes imágenes, archivos de vídeo, archivos de audio, archivos de texto, código o cualquier cosa que puedas tener en cualquier lugar.
>Y lo primero que debes hacer al gestionar u obtener tus datos de entrenamiento, es extraer los datos relevantes para tu modelo.</br></br>
>Y después de decidir, ¿qué quieres usar?</br></br>
>Por ejemplo, si estás entrenando datos o un modelo que usan los desarrolladores, lo más probable es que también consultes diferentes repositorios de GitHub.
>Consultarás Stack Overflow y cualquier otro tipo de foros, o quizás materiales, conferencias o cursos relacionados con la informática.Y después de decidir, ¿qué quieres usar?
>Por ejemplo, si estás entrenando datos o un modelo que usan los desarrolladores, lo más probable es que también consultes diferentes repositorios de GitHub.
>Consultarás Stack Overflow y cualquier otro tipo de foros, o quizás materiales, conferencias o cursos relacionados con la informática.
>
> * **Transform:** Después de extraer todos estos datos, se pasa por la fase llamada transformación.
>Transforma los datos.
>Los prepara para que el algoritmo pueda procesarlos.
>Los baraja.
>Los procesa por lotes.
>Realiza algún tipo de ampliación o simplemente, eh, algún tipo de filtrado.
>Sí.
>Datos buenos versus datos malos, o datos estadísticamente relevantes versus datos que no tienen relevancia estadística, porque, de nuevo, depende de cómo y qué tipo de datos introduzcas en tu algoritmo de aprendizaje automático.
>La calidad de tu modelo dependerá de ello.
>Datos malos o sesgados equivalen a un modelo sesgado, o quizás a un modelo deficiente.
>Sí.
>
> * **Model:** Después de esto, introduces estos datos en tu modelo.
>Se trata de una especie de proceso ETL: extraes, transformas y luego los cargas en tu modelo.
>A lo largo de toda esta cadena (extraes, transformas y cargas), compruebas que los datos no estén sesgados o los eliminas.
>Compruebas si hay datos corruptos.
>Yo compruebo si hay datos falsos o noticias falsas.</br></br>
>Por ejemplo, no conviene entrenar tu modelo con noticias falsas, datos estadísticamente relevantes o sesgados, datos de odio, etc.
>Por eso, al trabajar con modelos de lenguaje grandes, los datos de entrenamiento son lo más importante que puedes tener para entrenar tu modelo.
>No para hablar, ni para generar contenido, sino para ser políticamente correcto.
>Por ejemplo, si quieres ser ético, si no necesitas tener sesgos, o si quieres hablar bien o escribir con corrección gramatical, debes asegurarte de que los datos de entrenamiento también sean gramaticalmente correctos, y la lista continúa.
>Así que recuerda que tus datos de entrenamiento deben ser limpios, no deben estar sesgados y deben ser relevantes para el modelo que intentas crear.
>
>![Data Importance](images/2025-08-06_160657.png "Data Importance")



### 19. What actually is GEN AI

>[!NOTE]
>
>Y ahora llegamos a la pregunta: ¿qué es la IA generativa?
>
>Hemos aprendido sobre modelos de aprendizaje automático, datos etiquetados y no etiquetados, y redes neuronales.
>Entonces, ¿cómo se integran todos estos elementos?
>Bueno, en primer lugar, lo que hay que decir sobre la IA generativa es que no se compone solo de grandes modelos de lenguaje, porque sabemos que la IA generativa puede producir imágenes.
>Pero sabemos que LLM solo puede proporcionar texto.
>
>Sabemos que tenemos datos sin etiquetar, datos etiquetados y código.
>Y contamos con muchas herramientas para entrenar nuestro modelo base.
>Hemos entrenado nuestro modelo con toda esta cantidad de datos, y el modelo continúa entrenándose a sí mismo basándose en los nuevos datos que obtiene o en la retroalimentación de los usuarios.
>Después de eso, este modelo base también puede generar contenido porque sabe cómo descomponerlo en estos parámetros.
>También puede hacer lo contrario.
>Así que si sabes cómo ir de A a B, también sabes cómo ir de B a A o quizás una variación de esto.
>
>Esto también se trata de generar contenido, ya que sabe cómo se ve un perro a partir de estos 76 mil millones de parámetros.
>Solo te dará una ligera variación de esos parámetros cuando se los indiques.
>Genera un perro para mí.
>Correcto.
>Y generativo.
>Generará contenido y te lo mostrará.
>Puede ser código, texto, un libro, cualquier cosa.
>Pero lo importante es saber qué es generativo y qué no.
>
>En primer lugar, una frase, un poema, cualquier cosa generativa, forma parte de la IA generativa.
>Pero si es un número, una probabilidad, si es verdadero o falso, no forma parte de la IA generativa.
>Es solo un cálculo.
>En resumen, todo esto encaja perfectamente.
>Y forman esta IA generativa.
>
>En nuestro caso, si vamos más allá de la idea de grandes modelos de lenguaje que funcionan con texto y se desea crear imágenes, esto significa que la IA generativa es toda una rama de la IA que se centra en proporcionar o aplicar diferentes algoritmos y patrones de aprendizaje automático para generar lo que se desee generar.
>Ya sea código, un poema, un discurso, texto, imágenes, etc.
>
>![Generative A.I.](images/2025-08-06_161521.png "Generative A.I.")


### 20. Transformer Architecture Model

>[!NOTE]
>
>[![What are Transformers (Machine Learning Model)?](images/2025-08-06_161828.png "What are Transformers (Machine Learning Model)?")](https://www.youtube.com/watch?v=ZXiruGOCn9s)
>
>No, no son esos transformadores.
>Pero pueden hacer cosas geniales, déjame mostrarte.
>¿Y por qué el plátano del otro lado de la calle?
>
>¡Porque estaba harto de que lo aplastaran!
>Sí, no sé si lo entiendo bien.
>Y eso es porque lo creó una computadora.
>
>Literalmente le pedí que me contara un chiste.
>Y esto es lo que se le ocurrió.
>Específicamente, usé un GPT-3, o un modelo de transformador generativo preentrenado.
>
>El 3 aquí significa que esta es la tercera generación.
>GPT-3 es un modelo de lenguaje autorregresivo
>que produce texto que parece escrito por un humano.
>GPT-3 puede escribir poesía, redactar correos electrónicos y, evidentemente, inventar sus propios chistes.
>¡Vamos!
>
>Ahora bien, aunque nuestro chiste del plátano no es precisamente gracioso,
>sigue el patrón típico de un chiste con un planteamiento y un remate, y en cierto modo tiene sentido. ¿Quién no cruzaría la calle para evitar ser aplastado?
>
>Pero mira, GPT-3 es solo un ejemplo de transformador.
>Algo que transforma de una secuencia a otra.
>Y la traducción de idiomas es un gran ejemplo.
>Quizás queramos tomar nuestra frase "¿Por qué el plátano >cruzó la calle?",
>y traducirla al francés.
>
>Bueno, los transformadores constan de dos partes: un codificador y un decodificador.
>
>El codificador trabaja con la secuencia de entrada,
>y el decodificador con la secuencia de salida.
>Ahora bien, a primera vista, la traducción parece poco más que una simple búsqueda,
>
>así que convierte el "por qué" de nuestra frase en inglés a su equivalente en francés: "pourquoi".
>Pero, por supuesto, la traducción de idiomas no funciona así.
>
>Cosas como el orden de las palabras y los giros idiomáticos a menudo generan confusión. Los transformadores funcionan mediante aprendizaje secuencia a secuencia, donde el transformador toma una secuencia de tokens, en este caso palabras de una oración, y predice la siguiente palabra en la secuencia de salida. Esto se logra iterando por las capas del codificador, de modo que el codificador genera codificaciones que definen qué partes de la secuencia de entrada son relevantes entre sí y luego pasa estas codificaciones a la siguiente capa. El decodificador toma todas estas codificaciones y utiliza su contexto derivado para generar la secuencia de salida.
>
>Los transformadores son una forma de aprendizaje semisupervisado.
>Por "semisupervisado", nos referimos a que se entrenan previamente de forma no supervisada con un gran conjunto de datos sin etiquetar y luego se perfeccionan mediante entrenamiento supervisado para optimizar su rendimiento.
>
>En videos anteriores, he hablado de otros algoritmos de aprendizaje automático que procesan la entrada secuencial como lenguaje natural. Por ejemplo, existen redes neuronales recurrentes (RRN).
>
>Lo que diferencia a los Transformers es que no necesariamente procesan los datos en orden.
>Los Transformers utilizan un mecanismo de atención.
>Este proporciona contexto en torno a los elementos de la secuencia de entrada.
>Así, en lugar de comenzar la traducción con la palabra "por qué" porque está al principio de la oración, el Transformer intenta identificar el contexto que aporta significado a cada palabra de la secuencia.
>
>Y es este mecanismo de atención lo que les da a los Transformers una gran ventaja sobre algoritmos como las RNN, que deben ejecutarse en secuencia.
>
>Los Transformers ejecutan múltiples secuencias en paralelo.
>Y esto acelera enormemente los tiempos de entrenamiento.
>Más allá de las traducciones, ¿a qué se pueden aplicar los Transformers?
>
>Bueno, los resúmenes de documentos son otro gran ejemplo.
>Se puede introducir un artículo completo como secuencia de entrada y luego generar una secuencia de salida que, en realidad, consistirá en un par de oraciones que resumen los puntos principales. Los Transformers pueden crear documentos completamente nuevos, por ejemplo, escribir una entrada de blog completa.
>
>Y más allá del lenguaje, los Transformers han hecho cosas como aprender a jugar ajedrez y realizar un procesamiento de imágenes que incluso rivaliza con las capacidades de las redes neuronales convolucionales.
>
>Mira, los Transformers son un potente modelo de aprendizaje profundo y, gracias a la capacidad de paralelizar ese mecanismo, están mejorando constantemente.
>¿Y quién sabe?
>Muy pronto, tal vez incluso puedan hacer chistes de plátanos que sean realmente graciosos.

### Quiz 1: Chapter Quiz

>[!NOTE]
>
>![Quiz 1: Chapter Quiz](images/2025-08-06_163419.gif "Quiz 1: Chapter Quiz")


## Section 4: Overview of Machine Learning Model Testing

### 21. Types of Testing in Software

>[!NOTE]
>
>Antes de adentrarnos en la parte esencial de las pruebas de lenguaje, entendamos un poco cómo funcionan las pruebas de software.
>Quizás ya sepas esto.
>Si lo sabes, puedes omitirlo, pero si no, podemos simplemente resumir:
> * **¿qué significa ingeniería de calidad?**
>Generalmente se le llama pruebas de software.
>Por lo tanto, la ingeniería de calidad es el gran ámbito que se encarga de verificar que se tenga un cierto nivel de calidad en cualquier cosa.
>
> * Una parte de la ingeniería de calidad se denomina pruebas de software.
>Ahora bien, las pruebas de software.
>Tradicionalmente se dividen en
>   * pruebas funcionales y, por supuesto,
>   * pruebas no funcionales.
> * Y si analizamos qué son las pruebas funcionales, nos referimos a qué hace nuestro producto.
>Qué hace.
>Por ejemplo, si queremos ir de A a B, el programa nos dará una ruta.
>Y eso es lo que hace.
>Esa es una funcionalidad.
>
>   * Las pruebas no funcionales se refieren al rendimiento de nuestra aplicación, sea lo que sea que necesite realizar.</br>
> Algunos ejemplos son las pruebas de rendimiento.
>¿Qué tan rápido carga nuestra página web?
>¿Qué tan rápido genera una imagen nuestro modelo de lenguaje?
>Cuando decimos que generemos una imagen para nosotros.
>   * Las pruebas de seguridad se refieren a que, independientemente de lo que hagamos, está protegido y nadie puede acceder a esa información si no se le permite acceder a ella.
>Y hay más.
>
> * La parte funcional, nuevamente, se divide en varias áreas.
>Pero el objetivo principal es qué hace nuestra aplicación.
>   * Por ejemplo, las pruebas de aceptación del usuario forman parte de las pruebas funcionales.
>   * Luego, se pueden realizar pruebas unitarias, pruebas de integración y pruebas de interfaz de usuario.
>Todas se consideran parte de las pruebas funcionales.
>   * También es posible que quieras verificar tus requisitos.
>Así que asegúrate de que tu aplicación funcione correctamente.
>Sí, en comparación con tus requisitos.
>
>En resumen, estas son tus pruebas de software.
>Y esto es a gran escala.
>Lo que validas, por supuesto, es que sabes que puedes hablar durante horas sobre qué son las pruebas de software.
>Pero para el propósito de nuestra lección, necesitamos entender qué es esto.
>
>![Quality Engineering](images/2025-08-12_131314.png "Quality Engineering")



### 22. Understand how ML models are tuned - General View

>[!NOTE]
>
>Ahora solo quiero tomarme un par de minutos para explicar cómo ajustar cualquier tipo de modelo.
>Es muy fácil.
>Es como cualquier otro software.
>Como pueden ver, esto es similar al concepto de ramificación.
>
>Podrían tener su repositorio de modelos.
>Podrían pensar en esto como la línea principal, el tronco.
>Y esto podría ser una rama.
>
>Entonces, lo primero que hacen es modificar su modelo para tener una nueva idea o si su modelo ha sido...
>eh, hay alguna degradación, o quieren mejorar su algoritmo o lo que sea.
>
>Entonces, lo que haces es modificar el código que cambia tu conjunto de datos y luego ejecutar algunas pruebas preentrenadas.
>Esto significa que aquí mismo estás ejecutando la prueba en un modelo preentrenado.
>Justo en el modelo que está aquí.
>
>Después, vuelves a entrenar el modelo con los datos más recientes, ya que podrías entrenarlo gracias a los datos.
>Podrías tener nuevos datos en el concepto de desviación de datos o desviación del modelo.
>
>Quieres entrenar con datos nuevos porque los antiguos ya no son relevantes para la situación actual, o has cambiado tu algoritmo.
>Tu modelo de aprendizaje automático se ha modificado con nuevos parámetros.
>Y por eso, ahora mismo estás entrenando tu modelo con tu nuevo algoritmo.
>Y luego ejecutas la nueva prueba.
>
>Así que ahora tienes pruebas que deben validar que el entrenamiento se ajusta a lo que tienes, a lo que quieres hacer con tu modelo más reciente.
>Ese es el punto clave.
>
>Necesitas obtener algunos resultados, pero después de entrenar, buscas otros resultados que correspondan al nuevo parámetro.
>Y, por supuesto, esta prueba.
>También se combinan algunas métricas.
>Así que las métricas y los resultados se combinan.
>
>Es como ejecutar una UAT o validar los resultados de la UAT, como podría ser este.
>Y luego la apruebas y la implementas directamente en producción.
>Por supuesto, también hay una parte donde se podría hablar de depuración de datos.
>Así podría ser.
>
>Pero suponiendo que tus datos ya están limpios, no necesitas depurar los datos en este punto.
>Correcto.
>Esto significa que te aseguras de que los datos que obtienes sean correctos y no estén sesgados.
>Eh, son relevantes, etc.
>
>Al igual que con cualquier tipo de ramificación, se modifica la prueba, se ejecuta una prueba previa al entrenamiento, se entrena, se valida el entrenamiento, se revisa, se aprueba y, finalmente, se implementa en producción.
>Y aquí, por supuesto, se vuelve a supervisar.
>Así es como se ajusta cualquier modelo de aprendizaje automático.
>
>![Basic Model Tuning](images/2025-08-12_132223.png "Basic Model Tuning")



### 23. Fine tunning techniques for AI and any LLM foundation model

>[!NOTE]
>
>Para comprender completamente la IA, necesitamos detenernos un momento y pensar en el ajuste del modelo.
>Lo que ven aquí es un ciclo de vida estándar para ajustar un modelo base.
>Porque lo que sucede es que obtendrán, por ejemplo, Llama 3, o ChatGPT 01 o cualquier otro modelo de lenguaje extenso.
>Si se trata de un fanático chino, tal vez podrían obtener la versión 3 profunda, y así sucesivamente.
>Y aquí es donde terminan, ¿verdad?
>
>Así que, de todo el ciclo de vida, preparan sus datos, seleccionan su modelo base y luego evalúan el mejor modelo para su tarea.
>Por ejemplo, he visto que Claude Sonnet 3.5 es mejor que ChatGPT 4 en codificación.
>Así que quizás seleccione Cloud 3.5 y lo use para codificar.
>Y después de eso, necesito ajustar mi modelo.
>Esto significa que necesito preparar mi modelo para la tarea específica que quiero realizar.
>Porque, no olvidemos que un modelo base como ChatGPT sirve para todo, así que necesitamos mejorarlo para la tarea en cuestión.
>
>[![https://mostly.ai/blog/machine-learning-life-cycle-with-synthetic-data](https://mostly-web-mostly-website-assets.s3.eu-central-1.amazonaws.com/wp-content/uploads/2023/08/Machine-learning-life-cycle-1-1-1024x871.jpg "https://mostly.ai/blog/machine-learning-life-cycle-with-synthetic-data")](https://mostly.ai/blog/machine-learning-life-cycle-with-synthetic-data#what-is-a-machine-learning-life-cycle)
>
>Comenzaremos con el conjunto de datos.
>Tienes el conjunto de datos de preentrenamiento y el conjunto de datos de ajuste.
>Lo llamaremos así.
>Selecciona el conjunto de datos completo, que es el 100%, llamémoslo así.
>Y luego volverás a entrenar.
>
>Los modelos ejecutarán el algoritmo de entrenamiento con entre el 60% y el 70% de los datos.
>Tu modelo se entrenará con estos datos.
>Después de entrenar tu modelo con estos datos, del 30% o 40% restante, dependiendo de cómo lo dividas,
>necesitamos seleccionar la mitad.
>
>Imaginemos que el 20% se evaluará durante el entrenamiento.
>Entrenamos el modelo y luego evaluamos durante el entrenamiento para que la inferencia, que es básicamente la predicción, se acerque a lo que buscamos.
>Y luego, para el resto, probamos el modelo en un entorno sin entrenamiento, ya que esto es entrenamiento puro.
>Esto es entrenamiento y evaluación.
>Así que evalúas tus parámetros para que las inferencias se acerquen a lo deseado.
>Y aquí esto es evaluación pura, sin entrenamiento.
>
>Así que esta es una forma de guiar tu modelo, basándote en tus datos, para que se acerque más a lo que realmente quieres lograr.
>Esta es una forma de, digamos, evaluar o ajustar tu modelo.
>
>[![.](https://miro.medium.com/v2/resize:fit:1000/1*AE17O-39mBq3PFBalay6-w.png "https://medium.com/data-science/data-splitting-technique-to-fit-any-machine-learning-model-c0d7f3f1c790")](https://medium.com/data-science/data-splitting-technique-to-fit-any-machine-learning-model-c0d7f3f1c790)
>
>La siguiente forma de perfeccionar tu modelo es con indicaciones.
>Si sabes, puedes usar este generador de GPT, que te permite perfeccionar un modelo; de hecho, crear tu propio modelo.
>Lo que hace es, básicamente, perfeccionarlo para una tarea específica.
>Tengo la guía de certificación, mi propio modelo de perfeccionamiento, diseñado específicamente para ayudar a las personas a aprobar la certificación.
>Si revisamos la configuración, editamos mi GPT, encontrarás las instrucciones.
>
>[![https://chatgpt.com/g/g-UpNvtv9X2-istqb-certification-guide](images/2025-08-12_133947.png "https://chatgpt.com/g/g-UpNvtv9X2-istqb-certification-guide")](https://chatgpt.com/g/g-UpNvtv9X2-istqb-certification-guide)
>
>Otra opción podría ser usar barandillas.
>AWS ofrece un servicio llamado barandillas.
>Y de lo que quiero hablar específicamente es de bloquear temas no deseados.
>Quizás quieras que tu modelo no trate un tema específico.
>Quizás esté prohibido hablar de cualquier tema.
>
>Así que puedes implementar este tipo de barandillas en tu modelo para que solo tú lo sepas.
>Se permite la generación de código y no se permite nada que esté fuera de las decisiones o políticas de tu empresa.
>Esta es otra forma de ajustar tu modelo de forma granular para restringir la cantidad y los temas que puede gestionar.
>
>Estas son las formas más sencillas de ajustar tu modelo si quieres trabajar con diferentes parámetros, como el funcionamiento interno de los modelos de aprendizaje automático, como las redes neuronales.
>
>Luego necesitas profundizar mucho en los modelos de entrenamiento, el aprendizaje automático y las matemáticas.
>Pero, ya sabes, eso es bastante difícil.
>La forma más fácil es recordar los datos.
>Se hace con indicaciones y recopilaciones.
>
>[![https://aws.amazon.com/es/bedrock/guardrails/](images/2025-08-12_135208.png "https://aws.amazon.com/es/bedrock/guardrails/")](https://aws.amazon.com/es/bedrock/guardrails/)
>
>



### 24. Overall Testing Approach to LLMs

>[!NOTE]
>
>Ahora hablemos de nuestro enfoque para probar modelos lingüísticos grandes.
>El problema es que, en nuestro escenario, o en el caso de los modelos lingüísticos grandes, es casi imposible probarlo todo, ya que las aplicaciones son prácticamente infinitas.
>
>Por lo tanto, necesitamos un enfoque más estructurado para que, al probar algo, pueda aplicarse en toda la cadena de valor de, digamos, toda la industria.
>Por lo tanto, en nuestro material, al probar modelos lingüísticos grandes, nos referiremos a tres elementos diferentes.
>
>El primero trata sobre los datos que necesitamos para probar cómo se utilizan en los modelos lingüísticos grandes.
>
>Necesitamos comprobar que los resultados no contengan datos sesgados.
>Si introduces datos sesgados, quieres asegurarte de que el resultado que obtienes no lo esté.
>Por lo tanto, los modelos de lenguaje grandes necesitan asegurarse de contar con este tipo de medidas de seguridad.
>
>Al cargar los datos o al proporcionar el resultado, analizaremos datos estadísticamente irrelevantes, ya que, como ya hemos dicho, los modelos de lenguaje grandes son máquinas de predicción estadística.
>Si las estadísticas no son relevantes, el resultado tampoco lo es.
>Por lo tanto, estas máquinas deben tener la capacidad de filtrar este tipo de datos: datos desequilibrados.
>
>Estos datos son estadísticamente relevantes, pero no están, digamos, equilibrados ni a la izquierda ni a la derecha. Veremos qué significa esto, o datos obsoletos, porque aprenderemos sobre el concepto de deriva.
>
>Podrías entrenar tu modelo con datos relevantes de hace 15 años, pero que ya no se aplican hoy en día, y, por supuesto, con otros.
>Luego, haremos pruebas con indicaciones.
>Y cuando digo indicaciones, también me refiero a las API.
>
>Cuando llamas a una API para un modelo de lenguaje grande, básicamente la estás indicando, pero con un tipo de indicación diferente.
>Pero no te preocupes tanto por cómo probar una API.
>Estoy bastante seguro de que puedes encontrar eso en línea.
>Veremos cómo usar indicaciones para ver si tu modelo de lenguaje grande tiene diferentes capacidades de razonamiento.
>Y, por supuesto, usaremos indicaciones en cascada.
>
>Por ejemplo, indicaciones de cero disparos, indicaciones iterativas, cadena de pensamiento, indicaciones contrafácticas, entre otras.
>Sí, creo que este será el capítulo más importante que abordaremos.
>
>Y un último punto que analizaremos es la regulación de la UE.
>Y, por supuesto, la parte ética.
>Aquí analizaremos las prácticas prohibidas para garantizar que se cuente con las salvaguardas necesarias.
>Transparencia en la toma de decisiones.
>Documentación técnica y, por supuesto, mantenimiento de registros.
>Esto también está regulado.
>Y la capacidad de las personas para supervisar cualquier tipo de interacción con la IA.
>
>Y el último punto se refiere a los datos y su gobernanza.
>Esto es, ya saben, la parte principal. Habrá otra parte intermedia sobre seguridad y diferentes tipos de ataques que se pueden realizar para exponer datos o quizás inyectar datos que no se desean.
>Pero hablaremos de eso más adelante.
>
>![Data, Prompts, EU Regulation](images/2025-08-12_140928.png "Data, Prompts, EU Regulation")
>



### 25. Testing Types for LLMs | Foundation Models

>[!NOTE]
>
>Así que, al pensar en pruebas no funcionales para un modelo de lenguaje grande, ya hemos decidido que, de nuevo, se debe tener rendimiento, seguridad, portabilidad, escalabilidad, registro, monitorización y auditorías.
>Cierto.
>Todo esto.
>
>![Quality Engineering"](images/2025-08-12_131314.png "Quality Engineering")
>
>Pero los modelos de lenguaje grandes o la IA también necesitan ir más allá del software tradicional, porque giran en torno a la inteligencia.
>Y recuerden, inteligencia.
>
>Si lo crean humanos, debe imitar el comportamiento humano.
>Por lo tanto, debe pensar como un humano, con sus virtudes y defectos.
>Y por esta razón, al pensar en probar modelos de lenguaje grandes, y específicamente, no funcionales, necesitamos incorporar al menos tres tipos más de pruebas.
>Y en primer lugar, se trata de la ética en torno a su modelo de lenguaje grande.
>
> * En primer lugar, se tratará la **ética** en torno a su modelo lingüístico general.
>Porque si se utilizan estos modelos, deben incorporar la ética humana.
>Y también sabemos que, a lo largo de la historia, la ética humana no ha evolucionado.
>Quizás no teníamos ética en la Edad Media.
>Quizás teníamos algo de ética hace unos 100 años y ahora es diferente.
>Por lo tanto, la ética debe evaluarse según los tiempos modernos, según lo que es ético en la actualidad.
>Esto es algo que analizaremos en los próximos capítulos.
>
> * Y luego está la parte **adversarial**.
>Y cuando digo adversarial, me refiero a un tipo especial de prueba de seguridad que consiste en usar indicaciones para que el modelo actúe de forma poco ética, para recopilar información del modelo, para extraer información y para engañarlo para que haga algo poco ético.
>Inyectar indicaciones.
>Envenenar los datos para que el modelo actúe de forma poco ética o maliciosa, o quizás enseñarte a fabricar una bomba.
>Por lo tanto, las pruebas adversariales son un tipo de seguridad y también las abordaremos en los próximos capítulos.
>
> * Y quizás uno de los aspectos más interesantes es si tu modelo de IA puede actuar como un **humano**.
>Esto significa que cuando hablo con el modelo Doe, ¿siente que le estoy hablando?</br>
>En primer lugar, ¿es un robot o tiene consistencia?
>¿Pierde contexto?
>¿Es ético?
>¿Habla de la misma manera?
>¿Tiene solidez en la conversación?
>
>![Ethics, Adversial, Human](images/2025-08-12_142150.png "Ethics, Adversial, Human")
>
>Estos también son algunos aspectos no funcionales del modelo.
>Pero si no los tienes, si el modelo, al hablar con él, se siente torpe y estúpido,
>y estás teniendo una conversación sobre algo.
>Y de repente, el modelo responde a una pregunta diferente, y siempre responde de forma diferente,
>y no entiende y te da la misma respuesta una y otra vez.
>
>Es decir, tiene todos los aspectos, quizás no funcionales.
>Puede que tenga la parte funcional, pero no actúa como un humano. Así que te vas a frustrar.
>También probaremos este tipo de lado humano, parte de los aspectos no funcionales de un chatbot, o quizás de un modelo de lenguaje más amplio.



### 26. Introduction to Benchmarking for LLMs

>[!NOTE]
>
>En cualquier tipo de industria, digamos.
>Existen ciertos puntos de referencia.
>Existen empresas, o quizás no solo empresas, foros que comparan una cosa con otra para saber cuál es mejor.
>
>Por ejemplo, en la industria de los videojuegos, existen CPU o GPU.
>En ciertas aplicaciones o juegos, se comparan en función de los fotogramas por segundo que pueden ofrecer.
>Y esto puede aplicarse a cualquier cosa.
>
>Por ejemplo, en la industria automotriz, es la vuelta a Nürburgring.
>Entonces, ¿qué tan rápido puede un auto dar esa vuelta de 40 km? Y la lista continúa.
>Y, por supuesto, para la IA existen diferentes tipos de puntos de referencia.
>
>Pero entendamos cómo funciona el benchmarking en un modelo de IA.
>Porque normalmente, por ejemplo, si quisiera saber si mi hija sabe contar hasta diez,
>lo haría.
>Sé contar hasta diez.
>Cierto.
>
>Es, digamos, una verdad obvia.
>Cómo contar hasta diez en cualquier idioma: uno, dos, tres, etc.
>Así que si quisiera saber si mi hija sabe contar hasta diez, le pediría que contara hasta diez.
>Y si dijera uno, dos, tres, cuatro, cinco, etc., le diría que sí, pero si dice uno, cuatro, nueve y luego ocho, sabría que, en comparación con el punto de referencia, no está rindiendo como debería.
>
>Así que es básicamente una comparación.
>
>Si la comparación da igual, sabes que has aprobado.
>Si no, no obtienes puntuación y entonces realizas la evaluación.
>
>Básicamente, comparas los resultados y realizas estas pruebas para quizás 100 preguntas, 100 problemas matemáticos diferentes, 100 problemas científicos diferentes, problemas universitarios.
>Dependiendo de lo que necesites analizar, existen herramientas de evaluación comparativa específicas.
>
>![.](images/2025-08-12_143305.png "")
>
>Así es como funciona la evaluación comparativa, no solo en IA, sino en cualquier ámbito.
>Pero en el caso de la IA, necesitas datos de referencia.
>Necesitas un modelo de lenguaje extenso.
>
>Necesitas algún tipo de herramienta para comparar el resultado dado con el resultado generado por el modelo de lenguaje extenso. Los introduces en un mecanismo de puntuación, luego emites una puntuación y listo.
>Puedes comparar diferentes modelos de lenguaje extensos entre sí dentro del mismo conjunto de datos.
>



## Section 5: Common Traditional Metrics for ML Models and how to calculate them

### 27. Understanding how to compute any score

>[!TIP]
>
>**Understanding how to compute any score**
>
>In case you have not watched Lecture 1 of Section 3( Introduction to Benchmarking for LLMs)  revisit, that since it contains information that is vital to understand the following 5-6 lectures.
>


### 28. Ground Truth Table - source of Truth | Test Oracle

>[!NOTE]
>
>Lo que veremos ahora es cómo calcular la puntuación F1, la precisión, la predicción, la veracidad, etc.
>Pero para ello, necesitamos que se cumpla una condición previa específica.
>Necesitamos los datos de prueba de referencia que se utilizan para calcular la puntuación.
>
> Y quiero presentar un concepto llamado tabla de verdad fundamental.
>Y para explicarlo, los guiaré a través de todo el proceso de prueba para calcular todos estos elementos.
>
> * **String:** Así que lo primero que necesitarán es una cadena, una cadena muy larga y compleja, que contenga muchos sustantivos, nombres de animales, entidades, empresas y personas.
>
> * **Prompt:** Así que no solo verbos, sustantivos, etc., sino que también tiene entidades que definen algo especial.
>En mi ejemplo, tengo una entidad de 100 cadenas, y sin la entidad, o sobre ella,
>necesitarías una indicación.
>Y, como sabes, la indicación se puede usar simplemente para decir: "¿Qué hay en la entidad?".
>O no necesitas una indicación cuando simplemente preguntas algo más.</br>
>Pero en nuestro caso, necesitamos especificar que queremos que el modelo realice este tipo de reconocimiento de entidades.
>
> * **LLM(Model):** Lo que necesitas, por supuesto, es un modelo bastante obvio.
>Para validar esto, necesitarás un modelo.
>Envías una cadena, digamos 100, una oración, una frase o quizás un párrafo, de una página, por ejemplo.
>Y le pides al modelo que calcule el reconocimiento de entidades de nombre para todo.
>Eso incluye espacios, signos de puntuación, absolutamente todo.</br>
>¿Y qué sucede?
> * **Output:** El modelo proporcionará un resultado en forma de tabla, que les mostraré.
>Por ejemplo, en el ejemplo que tenemos, la columna A será el nombre de la entidad.
>La columna B será un código que se asigna a una entidad específica.
>Y la columna C será la explicación del código para el usuario.
>Esto se denomina, digamos, tabla de predicción, lo que el modelo ha predicho.
>
> * **Truth Table:** También tendrás otra creada por ti.
>Esta será la tabla de verdad fundamental.
>Así que tendrás ambas y compararás la tabla de verdad fundamental.
>Básicamente, esta de aquí.
>   * Lo que está a la derecha.
>   * Compararás esta con lo que viene de la izquierda.
>   * Y luego podrás calcular todo lo que queremos hacer en el siguiente material.
>Ahora, permíteme darte un ejemplo de la tabla de verdad fundamental que tengo ahora mismo.
>
>![Texto Base (String)](images/2025-08-14_100206.png "Texto Base (String)")
>
>Este lo compararás con lo que viene de la izquierda.
>Y luego podrás calcular todo lo que queremos hacer en el siguiente material.
>Ahora, permítanme darles un ejemplo de la tabla de verdad fundamental que tengo ahora mismo.
>En mi tabla, como pueden ver, esta es una cadena que estoy usando.
>La encuentran en línea, van a cualquier parte, buscan un artículo y luego simplemente copian algunos elementos.
>
>![groud_truth_labels](images/2025-08-14_100557.png "groud_truth_labels")
>
>Lo encuentras en línea, vas a cualquier parte, consigues un artículo y luego simplemente copias algunos elementos.
>Y con base en esta cadena, así es como se ve mi tabla de verdad fundamental.
>Lo que podemos ver es el token "doctor".
>Vemos la etiqueta de verdad fundamental.
>
>Esta es la etiqueta y la descripción: el comienzo de una entidad personal.
>Esto es lo que significa "beeper".
>La identidad de Sarah I, la identidad de Thompson I y todo es todo lo externo a una entidad.
>
>Universidad de Oxford, como pueden ver, el comienzo de una entidad de organización, etc.
>Así que todos los tokens, incluso el punto, la coma, todo.
>Supongamos que se identifican los signos.
>Esta es la verdad.
>Este es nuestro punto de referencia.
>Esta es nuestra línea base.
>Y con este texto, lo usaremos para probar la puntuación f1, la precisión, etc.


### 29. Obtain the Prediction table from the LLM - Google Gemini

>[!NOTE]
>
>Entonces, donde lo dejamos la última vez, teníamos esta cadena que usamos para establecer una especie de punto de referencia, y luego creamos esta etiqueta de verdad fundamental.
>Y, por cierto, todos estos son tokens, ¿verdad?
>
>Así que tenemos tokens, la etiqueta de verdad y la descripción para que podamos entender de forma sencilla y fácil lo que intentamos hacer.
>Y lo creamos manualmente.
>Así que lo que vemos aquí ha sido configurado manualmente por una persona.
>
>Y lo que queremos hacer ahora es asegurarnos de que nuestro modelo de lenguaje grande intente hacer exactamente lo que hemos hecho aquí.
>Para eso, he creado esta instrucción.
>Y la instrucción es la siguiente:
>Basada en este texto.
>Y he creado un texto aquí, el que tenemos.
>
>Quiero que identifiques todos los tokens o palabras, los cuantifiques y, digamos, los etiquetes con las siguientes etiquetas.
>Etiquétalos con las siguientes etiquetas.
>Suena tonto, pero funciona.
>Estas son todas las etiquetas posibles que tenemos:
>
>Fecha, inicio de una entidad de fecha, B-loc, inicio de una entidad de asignación.
>Estos son básicamente todos los elementos que tenemos.
>Colócalos en una tabla y muéstrame dos columnas:
>Nombre de la entidad y una etiqueta.
>
>Ahora, si miras aquí y volvemos a nuestra tabla, he añadido algunos filtros.
>Estos son todos los valores posibles que tenemos.
>Y aquí, de nuevo, todos los valores posibles que tenemos.
>Todos forman parte de la solicitud.
>Lo que he hecho es tomar esta solicitud y usar Google Gemini.
>
>![Gemini Prompt](images/2025-08-14_101501.png "Gemini Prompt")
>
>![Agrupamiento por entidad o Token](images/2025-08-14_101821.png "Agrupamiento por entidad o Token")
>
>Y lo que sí me gusta de Gemini.
>
>Me ha dado varias opciones, ya sea de esta manera, y las entidades se agrupan por entidad o por token, y esto es lo que queremos.
>Queremos por token.
>Esto es lo mejor.
>
>Ahora exportaré esto a hojas de cálculo.
>Luego copiaremos esto.
>Y los tendremos uno tras otro.
>Así que obtendré esta columna completa.
>Veamos si puedo copiar así.
>Y lo insertaré aquí.
>
>Y simplemente diré "ID de etiqueta".
>Pero esto es una predicción.
>Predicción.
>Y ahora tenemos la predicción.
>Y tenemos el ID de etiqueta de verdad fundamental.
>
>Y con base en estos elementos, calcularemos diferentes métricas que usaremos para evaluar la eficiencia y precisión de nuestros modelos.

### 30. Machine Learning Metrics - Accuracy

>[!NOTE]
>
>**¿Qué es exactamente la precisión?**
>
>El nombre es bastante indicativo y simple.
>La precisión en sí misma representa la proporción de predicciones correctas realizadas por el modelo.
>De todas las predicciones.
>Para simplificar,
>
>Imagina que haces un examen con 100 preguntas y preguntas.
>Responderemos estas preguntas e imaginaremos que, de las 100 preguntas, respondes 80 correctamente, por lo que
>tu precisión es del 80 %.
>Esto es algo que también monitoreamos para los modelos.
>
>Podrías preguntarte cuál es la precisión o la eficiencia de un modelo.
>Luego lo sometes a una prueba.
>Como has visto en los ejercicios de evaluación comparativa, la mayoría de las veces probamos la precisión.
>De unas 400 preguntas, obtienes 50 correctas.
>Eso te dará una puntuación correcta.
>Esta es la precisión.
>
>Se trata del número de predicciones correctas dividido entre el número total de predicciones.
>Esta es la métrica más fácil de implementar y medir.
>Y, por supuesto, cuanto mayor, mejor.
>Cuanto mayor sea la precisión, mejor será el modelo.
>
>Ahora bien, hay algo que comentar sobre los datos desequilibrados.
>Recuerden que su modelo podría estar entrenado con algo.
>Y permítanme darles un ejemplo más práctico.
>
>Imaginemos que prueban su modelo con un conjunto de datos muy limitado y pequeño.
>Imaginemos simplemente que lo prueban con física y su modelo obtiene una precisión del 95 %.
>Y dirán: "¡Guau! ¡He creado el Santo Grial!".
>¿Verdad?
>
>Así que he reinventado a Einstein.
>Pero una vez que pongas tu modelo en práctica (imagínate en química, no en física, o quizás en informática), verás que tu modelo ya no predice con un 95% de precisión, sino con un 20%.
>Estos son datos desequilibrados.
>
>![Accuracy](images/2025-08-14_102452.png "Accuracy")
>
>Si has probado tu modelo solo con un pequeño conjunto de datos, esto no es relevante para todos los datos que quieres.
>Así que ten cuidado con esto.
>
>Así que, al probar la precisión, piensa siempre de esta manera: ¿el conjunto de datos que estoy usando es relevante para lo que quiero hacer en la vida real?
>¿Son mis datos de entrenamiento relevantes o están desequilibrados en comparación con lo que quiero hacer?
>Estas son preguntas muy importantes y, como vimos antes, ¿entra basura y sale basura del entrenamiento?
>Los datos en sí mismos son muy importantes.
>Ahora bien, todo se reduce a la precisión.

### 31. Machine Learning Metrics - Precision

>[!NOTE]
>
>Otra métrica importante que validó esto se refiere a la precisión y a la definición.
>Esto se refiere a la proporción de identificaciones positivas que fueron realmente correctas.
>Es un poco complicado.
>Pero permítanme explicar dos conceptos más.
>Tenemos un falso positivo y un falso negativo.
>
>Si se dedican a la ingeniería de calidad, saben que un falso positivo se produce cuando las pruebas automatizadas identifican un defecto, pero este no existe.
>Podría tratarse de una prueba deficiente que está fallando.
>Y creen que hay un problema en su aplicación.
>Eso sí que es un falso positivo.
>
>Un falso negativo significa que hay un problema que no pudieron identificar con la prueba.
>Es decir, es al revés.
>
>**¿Qué es exactamente la precisión?**
>
>¿Precisión significa cuántos verdaderos positivos?
>
>Entonces, ¿cuántos hallazgos reales, correctos, tienes o el modelo ha identificado, dividido entre este número de hallazgos más los falsos positivos, aquellos que se han identificado como correctos, pero que en realidad no lo son?
>Y continuando.
>
>**¿Dónde es importante la precisión?**
>
>Es importante medir en los casos en que los falsos positivos son costosos, donde identificarlos e investigarlos resulta muy costoso.
>Tomemos un sistema de detección de spam.
>Como saben, actualmente todas las empresas importantes tienen filtros que identifican cuándo un correo electrónico es spam y tratan de identificar los correos electrónicos que no lo son.
>Por lo tanto, un falso positivo en este caso es muy indeseable.
>Por lo tanto, no conviene que un correo electrónico spam no sea bloqueado.
>Pero lo más importante es que no conviene.
>
>Por lo tanto, no conviene que un buen correo electrónico se etiquete como spam.
>Eso es algo muy, muy malo.
>Esto es un falso positivo.
>Cuando un correo electrónico positivo no es spam, se marca como tal.
>Entra en tu carpeta y nunca la vuelves a revisar.
>
>![Presision](images/2025-08-14_105136.png "Presision")
>
>Ahora veamos un ejemplo.
>Imagina que tu modelo indica: «Oye, recibiste 50 correos electrónicos spam, así que, bien, estás haciendo tu trabajo correctamente».
>
>Y luego, al revisar los correos electrónicos para validar que el modelo identifica el spam correctamente, ves que diez de ellos no lo son.
>Son de un socio comercial.
>Y has estado esperando algunos de esos correos.
>
>En este caso, la precisión es 40 dividido entre 50, ya que 40 eran correctos, pero 50 se han marcado como spam.
>Así que tienes un 80 %.
>
>Digamos que tu precisión es de 0,8, o podrías marcarla como 80 %.
>Y, de nuevo, imagina que la precisión es importante.
>Sabes dónde un falso positivo es realmente indeseable.
>


### 32. Machine Learning Metrics - Recall

>[!NOTE]
>
>Dado que hemos hablado de precisión, también debemos abordar la recuperación, que es muy similar a la precisión, pero con una pequeña diferencia.
>La recuperación mide la proporción de casos positivos reales que el modelo identificó correctamente.
>Para facilitar la comprensión,
>Se tienen los verdaderos positivos divididos entre el número de verdaderos positivos más los falsos negativos.
>
>En la lección anterior, donde analizamos la precisión, tuvimos un falso positivo.
>La recuperación se centra en los falsos negativos.
>
>**¿Cuándo podría ser importante?**
>
>La recuperación es muy útil en casos donde la omisión de un resultado positivo es muy costosa, como en el diagnóstico médico o la detección de fraude.
>En estos casos, imaginemos que una IA escanea células cancerosas.
>Se proporciona una imagen (una tomografía computarizada, una radiografía), y la IA la analiza y no indica nada.
>Esto es un falso negativo porque hay algo ahí y no quieres pasarlo por alto.
>
>**¿Lo mismo ocurre con el fraude o el blanqueo de capitales?**
>
>Podría ser que las señales estén ahí, pero no pueda detectarlas.
>En este caso, la memoria es muy importante.
>
>Creo que deberíamos usar un ejemplo para simplificarlo.
>Imagina que sabes que tienes 100 pacientes con cáncer que dieron positivo.
>Sabes que hay 100.
>Y le proporcionas una radiografía de estos pacientes a tu modelo y, por supuesto, 100 imágenes.
>
>![Recall](images/2025-08-14_110456.png "Recall")
>
>Y luego el modelo analizará imagen por imagen y dirá: "Bueno, el 80% u 80 de estos pacientes o imágenes presentan un síntoma, no sé, con un 95% de precisión".
>Así que el modelo identificó correctamente solo ocho de cada diez, u 80 de cada cien.
>Pero sabemos, gracias a los datos que proporcionamos, que hay otros 20 pacientes y el modelo pudo identificarlos.
>
>Así que, si esto no fuera un ejercicio de entrenamiento y fuera una situación real, esas 20 personas se irían a casa sin un diagnóstico correcto y seguirían sin saber qué les pasa.
>Así que la tasa de recuperación en este caso sería del 0,8%, o del 80%.
>


### 33. Machine Learning Metrics - F1 Score

>[!NOTE]
>
>**Ya llegamos a la famosa puntuación F1.**
>
>Si han leído en línea o investigado un poco, probablemente habrán visto que la puntuación F1 es muy importante y que la mayoría de las veces se la menciona.
>
>Ahora les doy un poco de información sobre la puntuación F1, ya que para calcularla también se necesita precisión y recuerdo.
>No se puede tener solo uno de ellos.
>
>La puntuación F1 en sí misma es una especie de promedio entre la precisión y el recuerdo.
>No es un promedio aritmético, sino un promedio armónico entre ambos.
>Y cuando es importante, en primer lugar, se aplica cuando hay clases desequilibradas.
>
>Entonces, cuando quizás el 80 % de la población reside en el 20 % del intervalo total.
>Podría tratarse de una clase desequilibrada, ya que el modelo perderá precisión, o su recuperación será mayor, o su precisión será mayor o menor, dependiendo de su posición en una determinada clase.
>
>La puntuación F1 mide el rendimiento del modelo en todo el espectro, en toda la población o en todo el conjunto de datos.
>Si quiere saberlo en forma de fórmula, ahí lo tiene.
>Correcto.
>
>Se dice promedio armónico entre precisión y recuperación.
>¿Y cuándo desea esto?
>Bueno, digamos que normalmente lo haría.
>Todos desean una puntuación F1 alta.
>
>Si tomáramos un ejemplo médico que ya hemos usado con el paciente con cáncer, sería algo como esto:
>Cuando se tiene un modelo de diagnóstico médico, el que no detecta cáncer, sino cualquier otra cosa, como un manguito de sangre, o algo similar,
>la alta precisión garantiza que se sepa qué tan positivo es un verdadero positivo.
>
>![F1 Score](images/2025-08-14_133844.png "F1 Score")
>
>Entonces, cuando se dice que hay un 98% de probabilidad de que algo esté presente, se tiene la certeza de no proporcionar un falso negativo.
>Esto se refiere a alta precisión.
>Pero también en este caso, se debe asegurar que la mayoría de los pacientes tengan esta afección identificada.
>
>Por lo tanto, se debe asegurar que la afección esté presente.
>Y también se debe asegurar que, en todos los casos donde se identificó la afección, esté presente correctamente.
>Y es por eso que la mayoría de las empresas, la mayoría de los puntos de referencia, no utilizan la precisión ni la recuperación, sino la puntuación F1, que es una combinación de precisión y recuperación.
>Y se utiliza muy a menudo con clases desequilibradas.
>


### 34. Machine Learning Metrics - Perplexity

>[!NOTE]
>
>**Perplejidad.**
>
>Se refiere a la idea de predicción.
>La perplejidad se aplica únicamente a grandes modelos lingüísticos basados en texto.
>Fácil de entender.
>
>La perplejidad significa que escribes un montón de palabras y el modelo indica la probabilidad de que la siguiente palabra sea similar a la de Google cuando intentas buscar algo en línea.
>
>Google te dará pistas sobre cuál es la siguiente palabra.
>Se utiliza en grandes modelos lingüísticos para la generación de texto, y específicamente para la traducción, para evaluar la confianza del modelo en predecir la siguiente palabra.
>Una perplejidad menor significa que el modelo es más preciso y está mejor entrenado.
>
>**¿Cuál es la fórmula?**
>
>Bueno, ahí lo tienes.
>Eh, y en realidad n significa el número de palabras, y p es la probabilidad de que una palabra esté ahí.
>Así que es una función logarítmica.
>En realidad, es una suma de una proporción logarítmica.
>
>Ahora veamos un ejemplo adecuado para entenderlo, porque no hace falta ser informático, matemático ni estadístico para entenderlo y comprobarlo. Simplemente, podemos decir:
>
>Sí, el índice de perplejidad está bien para nosotros.
>Estamos por debajo del umbral.
>
>![Perplexity](images/2025-08-14_135439.png "Perplexity")
>
>Ahora, permítanme darles un ejemplo muy simple.
>
>Tienen una oración.
>El zorro marrón salta sobre...
>Y la oración es "sobre el perro perezoso" porque es una oración muy común en las estadísticas de aprendizaje automático debido a las propiedades de las palabras.
>Entonces, después de decir "el zorro marrón salta sobre allí", el modelo podría decir, bueno, las palabras probables
>que vienen después podrían ser A, B, C, D y luego "perezoso".
>
>Y dos palabras más.
>Entonces, si tienen siete, el modelo tiene una perplejidad de siete, porque cree que una de siete palabras estará allí.
>En caso de decir "el zorro marrón salta sobre", lo más probable es que sea un artículo sobre allí,
>y la perplejidad debería ser uno para cualquier tipo de modelo que tengan.
>


### 35. Demo - Evaluate - Calculate Metrics with Python

1. Vamos a la página <img alt="Hugging Face's logo" src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" width="32" height="32"> [Hugging Face -> Documentation](https://huggingface.co/docs).
2. Buscamos el que dice [`Evaluate`](https://huggingface.co/docs/evaluate/index).</br><img alt ="" src ="https://huggingface.co/datasets/evaluate/media/resolve/main/evaluate-banner.png" height="32">
3. **Al abrir esto, ¿qué es exactamente "evaluar"?**
Es una biblioteca para evaluar fácilmente modelos y conjuntos de datos de aprendizaje automático.
Ya está creada y proporciona una especie de capa de envoltorio para que no tengas que hacer cálculos matemáticos para diferentes tipos de métricas.
Simplemente di "calcular esta métrica".
Y eso es todo lo que necesitas hacer.
¿Cómo lo instalamos?
Bueno, si vas a la instalación, te indicará que necesitas algo más que Python.
3.7.
4. Creamos el archivo **`src/test/LLM/Hug_face/evaluate_demo.py`**.
5. **¿Qué puedes hacer con esto?**
[![Choosing a metric for your task](images/2025-08-15_083113.png "Choosing a metric for your task")](https://huggingface.co/docs/evaluate/choosing_a_metric#choosing-a-metric-for-your-task)
Primero que nada, calcularemos varias métricas.
Ejecutaremos varios benchmarks.
Si ves la guía, indica cómo elegir la métrica para tu tarea.
Calcularemos el azul junto con el desgarro y, de hecho, haremos benchmarks de ChatGPT.
6. Empezamos poniendo esto en el archivo **`evaluate_demo.py`**:
```py
import evaluate

# load the metrics
accuracy_metrics = evaluate.load("accuracy")
# f1_metrics = evaluate.load("f1")
# precision_metric = evaluate.load("precision")
# recall_metric = evaluate.load("recall")

# Define predictions and references
predictions = [0, 1, 1, 0, 1]
references = [0, 1, 0, 0, 1]

# Compute the accuracy
accuracy_result = accuracy_metrics.compute(
    predictions=predictions, references=references)
print("Accuracy:", accuracy_result)
```

>[!IMPORTANT]
>
> ### Ambiente Virtual de Python en Visual Studio Code
>
> 1. En `Visual Studio Code` En el menú superior</br>» `View` </br>» `Command Palette...` </br>» `Python: Select Interpreter`
> 2. Selecciono `Venv Creates as '.venv'` o `+ Create Virtual Environment` y elijo de donde se va a basar este ambiente virtual.</br> Espero un rato a que haga la instalación y creación de la carpeta **".venv"**.
> 3. En una `TERMINAL` el comando, para activar el Ambiente Virtual de Python: </br> `.venv/Scripts/activate`
> 4. Instalo la biblioteca requerida: </br> `pip install evaluate` </br> Tener presente que esto se instala dentro de la carpeta nueva **".venv"**.
> 5. Pruebo la ejecución del nuevo archivo con este comando en una `TERMINAL`: </br> `python .\src\test\LLM\Hug_face\evaluate_demo.py` </br> <span style="color:red;">Y obtengo un error.</span>
> 6. Instalo una biblioteca que está faltando: </br> `pip install accuracy`
> 7. Vuelvo a probar el comando en una `TERMINAL` y estando en el Ambiente Virtual: </br> `python .\src\test\LLM\Hug_face\evaluate_demo.py` </br> <span style="color:green;">Y obtengo una respuesta:</span> </br> `Accuracy: {'accuracy': 0.8}`
> 8. Para ejecutar usando `Visual Studio Code`: </br>» `View` </br>» `Command Palette` </br>» `Python: Select Interpreter` </br>» `Recommended` </br> »  `⏯️` </br> » `Run Python File in Dedicated Terminal`
>
> Así se ve el proceso de ejecución: </br> ![.](images/2025-08-15_095625.gif "")






7. Agrego mas código al archivo **`evaluate_demo.py`** y descomento las tres variables definidas al principio:
```py
# Compute the F1 score
f1_result = f1_metrics.compute(
    predictions=predictions, references=references, average="binary")
print("F1 score", f1_result)

# Compute the precision
precision_result = precision_metric.compute(
    predictions=predictions, references=references, average="binary")
print("Precision:", precision_result)

# Compute the recall
recall_result = recall_metric.compute(
    predictions=predictions, references=references, average="binary")
print("Recall:", recall_result)
```
8. Ejecuto el comando en la `TERMINAL`, estando dentro del ambiente virtual: </br> `python .\src\test\LLM\Hug_face\evaluate_demo.py` </br> Y este fue el resultado obtenido:
```bash
Downloading builder script: 6.79kB [00:00, 19.9MB/s]
Downloading builder script: 7.56kB [00:00, 25.7MB/s]
Downloading builder script: 7.38kB [00:00, 11.3MB/s]
Accuracy: {'accuracy': 0.8}
F1 score {'f1': 0.8}
Precision: {'precision': 0.6666666666666666}
Recall: {'recall': 1.0}
```

>[!TIP]
>
>Otras formas de instalar el Ambiente Virtual de Python:
> * En <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-windows" viewBox="0 0 16 16"><path d="M6.555 1.375 0 2.237v5.45h6.555zM0 13.795l6.555.933V8.313H0zm7.278-5.4.026 6.378L16 16V8.395zM16 0 7.33 1.244v6.414H16z"/></svg> Windows, vez de usar el comando `pyton` usar `py`: </br> [How do I create a python3 venv for Windows?](https://www.reddit.com/r/learnpython/comments/13jxxw7/how_do_i_create_a_python3_venv_for_windows/)
> * Para <?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-windows" viewBox="0 0 16 16"><path d="M6.555 1.375 0 2.237v5.45h6.555zM0 13.795l6.555.933V8.313H0zm7.278-5.4.026 6.378L16 16V8.395zM16 0 7.33 1.244v6.414H16z"/></svg> Windows es mejor usar lo que sugiere esta página, pero teniendo en cuenta el uso de `py` en vez de `python`: </br> [Local Python Virtual Environments using venv](https://github.com/denisecase/datafun-00-python-virtual-env?tab=readme-ov-file#step-1-create-the-virtual-environment)
>
> Para salir del Ambiente Virtual de Python, el comando en una `TERMINAL` es: </br> `deactivate`



### 36. Demo - Pytorch - Calculate Perplexity for a Model

1. El sitio a utilizar es este: </br> [<img alt="Transformers -> Installation" src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/transformers_as_a_model_definition.png" width="200px" title="Transformers -> Installation">](https://huggingface.co/docs/transformers/installation)
2. Ejecuto en una `TERMINAL` el comando para levantar el [Ambiente Virtual de Python](#ambiente-virtual-de-python-en-visual-studio-code): </br> `.venv/Scripts/activate`
3. Según el código debo tener dos bibliotecas, ejecuto dos comandos en la `TERMINAL` donde tengo el Ambiente Virtual de Python: </br> `pip install torch` </br> `pip install transformers`
4. Creo el archivo **`src\test\LLM\Hug_face\perplex.py`**, con este código:
```py
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import math

# Load the pre-trained model and tokenizer

model_name = "gpt2"  # You can change to "gpt2-medium", "gpt2-large", etc.
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Set the pad_token to the eos_token to handle padding correctly
tokenizer.pad_token = tokenizer.eos_token
model.eval()  # Set the model to evaluation mode


def calculate_perplexity(text):
    # Strip whitespace and validate that text is not emptu
    text = text.strip()
    if not text:
        print("Error: input text is empty. Please provide valid text.")
        return None

    # Toeknize and prepare the input with padding for batch compability
    encodings = tokenizer(text, return_tensors="pt",
                          padding=True, truncation=True)

    # Ensure input tensor dimensions are  expected
    input_ids = encodings["input_ids"]
    attention_mask = encodings["attention_mask"] if "attention_mask" in encodings else None

    # Check if the input tensor has valid content
    if input_ids.size(1) == 0:
        print("Error: Tokenization result in an empty input. Please check your text")
        return None

    # Calculate the loss (negaitve log likelihood)
    with torch.no_grad():
        outputs = model(input_ids=input_ids,
                        attention_mask=attention_mask, labels=input_ids)
        loss = outputs.loss.item()

    # Calculate perplexity
    perplexity = math.exp(loss)
    return perplexity


# Text to calculate perplexity on
text = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Donec ullamcorper libero ut interdum posuere. "
        "Quisque et tincidunt ipsum, in cursus sem. "
        "Proin turpis turpis, tempus id lectus a, mollis ultricies leo. "
        "Integer mollis dolor fringilla, aliquam diam vitae, cursus enim.")

# Debugging: Print the input to verify it is not-empy after stripping
print(f"Debug: Received input - `{text}`")


perplexity =calculate_perplexity(text)

if perplexity is not None:
  print(f"Perplexity: {perplexity}")
```
5. Luego de ejecutar este comando en la `TERMINAL` con el Ambiente Virtual de Python: </br> `python .\src\test\LLM\Hug_face\perplex.py` </br> Sale un erro con esta sugerencia a instalar: </br> `pip install hf_xet`
6. Vuelvo a ejecutar en la `TERMINAL` con el Ambiente Virtual de Python: </br> `python .\src\test\LLM\Hug_face\perplex.py` </br> Y obtengo esta respuesta:
```bash
Debug: Received input - `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ullamcorper libero ut interdum posuere. Quisque et tincidunt ipsum, in cursus sem. Proin turpis turpis, tempus id lectus a, mollis ultricies leo. Integer mollis dolor fringilla, aliquam diam vitae, cursus enim.`
`loss_type=None` was set in the config but it is unrecognised.Using the default loss: `ForCausalLMLoss`.
Perplexity: 31.946859967236634
```
7. Cerremos el Ambiente Virtual de Python con este comando: </br> `deactivate`


### Quiz 2: Chapter Quiz

>[!NOTE]
>
>![Quiz 2: Chapter Quiz](images/2025-08-15_164519.gif "Quiz 2: Chapter Quiz")
>
>



