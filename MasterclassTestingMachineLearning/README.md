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


