# TPFins - Documentación del proyecto

TPFins es una página web basada en Django que proporciona una plataforma para administrar y buscar benchmarks de operaciones financieras. A continuación, encontrarás una descripción general del proyecto y las instrucciones para configurar el entorno de desarrollo.

Descripción general
TPFins es una página web que consta de los siguientes componentes principales:

Benchmark Request: Este modelo permite a los usuarios enviar solicitudes de benchmarks específicos. Cada solicitud contiene información detallada sobre los requisitos del benchmark, como país, tipo de analisis, induatria, entre otros.

TPFins Tool: Este modelo permite a los usuarios enviar solicitudes de benchmarks específicos. Cada solicitud contiene información detallada sobre los requisitos de la operacion financiera, como moneda, tipo de tasa de interes, entre otros.

Contact Us: Este modelo permite a los usuarios ponerse en contacto con los administradores del sitio para realizar consultas o informar problemas relacionados con el sitio web.

Además, la página web también ofrece un buscador de benchmarks por país, lo que permite a los usuarios buscar benchmarks específicos en función de su ubicación geográfica.

# Configuración del entorno de desarrollo
Sigue estos pasos para configurar el entorno de desarrollo y ejecutar el proyecto localmente:

Clona el repositorio de TPFins desde GitHub: git clone <URL_DEL_REPOSITORIO>

Ve al directorio del proyecto: cd tpfins

Crea un entorno virtual para el proyecto (opcional pero se recomienda): python3 -m venv env

Activa el entorno virtual:

En Linux/Mac: source env/bin/activate
En Windows: env\Scripts\activate
Instala las dependencias del proyecto: pip install -r requirements.txt

Realiza las migraciones de la base de datos: python manage.py migrate

Inicia el servidor de desarrollo: python manage.py runserver

Una vez completados estos pasos, podrás acceder al sitio web de TPFins localmente en tu navegador web utilizando la URL http://localhost:8000/.

Instrucciones para entrar al panel aministrativo de Django:
Acceder con user y password via:
127.0.0.1:8000/admin

Superusuario de pruebas
username:prueba_superadmin@hotmail.com contraseña:Chau123!

Usuarios normales
username:prueba@hotmail.com contraseña:Hola123!