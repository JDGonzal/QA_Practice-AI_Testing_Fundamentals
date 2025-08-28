# ACCELQ Academy

Most useful courses to develop the skills needed in this new era of QAs in AI.


<https://community.accelq.io/c/learn-to-automate/>

[![Academy ](https://app.circle.so/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCSTkyVHdNPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--169e9630403588aae0ad704f1470b411cedb717b/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNITUdrQ2FBRTZDbk5oZG1WeWV3WTZDbk4wY21sd1ZBPT0iLCJleHAiOm51bGwsInB1ciI6InZhcmlhdGlvbiJ9fQ==--e7ed929538cfb0e8497fbd036110b7591e89532a/240x60-community-logo.png "Academy")](https://community.accelq.io/)

## Section 1: Getting Started - Web Automation

### 1. ▶️ Hello World! Let's Automate our first Scenario!

>[!WARNING]
>
> El ejercicio empieza en este sitio [![ACCELQ -> Autopilot](https://poc.accelq.io/aq_deliverables/client/images/accelq-white-logo.svg "ACCELQ -> Autopilot")](https://poc.accelq.io/), pero infortunadamente no tenemos acceso, así que todo se hará con ejercicios en la imaginación.
>

1. Un escenario en `AccleQ` representa un caso de uso o un proceso de negocio que se intenta automatizar.
2. Aquí tenemos un ejemplo que comienza con:
   * La invocación del navegador
   * El inicio de sesión en el banco
   * El proceso de transferencia de fondos
   * Para transferir fondos al banco
   * Y cerrar sesión.
3. Intentemos crear nuestro primer escenario en un proyecto completamente nuevo.
4. Vamos a la parte izquierda a `Navigator` y luego seleccionamos el tabulador `Scenarios`
5. Clic en el botón `[Create Scenario]`.
6. El nombre es `Validate Login on QBank`.
7. Tenemos dos opciones o: </br> » `Record in Design Studio` </b> o </br> » `➕ Add Step` </br> Seleccionamos la primera `Record in Design Studio`.
8. En la parte superior derecha, en la casilla de `WEB`, ponemos la _URL_ `qbank.accelq.com` </br> ![qbank.accelq.com](images/2025-08-01_090322.png "qbank.accelq.com")
9. Aparece el primer paso: </br> `1️⃣ Invoke Browser (URL: 'qbank.accelq.com')`
10. Hace clic en el cuadro al medio a la derecha con el nombre de `Username` y me aparecen un selector de campos y escojo `enter text in a web input`.
11. Presiono la tecla [`Enter`] y tengo el paso número 2, que debo completar: </br> `2️⃣ Enter text` _in input field whose label (equals, ignore case): 'Username'. Look for the label anyware on page_ </br> Lo completamos con `qbankadmin` y presionamos la tecla [`Enter`].
12. Repetimos haciendo clic en el cuadro al medio a la derecha con el nombre de `Password` y me aparecen un selector de campos y escojo `enter encrypted text in a web input`.
13. Presiono la tecla [`Enter`] y tengo el paso número 3, que debo completar: </br>  `3️⃣ Enter encrypted text` _in input field whose label (equals, ignore case): 'Password'. Look for the label anyware on page_ </br> Lo completamos con `qbTrnPass1&` y presionamos la tecla [`Enter`].
14. Finalmente clic en el botón verde de `[Sign In]` y en el selector escojo `click on a web element`.
15. Presiono la tecla [`Enter`] y tengo el paso número 4, que debo completar: </br>  `4️⃣ Click on text` _(equals, ignore case): 'Sign In'. Look for the clickable text on page_
16. Como se puede ver, estamos grabando estas declaraciones, la declaración es generada y la interacción también está pasando en el cuadro de la derecha: </br> ![qbank.accelq.com/account/acsum](images/2025-08-01_093419.png "qbank.accelq.com/account/acsum")
17. Damos clic en el botón verde de `[Log out]` y en el selector de campos selecciono `click on a web element`.
18. Presiono la tecla [`Enter`] y tengo el paso número 5, que debo completar: </br>  `5️⃣ Click on text` _(equals, ignore case): 'Log out'. Look for the clickable text on page_
19. Hemos completado el proceso, pero en este punto si trata de **Finalizar y Salir**, es decir dar clic en el botón `[Finalize]` en la parte superior derecha y luego `💾 Finalize Changes`, sale una ventana: </br> ![Modularity is essential](images/2025-08-01_094312.png "Modularity is essential") </br> Modularizar es convertir este escenario grabado en funcionales bloques reusables, que se llaman _actions_.
20. Clic en el botón azul `[Let's Moduralize!]`.
21. Esto ayuda en el mantenimientoy la velocidad del desarrollo a medida que vayas construyendo más escenarios en `AccelQ`.
22. Selecciono del paso `2️⃣ Enter 'qbankadmin' in input` hasta el paso `4️⃣ Click on text (equals, ignore case): 'Sign In'` y presiono el clic derecho.
23. Y selecciono de la lista el penúltimo `Create New Action and Replace`.
<a name="unique-anchor-name"></a>
24. En el `Action Name`, le pongo `Login to QBank`.
25. En el cuadro selector de nombre `Which page does this Action star-from/belong-to ❓`, escribo `QBank Login Page` y presiono [`Enter`] </br> _¿De donde sale este nombre? pues le sale de los 🥚🥚 al Instructor_).</br> ![New Action](images/2025-08-01_103118.png "New Action")
26. Clic en el botón `[Input Params >]`: </br> ![Input Parameters](images/2025-08-01_103449.png "Input Parameters")
27. En este podemos parametrizar los datos a usar en los pasos del _login_. Si quisiera usar el _login_ con diferentes _usernames_ y _passwords_ a través de diferentes escenarios y variar la información.
28. Seleccione el `Username` y dele clic </br> ![Input Parameters -> Username](images/2025-08-01_104006.png "Input Parameters -> Username")
29. Selecciono el `Password` y dmos clic </br> ![Input Parameters -> Password](images/2025-08-01_104242.png "Input Parameters -> Password")
30. Damos clic en el botón azul `[Done]`.
31. La lista de pasos se redujo a solo 2: </br> ![Login to QBank()](images/2025-08-01_104509.png "Login to QBank()") </br> La modularidad se construyó, se puede ver a la izquierda.
32. Vamos a hacer lo mismo con la declaración de `Log out`, para convertirla en acción, dando clic derecho al paso `2️⃣ Click on text (equals, ignore case): 'Log out'` y seleccionando `Create New Action`.
33. En el cuadro de `Action Name` le ponemos `Logout from QBank` y en el selector de `Which page does this Action star-from/belong-to ❓`, escribo `QBank Home Page`.
34. Damos clic en el botón de `[Create Action]`.
35. En este paso el escenario que grabamos se convirtió en una serie de pasos reutilizables. Esto se puede validar al seleccionar las declaraciones de la izquierda y presionando el botón de `[PLAYBACK]` </br> ![Declaraciones seleccionadas](images/2025-08-01_105533.png "Declaraciones seleccionadas")
36. Luego que corrió la prueba, puede presionar el botón superior derecho de `Finalize` y `Finalize Changes` y nos aparece el Escenario, listo para correr: </br> ![Scenario -> Validate Login on QBank](images/2025-08-01_105939.png "Scenario -> Validate Login on QBank") </br> con solo tres pasos: </br> » 1️⃣ Invoke Browser </br> » 2️⃣ Login to QBanck </br> » 3️⃣ Logout from QBank
37. Damos clic al tabulador `Test Cases` y existe solo uno de nombre `Test case 1`, que es el resultado de la grabación.
38. Se pueden crear mas _Test Cases_, con _usernames_ o crendenciales diferentes: </br> ![New Test Case](images/2025-08-01_113201.png "New Test Case")

>[!IMPORTANT]
>
>[![Haz clic aquí y mira el video `Hello World`](images/2025-07-31_084115.gif "Haz clic aquí y mira el video `Hello World`")](videos/01_Hello_World.mp4)
>



### 2. 🚀 Pop Quiz: Introduction to ACCELQ Automation

>[!NOTE]
>
>![🚀 Pop Quiz: Introduction to ACCELQ Automation](images/2025-08-05_090737.gif "🚀 Pop Quiz: Introduction to ACCELQ Automation")
>



### 3. ▶️ Extending Hello World!

1. Ahora que se hizo el escenario `Hello World`, vamos a crear un escenario de complejidad algo identificable. Vamos a tratar de verificar transferencia de fondos en `QBank`.
2. Ya hay un escenario de nombre `Verify Founds Transfer on QBank` y seleccionamos `Record in Design Studio`: </br> ![Scenario -> Record in Design Studio](images/2025-08-05_103637.png "Scenario -> Record in Design Studio")
3. En la parte derecha agregar la _URL_ apuntando a `http://qbank.accelq.com`, que por defecto lo deja en la página de _login_, al darle [`ENTER`], aparece el paso: </br> `1️⃣ Invoque Browser (URL: 'http://qbank.accelq.com')` </br> ![1️⃣ Invoque Browser (URL: 'http://qbank.accelq.com')](images/2025-08-05_104308.png "1️⃣ Invoque Browser (URL: 'http://qbank.accelq.com')")
4. Vamos a hacer _login_ de nuevo, así que dar click derecho en el cuadro de `Username` de la derecha, aparecen los `Commands`, entonces cambia a `Actions`: </br> ![Cambiar `Commands` a `Actions`](images/2025-08-05_104717.png "Cambiar `Commands` a `Actions`")
5. Seleccionamos el que creamos en el paso [24](#1-️-hello-world-lets-automate-our-first-scenario) anterior: `Login to QBank`, y nos pide completar `Username` y `Password`: </br> ![.](images/2025-08-05_111900.png "Login to QBank")
6. Una vez adentro Damos click derecho al botón `[Make a Transfer]`y cambiamos de `Actions` a `Commands`, para luego seleccionar: </br> `clic on a web element` </br> ![Make a Transfer -> clic on a web element](images/2025-08-05_112456.png "Make a Transfer -> clic on a web element") </br> Esto crea el tercer paso </br> `3️⃣ Click on text (equals, ignore case): 'Make a Transfer'`
7. Nos abre un formulario para llenar: </br> ![Formulario -> Transfer Founds](images/2025-08-05_112916.png "Formulario -> Transfer Founds")
8. Damos clic derecho sobre el primer campo de `Transfer form` y Seleccionamos `select an item from a web dropdown`, pero sería mas largo y demorado hacer cada paso.
9. Sugerencia seleccionar toda el área que envuelve el formulario: </br> ![WebElement div#qbl-transfer-box.qbf-box ng-scope](images/2025-08-05_113327.png "WebElement div#qbl-transfer-box.qbf-box ng-scope") </br>
<div>
  <div>
    <div>Transfer Funds</div>
    <div>
      <div>
        <div>01</div>
        <div>Fill Details</div>
      </div>
      <div>
        <div>02</div>
        <div>Confirmation</div>
      </div>
    </div>
    <div>
      <form>
        <div>
          <div>
            <div>Transfer from </div>
            <div>
              <select>
                <option></option>
                <option>Salary Account</option>
                <option>Monthly Savings account</option>
              </select><sup>1️⃣</sup>
            </div>
          </div>
          <div>
            <div>Transfer to </div>
            <div>
              <select>
                <option></option>
                <option>Electricity Bill</option>
                <option>Mortgage Payment</option>
                <option>Day care</option>
                <option>ac</option>
                <option>TEST</option>
                <option>Kumar</option>
                <option>sai</option>
              </select><sup>2️⃣</sup>
            </div>
          </div>
          <div>
            <div>Amount ($)</div>
            <div>
              <input type="number" /><sup>3️⃣</sup>
              <div style="font-size: 12px; font-style: italic">
                Transfer amount not to exceed $150
              </div>
            </div>
          </div>
          <div>
            <div>Date of Transfer</div>
            <div>
              <input type="date" /><sup>4️⃣</sup>
            </div>
          </div>
          <div>
            <div>Memo</div>
            <div>
              <input type="text" /><sup>5️⃣</sup>
            </div>
            <div>
              <div></div>
            </div>
          </div>
          <div>
            <div>
              <div>One-time or repeating?</div>
            </div>
            <div>
              <label>
                <input type="radio" name="onetime_or_repeating" /><sup>6️⃣</sup>
                One-time
              </label>
              <label class="qbl-radiolabel">
                <input type="radio" name="onetime_or_repeating" /><sup>7️⃣</sup>
                Repeating
              </label>
            </div>
            <div>
              <div></div>
            </div>
          </div>
          <div>
            <div></div>
            <div>
              <button type="button">Cancel</button>
              <button type="submit">Submit</button>
            </div>
          </div>
        </div>
      </form>
    </div>
  </div>
</div>


10. Damos clic derecho y seleccionamos un link abajo de nombre `Fill/Update Form Fields`: </br> ![Fill/Update Form Fields](images/2025-08-05_123525.png "Fill/Update Form Fields")
11. Nos trae una estructura numerada con los siete (7) campos que podemos completar: </br> ![Select the fields to generate statments for populate](images/2025-08-05_123808.png "Select the fields to generate statments for populate")
12. El primer campo de `Transfer from`<sup>1️⃣</sup>, le selecciono `Salary Account`.
13. El segundo campo de `Transfer to`<sup>2️⃣</sup>, le selecciono `Electricity Bill`.
14. En el tercero de `Amount($)`<sup>3️⃣</sup>, escribo `10`. </br> Así se ve los campos seleccionados hasta el momento: </br> ![Tres primeros campos](images/2025-08-05_131904.png "Tres primeros campos")
15. En el cuarto de `Date of Transfer`<sup>4️⃣</sup>, le quito el chulo o _checkbox_ ☑️ -> 🔲.
16. El quinto de `Memo`<sup>5️⃣</sup>, le pongo `test`.
17. El sexto de `One-time`<sup>6️⃣</sup> lo dejo intacto y quito el chulo o _checkbox_ ☑️ -> 🔲 de `Repeating`<sup>7️⃣</sup>, y así van los campos: </br> ![Los últimos cuatro campos](images/2025-08-05_132553.png "Los últimos cuatro campos")
18. El cuadro de abajo que dice `Button Label`, le escribo `Submit`.
19. Por último presiono el botón de `[Done]`, y nos sale la ventana de `Generación exitosa` y atrás los pasos que se crearon </br> ![Generación exitosa y los pasos](images/2025-08-05_132958.png "Generación exitosa y los pasos")
20. Aquí le damos al botón `[Create Action]`.
21. Y le ponemos un nombre: `Populate Found Transfer Info` y para `Which page does this Action`, escribimos `Transfer info page`</br> ![New Action -> Populate Founds](images/2025-08-05_133550.png "New Action -> Populate Founds")
22. Damos clic en el botón azúl `[Input Params>]` y nos lleva a esta pantalla: </br> ![Input Parameters](images/2025-08-05_133827.png "Input Parameters")
23. Seleccionamos, los tres primeros y ajustamos los nombres para que no tengan caracters especiales: </br> ![Tres primeros campos de `Input Parameters`](images/2025-08-05_134119.png "Tres primeros campos de `Input Parameters`")
24. La lista de pasos se redujo a cuatro: </br> ![Declaraciones reemplazadas por una nueva Acción](images/2025-08-05_134339.png "Declaraciones reemplazadas por una nueva Acción")
25. Vamos a darle clic derecho al botón superior derecho de `[Log out]` y seleccionamos `Actions` el de nombre `Logout from QBank`: </br> ![Actions -> Logout from QBank](images/2025-08-05_143541.png "Actions -> Logout from QBank")
26. Si revisa la lista de pasos, el 3️⃣, tiene mas acciones que el resto: </br> ![Paso 3️⃣ tiene mas acciones](images/2025-08-05_143833.png "Paso 3️⃣ tiene mas acciones")
27. Como tenemos seleecionado el paso 3️⃣ , en la parte superior seleccionamos en `CREATE ACTION FROM SELECTION`, la opción `Create Action and Replace`: </br> ![Create Action and Replace](images/2025-08-05_144422.png "Create Action and Replace")
28. Le ponemos de nombre `Navigate to founds transfer` y en el campo de `Wich page dows Action`, seleccionamos `QBanck Home Page`: </br> ![New Action -> Navigate to founds transfer](images/2025-08-05_144731.png "New Action -> Navigate to founds transfer")</br> Y clic en el botón azul de `[Create Action]`.
29. VAmos a la parte superior derecha en el botón `[Finalize]` y seleccionamos 💾 `Finalize Changes`: </br> ![💾 Finalize Changes](images/2025-08-05_145201.png "💾 Finalize Changes")
30. Esta es la manera en como se reutilizan acciones en ACCELQ y como el sistema los muestra cuando hay una oportunidad. </br> Así es como se construyen mas y mas escenarios, y se convierte en un reuso eficiente, de activos en vez de recrear o regrabar la lógica de nuevo. </br> ![Escenario y los cinco(5) Pasos](images/2025-08-05_145448.png "Escenario y los cinco(5) Pasos")


>[!IMPORTANT]
>
>[![Haz clic aquí y mira el video `Extending Hello World`](images/2025-08-05_095351.gif "Haz clic aquí y mira el video `Extending Hello World`")](videos/02_Extending_Hello_World.mp4)
>


### 4. 🚀 Pop Quiz: Action Reuse in Scenario Development

>[!NOTE]
>
>![🚀 Pop Quiz: Action Reuse in Scenario Development](images/2025-08-11_142021.gif "🚀 Pop Quiz: Action Reuse in Scenario Development")



### 5. ▶️ Basic Entities in ACCELQ

>[!NOTE]
>
>1. En los últimos dos ejemplos, ACCELQ toma una primera aproximación al diseño para la automatización del test.</br>
>Aquí mientras estamos construyendo elementos en vez de grabar los casos de prueba. Esencialmente esto quiere decir que estamos construyendo una configuración modular desde el _get-go_ (Ve y consigue) y varios pasos han sido creados por ACCELQ como unas simples tareas.
>
>2. Vamos a darle otra mirada a esto en este escenario:</br> ![Scenario: ValidateLogin on QBank](images/2025-08-11_145205.png "Scenario: ValidateLogin on QBank")</br>
>Cada paso que se ve comprende dos porciones.</br>
>Una es el `Login to QBank` que es una acción en ACCELQ, que puede tener ciertos parámetros (_Username_ y _Passord_) y adicional cada acción toma un lugar en un particular página de su aplicación, el cual llama un contexto.
>
>3. Por lo tanto, simplemente por proveer un nombre de página, usted creó una acción, dando mucho mejor contexto a su proceso de negocios y ayuda a entender que está pasando.
>
>4. Antes demostrar los pasos relacionados mas allá del ejemplo, permítame abrir una acción y mostrarla:</br> ![Action: Login to QBank](images/2025-08-11_150244.png "Action: Login to QBank")</br>
>Notará que la acción primariamente consiste de la automatización de la lógica.
>
>5. Esto se detallará mas en próximos vídeos. Ahora vamos detrás de las escenas y examinemos el botón de `NAVIGATOR` que muestra los elementos que van a ser construídos: </br> ![NAVIGATOR](images/2025-08-11_151021.png "NAVIGATOR")
>
>6. Lo primero que muestra son los Escenarios, Contextos y Acciones: </br> ![Scenarios, Contexts, Actions](images/2025-08-11_151522.png "Scenarios, Contexts, Actions")</br>
>Se pueden ver las acciones formuladas, los contextos creados y los escenarios que hemos grabado.
>
>7. Ahora todo esto pasa sin requerir habilidades técnicas avanzadas o esfuerzo adicional de su parte.
>Así que se continua construyendo mas escenarios de pruebas en ACCELQ, todo estará uniéndose y demuestra como esto ayuda a reducir el mantenimiento e incrementar la velocidad de desarrollo.
>
>8. Y el `UNIVERSE` captura las posibles interacciones en su aplicación: </br> ![UNIVERSE](images/2025-08-11_152138.png "UNIVERSE") </br>
>y empieza a auto-formular como se construyen los elementos.
>
>9. Ahora antes de terminar, deseo clarificar y asegurar que todo esté claro. La diferencia entre una `Action` y un `Scenario`: </br> ![Clarificar diferenciar una `Action` de un `Scenario`](images/2025-08-11_152629.png "Clarificar diferenciar una `Action` de un `Scenario`")</br>
>Un `Scenario` es un proceso del negocio que se está probando en cambio una `Action` es un bloque de lógica reutilizable significativo y funcional que se usa como un `Step` en un `Scenario`.



>[!IMPORTANT]
>
>[![Haz clic aquí y mira el video `Key Entities in ACCELQ`](images/2025-08-11_144035.gif "Haz clic aquí y mira el video `Key Entities in ACCELQ`")](videos/03_Key_Entities_in_ACCELQ.mp4)
>



### 6. 🚀 Pop Quiz: Key Entities in ACCELQ

>[!NOTE]
>
>![🚀 Pop Quiz: Key Entities in ACCELQ](images/2025-08-19_152120.gif "🚀 Pop Quiz: Key Entities in ACCELQ")


### 7. ▶️ Introduction to Element Identification (Web)


1. Empezamos con un ejemplo, dando clic en el cuadro de `Username`, después de un rato aparecen las opciones: </br> ![.](images/2025-08-21_112453.png "")</br> Para obtener un elemento para la prueba que se va a correr. </br> La identificación de elementos involucra la definición de este criterio y el término `locator` es comunmente usado para indicar la identifación de un elemento.
2. Se utilizan dos aproximaciones para la identificación de un elemento: </br> » Uno es el **Locator-Free**. </br> » Y el otro es el **Smart-Locator**.
3. **Locator-Free**, no tiene `locators`, es decir no tiene localizadores o identificadores de elemento.
4. **Smart-Locator**, usa una combinación de atributos _HTML_ que son óptimos y probalemente estáticos a favor de identificar un elemento.

![Two ways to identify Elements in ACCELQ](images/2025-08-21_144230.png "Two ways to identify Elements in ACCELQ")

5. En la mayoría de los casos ACCELQ puede identificar usando la aproximación  usando el **Locator-Free**. En el Escenario no se requiere buscar los elementos o los _locators_, que son implícitos yendo con el **Locator-Free**. El ACCELQ permite configurar por defecto cual aproximación utilizar.
6. Yendo por `RESOURCES` está la opción `Project Preferences` </br> ![RESOURCES -> Project Preferences](images/2025-08-22_084607.png "RESOURCES -> Project Preferences")
7. Se especifica el uso de **Locator-Free** o **Smart-Locator**: </br> ![Project Preferences](images/2025-08-22_084803.png "Project Preferences") </br> Vamos a escribir un Escenario ejemplo el cual demuestra estos dos típos de localizadores. El sistema detecta automáticamente cuando usar que tipo de localizador.
8. El primer paso a invocar en el browser dando [`ENTER`] en la _URL_: </br> ![ENTER -> URL](images/2025-08-22_085821.png "ENTER -> URL") </br> ![1️⃣ Invoque Browser](images/2025-08-22_090051.png "1️⃣ Invoque Browser")
9. El siguiente es darle clic derecho al cuadro de `Username` y vamos a la opción de `Actions` y luego `Login to QBank`: </br> ![Login to QBank](images/2025-08-22_090519.png "Login to QBank")
10. Aparece a la izquierda y completamos los campos vacíos o pendientes: </br> ![2️⃣ Login to QBank](images/2025-08-22_090746.png "2️⃣ Login to QBank")
11. Damos clic en un ícono en la parte superior al centro: </br> ![WebElement](images/2025-08-22_091200.png "WebElement") </br> Al momento parece esta información: </br> ![WebElement -> div#qdb_notifications](images/2025-08-22_091358.png "WebElement -> div#qdb_notifications")
12. Damos clic derecho y seleccionamos la opción `click on a web element`: </br> ![click on a web element](images/2025-08-22_091702.png "click on a web element")
13. Pide un nombre al elemento: </br> ![Provide a name for the Element](images/2025-08-22_094801.png "Provide a name for the Element")</br>Esto es un **Smart-Locator** y es manejado como un elemento que necesita proveer un nombre, para tratar con este elemento. </br> Le da clic para completar la operación y aparece el tercer elemento: </br> `3️⃣ Click on Notification icon web element`.
14. Y esto hace que se nevegue a la página siguiente: </br> ![Notifications page](images/2025-08-22_095350.png "Notifications page")
15. Damos clic en `ELEMENTS`: </br> ![Elements(1)](images/2025-08-22_095642.png "Elements(1)") </br> Aparecen todos los **Smart-Locators**
16. Si le doy clic en `Notification icon`: </br> ![Notification icon -> Generic Element <div/>](images/2025-08-22_095921.png "Notification icon -> Generic Element <div/>")
17. Damos clic en el texto `Notifications` y esperamos : </br> ![WebElement -> Notifications](images/2025-08-22_100207.png "WebElement -> Notifications")
18. Aparece el menú de `Generic Element`: </br> ![Generic Element](images/2025-08-22_100458.png "Generic Element") </br> Buscamos y seleccionamos `verify page text`: </br> ![verify page text](images/2025-08-22_101119.png "verify page text")
19. Seleccionamos `verify page contains text (web)`: </br> ![verify page contains text (web)](images/2025-08-22_101419.png "verify page contains text (web)")
20. Completamos el texto faltante de `4️⃣ verify page contains text (web)`: </br> ![4️⃣ verify page contains text (web) -> Notifications](images/2025-08-22_101651.png "4️⃣ verify page contains text (web) -> Notifications")
21. Vamos por el botón superior derecho: </br> ![click on a web element](images/2025-08-22_102002.png "click on a web element") </br> Y me aparecen dos opciones, **Locator-Free** y **Smart-Locator**: </br> ![LOCATOR OPTIONS](images/2025-08-22_102519.png "LOCATOR OPTIONS")
22. Selecciono el **Locator-Free** y obtengo el quinto paso: </br> ![5️⃣ Click on text](images/2025-08-22_102755.png "5️⃣ Click on text") </br>nos lleva a una nueva página: </br> ![Recent Activity](images/2025-08-22_103431.png "Recent Activity")
23. Damos clic en el paso 5️⃣ en el texto `(equals, ignore case)` y seleccionamos `starts with` </br> ![starts with](images/2025-08-22_104311.png "starts with")
24. Cambiamos el texto del paso 5️⃣ por `Mark as Read` </br> ![Mark as Read](images/2025-08-22_104710.png "Mark as Read") </br> De esta manera, aunque el _label_ fue algo dinámico, se usarí un **Locator-Free**. </br> Y una vez esto esta hecho, puede pasar al normal curso para convertir esto en una `Action` y salir de este `Scenario`.



>[!IMPORTANT]
>
>[![Element_Id](images/2025-08-21_100000.gif "Haz clic aquí y mira el video `Element_Id`")](videos/04_Element_Id.mp4)
>



### 8. 🚀 Pop Quiz: Introduction to Element Identification


>[!NOTE]
>
>![🚀 Pop Quiz: Introduction to Element Identification](images/2025-08-27_101432.gif "🚀 Pop Quiz: Introduction to Element Identification")



### 9. ▶️ Navigating around ACCELQ

1. Navegar a través de `ACCELQ`, es muy intuitivo, veremos algunos controles y las funcionalidades disponibles.
2. Empezando por la navegación superior, está en la imagen superior a la derecha, el `Profile` o Perfil: </br> ![Profile](images/2025-08-28_110411.png "Profile") </br> Se ve la descripción, el correo, cambio de contraseña.
3. `Auth Properties`: Están las `KEY` o _Tokens_ para utilizar desde una _API_.

|||
|-|-|
|![Auth Properties](images/2025-08-28_110901.png "Auth Properties") | Las `KEY` se usan para herramientas de integración con `ACCELQ`.|

4. `Project Information`: Al lado de la imagen del `Profile` o Perfil, está el proyecto y la información de este.

|||
|-|-|
|![Project Information](images/2025-08-28_144011.png "Project Information")| Se puede cambiar entre los diferentes proyectos.</br> Aquí también aparece el `Role` = `QA Engineer`.</br> Y los privilegios a los que este corresponde.</br> También el `Test Asset View`, los cuales son las preferencias que se tienen tanto para automatización como para manual.</br>Controla que _asset_ desea verse y obtiene una vista rápida a configuración.|

5. `Project Settings`, donde puede configurar una montón de cosas relacionadas con el proyecto.

|||
|-|-|
|![Project Settings](images/2025-08-28_145151.png "Project Settings")| Se debe tener privilegios de administrador.|

6. `Project Activity`: Se pueden ver los proyectos recientes

|||
|-|-|
|</br> ![Project Activity](images/2025-08-28_145436.png "Project Activity")|Se accede a los proyectos recientes.|

7. `Activity`: Estos sería la vista de los proyectos recientes.

|||
|-|-|
|![Activity](images/2025-08-28_145650.png "Activity")|En este caso de las dos últimas semanas|

8. `Activity -> Filter by users`: Por defecto aparecen `ALL USERS`

|||
|-|-|
|![Activity -> Filter by users](images/2025-08-28_145911.png "Activity -> Filter by users")|También lo puede filtrar por cada usuario|

9. `Help Center`: El el botón con el ❔ es el `Help Center` o centro de ayuda:

|||
|-|-|
|![Help Center](images/2025-08-28_150212.png "Help Center")|Se puede consultar cualquier tema del `ACCELQ`|

10. `Help Center -> Knowledge Base`: Se escribe de forma libre.

|||
|-|-|
|![Help Center -> Knowledge Base](images/2025-08-28_150528.png "Help Center -> Knowledge Base")|Provee acceso a la base del conocimiento, donde puede escribir o preguntar de forma libre, sobre el tema que se desea aprender.|

11. `Browse Product Guide`: Se puede tener acceso a recursos de aprendizaje.

|||
|-|-|
|![Browse Product Guide](images/2025-08-28_153138.png "Browse Product Guide")|» `Product Guide` o Guía de productos </br>» `Learn by Videos` o Aprender por vídeos </br> » `Commands in Action Logic` o Comandos Lógicos de Acciones|

12. `What's New?`: Abajo a la derecha del `Help Center`.

|||
|-|-|
|![What's New?](images/2025-08-28_153502.png "What's New?")|Para mirar las nuevas características que están disponibles en la actual versión|

13. `What's New in Release 5.1`: Al darle clic a `What's New?` aparece esta ventana.

|||
|-|-|
|![What's New in Release 5.1](images/2025-08-28_153915.png "What's New in Release 5.1") </br> ![What's New ACCELQ](images/2025-08-28_154224.png "What's New ACCELQ")|En el botón `Explore Now`, muestras las nuevas características que le fueron agregadas. </br> </br> Las caracterías que tenemos en esta versión.|

14. `Create New Entity`: el botón con el signo de ➕.

|||
|-|-|
|![Create New Entity](images/2025-08-28_164549.png "Create New Entity") </br> ![Create New Entity -> List](images/2025-08-28_164950.png "Create New Entity -> List") |Donde se puede crear de forma rápida uno de los siguiente elementos: </br> » `AUTO` ->`Test Suite` o Conjunto de Pruebas en Auto </br> » `AUTO`-> `Scenario` o Escenarios en Auto </br> » `AUTO`->`Context` o Contextos en Auto </br> » `AUTO`->`Action` o Acciones en Auto </br> </br> » `MANUAL`->`Test Suite` o Conjunto de Pruebas Manuales </br> » `MANUAL`->`Scenario` o Escenarios Manuales|

15. `RUN`: El botón para ejecución

|||
|-|-|
|![Run](images/2025-08-28_171038.png "Run") </br> ![Run -> List](images/2025-08-28_171237.png "Run -> List") | Provee acceso a ejecutar pruebas. </br> </br> Estas pueden ser:</br> » `Run Automation Test` o Correr pruebas automáticas </br> » `Create CI Job` o Crear Trabajos de Integración Continua</br> » `Start Manual Test` o Ejecutar pruebas Manuales|

16. `Global Search / ctrl+G`🔍: Búsqueda Global.

|||
|-|-|
|![Global Search / ctrl+G](images/2025-08-28_171802.png "Global Search / ctrl+G") </br> ![.](images/2025-08-28_172106.png "") |Acá se puede conseguir cualquier entidad sin necesidad de hacerlo manualmente. </br> </br> Busca por cualquier parte del nombre con mayúsculas o minúsculas, y luego seleccionarlo.|

17. `UNIVERSE`: En la barra izquierda de navegación.

|||
|-|-|
|![UNIVERSE](images/2025-08-28_172521.png "UNIVERSE") | Esquema Visual de como se relacionan loe elementos en las pruebas. </br> </br> Permite seguir los casos de prueba y navegar sobre estas.|

18. `NAIGATOR`: Va a alguno de los elementos del aplicativo.

|||
|-|-|
|![NAVIGATOR](images/2025-08-28_172856.png "NAVIGATOR") |Donde se puede navegar de forma rápida uno de los siguiente elementos: </br> » `AUTO` ->`Test Suite` o Conjunto de Pruebas en Auto </br> » `AUTO`-> `Scenario` o Escenarios en Auto </br> » `AUTO`->`Context` o Contextos en Auto </br> » `AUTO`->`Action` o Acciones en Auto </br> </br> » `MANUAL`->`Test Suite` o Conjunto de Pruebas Manuales </br> » `MANUAL`->`Scenario` o Escenarios Manuales|

19. `NAVIGATOR`->`Scenarios`: Seleccioné este y me lleva a los Escenarios, que tengo creados, para este Proyecto.

|||
|-|-|
|![Scenarios](images/2025-08-28_173218.png "Scenarios") |Lista todos los escenarios que están disponibles. </br> Se pueden aplicar algunos filtros. </br> Puede cambiar el Orden de la lista. </br>|

20. `RESOURCES`: las herramientas que se pueden utilizar.

|||
|-|-|
|![RESOURCES`](images/2025-08-28_173617.png "RESOURCES") |Estos recursos los cuales son el soporte a las entidades. </br> » `DATA`->`Global Propierties` </br> » `DATA`->`Run Properties` </br> » `DATA`->`Data List` </br> » `DATA`->`Data Types` </br> » `RESOURCES`->`User Extensions` </br> » `RESOURCES`->`Local Agents` </br> » `RESOURCES`->`Drivers Profiles`|

21. `Global Propierties`: Tengo acceso a los diferente elementos de `RESOURCES`

|||
|-|-|
|![Global Propierties](images/2025-08-28_174439.png "Global Propierties") | Presentación similar a los elementos de `NAVIGATOR`. </br> </br> En la parte de arriba se ven las listas de `RESOURCES`.|

22. `RESULTS`: En el menú de la izquierda.

|||
|-|-|
|![RESULTS](images/2025-08-28_174820.png "RESULTS") </br> ![RESULTS->List](images/2025-08-28_174957.png "RESULTS->List") |Son los resultados tanto Automáticos como manuales y las Tareas de Integración Contiua `CI Jobs`. </br> Los listados son ordenados del mas reciente al mas antiguo. </br>  |

23. Puedo por ejemplo empezar por `NAVIGATOR`, seleccionar `Scenarios`. </br> Luego estando en `SCENARIOS`, Selecciono uno de esa lista, ejemplo `Verify Login on QBank`. </br> Luego puedo revisar una de las `Action` en esta lista y me lleva a visualizar en detalle esa `Action`: </br> ![Scenarios -> Action -> Detail](images/2025-08-28_175818.png "Scenarios -> Action -> Detail")
24. Puedo navegar a `Account Summary Page`: </br> ![Account Summary Page](images/2025-08-28_180114.png "Account Summary Page")
25. Aqui pudimos ver un rápido vistazo a las mútiples entidades que tenemos, las cuales se pueden editar em cualquier momento.



>[!IMPORTANT]
>
>[![Reviewed_Navigating_around_in_ACCELQ](images/2025-08-27_15552.gif "Haz clic aquí y mira el video `Reviewed_Navigating_around_in_ACCELQ`")](videos/05_Reviewed_Navigating_around_in_ACCELQ.mp4)
>



