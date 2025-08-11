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
>[![Haz clic aquí y mira el video `Hello World`](images/2025-07-31_084115.gif "Haz clic aquí y mira el video `Hello World`")](videos/01_Hello%20World.mp4)
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
>[![Haz clic aquí y mira el video `Extending Hello World`](images/2025-08-05_095351.gif "Haz clic aquí y mira el video `Extending Hello World`")](videos/02_Extending%20Hello%20World.mp4)
>


### 4. 🚀 Pop Quiz: Action Reuse in Scenario Development

>[!NOTE]
>
>![🚀 Pop Quiz: Action Reuse in Scenario Development](images/2025-08-11_142021.gif "🚀 Pop Quiz: Action Reuse in Scenario Development")


