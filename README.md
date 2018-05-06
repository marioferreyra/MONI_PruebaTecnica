Prueba Tecnica - MONI
=====================

Enunciado
---------
Se debe desarrollar sitio web en el que se registran pedido de prestamos de usuarios que acceden a el.  
El usuario no necesita registrarse para solicitar un préstamo.  
Para definir si al usuario se le aprueba o no el préstamoo usaremos una API definida debajo:

  * Endpoint: <http://scoringservice.moni.com.ar:7001/api/v1/scoring/>

  * Ejemplo: <http://scoringservice.moni.com.ar:7001/api/v1/scoring/?document_number=30156149&gender=M&email=fran@mail.com>

**ACLARACION:** Usar esta API, no implementarla.

El formulario de pedido de prestamos el usuario debe ingresar:
  * DNI
  * Nombre
  * Apellido
  * Genero (Masculino, Femenino)
  * E-mail
  * Monto solicitado.

El usuario luego de ingresar los datos debe recibir la respuesta **negativa** o **positiva** en la misma página que ingreso sus datos.  
Contemplar casos de datos ingresados con errores.

También se debe desarrollarse un **sitio de administración** en el que se puedan ver los pedidos de préstamo, con la opción de:
  * Editarlos
  * Eliminarlos

A este sitio solo pueden acceder usuarios administradores.  

**ACLARACION:** No usar _admin_ de Django.


Instalación
-----------

1.  Se necesita el siguiente software:

    -   Git
    -   Flake8
    -   Pip
    -   Python 3.4 o posterior
    -   Virtualenv

    En un sistema basado en Debian (como Ubuntu), se puede hacer:

        $ sudo apt-get install git flake8 python-pip python3 virtualenv

2.  Crear y activar un nuevo [virtualenv]. Recomiendo usar [virtualenvwrapper]. Se puede instalar así:

        $ sudo pip install virtualenvwrapper

    Y luego agregando la siguiente línea al final del archivo `.bashrc`:

        export WORKON_HOME=$HOME/.virtualenvs
        export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
        export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
        [[ -s "/usr/local/bin/virtualenvwrapper.sh" ]] && source "/usr/local/bin/virtualenvwrapper.sh"

    Para crear y activar nuestro virtualenv:

        $ mkvirtualenv --python=/usr/bin/python3 moni

3.  Bajar el código:

        $ git clone https://github.com/marioferreyra/Prueba_Tecnica_MONI.git

4.  Instalarlo:

        $ cd Prueba_Tecnica_MONI
        $ pip install -r requirements.txt

Ejecución
---------

1.  Activar el entorno virtual con:

        $ workon moni

2. Generar y llenar la base de datos:

        $ cd Prestamista
        $ python manage.py migrate


3. Activar el server local:

        $ python manage.py runserver

4. Luego en el navegador acceder a la pagina web:

        http://127.0.0.1:8000/prestamos/
        ó
        http://localhost:8000/prestamos/

5. Para entrar al **Log in** se debe crear un superusuario de Django, usar el siguiente comando:

        $ python manage.py createsuperuser

    Ahora podra ingresar al "Log in" ingresando el usuario y contraseña que uso para crear al superusuario de Django.

6. Desactivar el entorno virtual

        $ deactivate


Chequear Estilo de Código
-------------------------

Correr flake8 sobre el paquete o módulo que se desea chequear.  
Por ejemplo:

    $ flake8 Prueba_Tecnica_MONI


<!---------------------- Links ---------------------->
[virtualenv]: http://virtualenv.readthedocs.org/en/latest/virtualenv.html
[virtualenvwrapper]: http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation
