
# Proyecto: Creación de pruebas para comprobar la funcionalidad de Urban Routes 

## Acerca del Proyecto
Este proyecto se centra en la creación de kits personalizados para usuarios a través de una API. Se sigue un flujo de trabajo que incluye la creación de un nuevo usuario y la autenticación del mismo mediante un autotoken proporcionado por la API. Posteriormente, se procede a la creación de un nuevo kit personalizado asociado al usuario recién creado.
El objetivo principal es garantizar que el proceso de creación de kits funcione correctamente y que los datos proporcionados en el campo "name" cumplan con los requisitos especificados por la API. Esto se logra mediante pruebas exhaustivas tanto positivas como negativas, que validan la funcionalidad esperada y manejan los casos de error de manera adecuada.

Urban Routes es una aplicación para solicitar taxis por lo que éste proyecto se basa en la creación de pruebas para la 
comprobación de la funcionalidad de la aplicación, desde el ingreso de las direcciones hasta obtener los detalles finales del viaje. 

Proceso:

- Se han especificado los localizadores de todos los elementos necesarios en el archivo "Locators.py"
- Se han creado métodos para cada paso en el proceso de solicitud de taxi en el archivo "Methods.py"
- Se han especificado datos de prueba en el archivo "data.py"
- Se han escrito test para comprobar que la aplicación funciona correctamente en el archivo "main.py"

## Tecnologías Utilizadas
- PyCharm: Entorno de desarrollo integrado (IDE)
- Pytest: Marco de pruebas automatizadas
- Selenium: Herramienta para automatizar navegadores web
- Webdriver: (Selenium WebDriver) Interfaz de programación que permite interactuar con navegadores web
- Python: Lenguaje de programación utilizado para el desarrollo
- ChromeDriver: Controlador de WebDriver para Chrome

## Instalación y uso de las Librerías
1. Instala PyCharm desde su página oficial. Descarga la versión gratuita: Community. (https://www.jetbrains.com/pycharm/download/)
2. Clona este repositorio en tu máquina local.
3. Abre el proyecto en PyCharm.
4. Abre una terminal en la ubicación del proyecto y ejecuta los siguiente comando para instalar pytest y requests: 
    pip install pytest requests

## Conectar Selenium en PyCharm
Para trabajar con Selenium WebDriver, es necesario conectarlo con tu IDE. En primer lugar, se debe instalar un 
controlador para tu navegador para que las pruebas automatizadas puedan acceder a él.

PASO 1:
Instala el controlador del navegador
Todos los navegadores populares son compatibles con Selenium WebDriver. Cada navegador tiene su propia versión del controlador.

        ## Para Safari

        Solo tienes que activar WebDriver; ya está integrado. Para activarlo, ejecuta el siguiente comando en la terminal:
        safaridriver --enable

        ## Para Firefox, Internet Explorer o Edge

        Accede al sitio oficial de Selenium donde se encuentran los drivers:
        https://www.selenium.dev/documentation/getting_started/installing_browser_drivers/
        Verás una selección de diferentes archivos comprimidos. Descarga el que coincida con tu sistema operativo.
        Descomprime el archivo. Crea una carpeta llamada WebDriver/bin y guarda el archivo allí.
        Agrega la ruta a bin a la variable de entorno PATH. El algoritmo depende del sistema operativo.

                ### Para Windows
                    - Abre el Panel de Control.
                    - Ve a Sistema → Configuración avanzada del sistema → Variables de entorno.
                    - Busca y edita la variable PATH agregando la ruta completa hacia la carpeta bin que acabas 
                      de crear. Debería ser algo como C:\WebDriver\bin.


                ### Para MacOS y Linux

                    - Abre la terminal.
                    - Ejecuta el siguiente comando para agregar la carpeta bin al PATH del sistema:
                        export PATH=/Users/<username>/Downloads/WebDriver/bin:$PATH

        Si planeas descargar WebDriver para otros navegadores y sus versiones, guarda todos los archivos en la
        misma carpeta: WebDriver/bin. De esta manera, no tendrás que editar PATH de nuevo.
        
        ## Para Chrome

        1. Acceder al sitio oficial de Selenium donde se encuentran los drivers:
        https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/
        2. Selecciona la versión del controlador que coincida con tu versión de navegador.
        3. Haz clic en Downloads (Descargas) para abrir una ventana con carpetas que contienen diferentes versiones del 
        controlador. Necesitas la versión que coincida con la versión de tu navegador, al menos la parte antes del primer
        punto. Por ejemplo, si la versión de tu navegador es 102.0.5005.115, funcionarán tanto la versión 102.0.5005.27 
        como la 102.0.5005.61 del controlador. Si no encuentras ninguna coincidencia, descarga la versión más reciente.
        4. Hay varios archivos comprimidos en la carpeta. Descarga el que coincida con tu sistema operativo.
        5. Descomprime el archivo. Crea una carpeta llamada WebDriver/bin y guarda el archivo allí.
           Agrega la ruta a bin a la variable de entorno PATH. El algoritmo depende del sistema operativo.

                  ### Para Windows

                     - Abre el Panel de Control.
                     - Ve a Sistema → Configuración avanzada del sistema → Variables de entorno.
                     - Busca y edita la variable PATH agregando la ruta completa hacia la carpeta bin que acabas de crear. Debería ser algo como C:\\WebDriver\\bin.

                  ### Para MacOS y Linux

                     - Abre la terminal.
                     - Ejecuta el siguiente comando para agregar la carpeta bin al PATH del sistema:
                     - export PATH=/Users/<username>/Downloads/WebDriver/bin:$PATH

        Si planeas descargar WebDriver para otros navegadores y sus versiones, guarda todos los archivos en la misma 
        carpeta: WebDriver/bin. De esta manera, no tendrás que editar PATH de nuevo.

PASO 2
Para poder utilizar Selenium con Python, necesitas instalar el paquete de Selenium. Sigue los siguientes pasos:

1. Abrir la Consola o Terminal Terminal desde las aplicaciones o usando el buscador de aplicaciones.
2. Ejecutar el Comando de Instalación
3. Escribe el siguiente comando para instalar el paquete de Selenium:
      pip install selenium

Nota: Si recibes un mensaje de error que indica que pip no está instalado o no se reconoce, intenta 
utilizar pip3 en lugar de pip:
      pip3 install selenium


## Autor y Sprint del Proyecto
Autor: Carolina Rosillo
Sprint del Proyecto: [Sprint #7]
