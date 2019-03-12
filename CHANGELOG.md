# Changelog
En este archivo se documentarán todos los cambios relevantes realizados en todos los ambientes para el desarrollo del presente proyecto. Esto incluye tanto instalaciones como desarrollo del código.

## 2019-03-12 - AVS-5 Arquitectura general
A continuación se presenta el diagrama de clases con la arquitectura general del presente proyecto:

![Arquitectura](https://raw.githubusercontent.com/erickduran/avs-remote-controller/master/docs/img/03-class-diagram.jpg)

## 2019-03-11 - AVS-28 REST API
Se implementó la primera versión del API para enviar comandos desde clientes externos a la televisión. E

El _endpoint_ público está disponible en `http://vcrc.erickduran.com:55555`.

La documentación completa puede consultarse [aquí](https://github.com/erickduran/avs-remote-controller/blob/master/docs/API.md).

## 2019-03-11 - AVS-30 Se implementó la versión _review_mode_
Se implementó una versión del modo `cli` que permite interactuar con el programa sin emitir los comandos del hardware, con el objetivo de realizar pruebas locales y al público.

Para correr el _review_mode_ implementado, es necesario correr el siguiente comando:
```bash
python3 main.py cli lg
``` 

## 2019-03-10 - AVS-10 Código en Python
Se implementó la primera versión del código en Python para interactuar con la televisión a través de comandos IR. Se agregó una dependencia:

```bash
pip3 install pyyaml
```

Para correr el modo interactivo implementado, es necesario correr el siguiente comando:
```bash
python3 main.py cli lg
``` 

La nueva interface permite enviar los comandos descritos en los archivos `remote-controller/resources/commands.yml` (simplificados) y `remote-controller/resources/raw-commands.yml` (directos a `lirc`). Los comandos simplificados permiten enviar argumentos adicionales, dependiendo de cada comando. Para verificar cada comando específicamente, ver sus archivos de configuración.

## 2019-03-09 - AVS-7, AVS-8 y AVS-9 Reconocimiento de señales IR
Una vez configurado el sensor (receptor) IR, se realizó la primera configuración de los comandos para una televisión marca LG. A continuación se presenta el procedimiento que se siguió para lograr esto.

Para probar que el circuito con el receptor IR está funcionando, primero se deshabilita el servicio:

```bash
sudo service lircd stop
```

Y ejecutando el siguiente comando:

```bash
mode2 -d /dev/lirc0
```

Al apuntar un control al receptor, pueden verse algunas salidas en consola.

![Salida](https://raw.githubusercontent.com/erickduran/avs-remote-controller/master/docs/img/02-mode-output.png)

Para agregar un nuevo control y almacenar comandos, es necesario ejecutar el siguiente comando:
```bash
irrecord -d /dev/lirc0
```
El cual utilizará el dispositivo que se ha configurado para encontrar la configuración correcta. `lirc` mostrará un instalador interactivo para facilitar la configuración, seguir los pasos y obtener el archivo generado. Para este caso, se obtuvo el archivo `lg.lircd.conf` (en la carpeta donde se ejecutó). 

Es necesario seguir los pasos __exactamente__ como se piden, ya que, de no ser así, la configuración no se podrá crear. Para uno de los pasos, es necesario contar con los nombres de los comandos en el ambiente `lirc`, los cuales pueden ser consultados [aquí](https://gist.github.com/unforgiven512/0c232f4112b63021a8e0df6eedfb2ff3).

Para los fines de este proyecto, los comandos configurados fueron:
- `KEY_POWER`
- `KEY_VOLUMEDOWN`
- `KEY_VOLUMEUP`
- `KEY_CHANNELUP`
- `KEY_CHANNELDOWN`
- `KEY_UP`
- `KEY_DOWN`
- `KEY_LEFT`
- `KEY_RIGHT`
- `KEY_OK`
- `KEY_0`
- `KEY_1`
- `KEY_2`
- `KEY_3`
- `KEY_4`
- `KEY_5`
- `KEY_6`
- `KEY_7`
- `KEY_8`
- `KEY_9`
- `KEY_LIST`
- `KEY_UNDO`
- `KEY_BACK`
- `KEY_INFO`
- `KEY_EXIT`
- `KEY_MENU`
- `KEY_MUTE`
- `KEY_CONFIG`
- `KEY_VIDEO`
- `KEY_SCREEN`

El archivo resultante se copió a `/etc/lirc/lircd.conf.d`, utilizando el siguiente comando:
`sudo cp lg.lircd.conf /etc/lirc/lircd.conf.d/lg.lircd.conf`

Y se obtuvo la siguiente configuración:
##### `/etc/lirc/lircd.conf.d/lg.lircd.conf`
```
begin remote

  name  lg
  bits           32
  flags SPACE_ENC|CONST_LENGTH
  eps            30
  aeps          100

  header       8981  4511
  one           507  1735
  zero          507   614
  ptrail        502
  repeat       8983  2274
  gap          108016
  toggle_bit_mask 0x0
  frequency    38000

      begin codes
          KEY_POWER                0x20DF10EF 0xBE89025C
          KEY_VOLUMEDOWN           0x20DFC03F 0xBE89025C
          KEY_VOLUMEUP             0x20DF40BF 0xBE89025C
          KEY_CHANNELUP            0x20DF00FF 0xBE89025C
          KEY_CHANNELDOWN          0x20DF807F 0xBE89025C
          KEY_UP                   0x20DF02FD 0xBE89025C
          KEY_DOWN                 0x20DF827D 0xBE89025C
          KEY_LEFT                 0x20DFE01F 0xBE89025C
          KEY_RIGHT                0x20DF609F 0xBE89025C
          KEY_OK                   0x20DF22DD 0xBE89025C
          KEY_0                    0x20DF08F7 0xBE89025C
          KEY_1                    0x20DF8877 0xBE89025C
          KEY_2                    0x20DF48B7 0xBE89025C
          KEY_3                    0x20DFC837 0xBE89025C
          KEY_4                    0x20DF28D7 0xBE89025C
          KEY_5                    0x20DFA857 0xBE89025C
          KEY_6                    0x20DF6897 0xBE89025C
          KEY_7                    0x20DFE817 0xBE89025C
          KEY_8                    0x20DF18E7 0xBE89025C
          KEY_9                    0x20DF9867 0xBE89025C
          KEY_LIST                 0x20DF32CD 0xBE89025C
          KEY_UNDO                 0x20DF14EB 0xBE89025C
          KEY_BACK                 0x20DF58A7 0xBE89025C
          KEY_INFO                 0x20DF55AA 0xBE89025C
          KEY_EXIT                 0x20DFDA25 0xBE89025C
          KEY_MENU                 0x20DFA25D 0xBE89025C
          KEY_MUTE                 0x20DF906F 0xBE89025C
          KEY_CONFIG               0x20DFC23D 0xBE89025C
          KEY_VIDEO                0x20DFD02F 0xBE89025C
          KEY_SCREEN               0x20DF9E61 0xBE89025C
      end codes

end remote
```
Al copiar la configuración en la carpeta mencionada, `lirc` podrá consultarla automáticamente al enviar los comandos.

Una vez concluido esto, se pueden enviar las instrucciones a la televisión utilizando el siguiente comando:
```
irsend SEND_ONCE <DEVICE_NAME> <COMMAND>
```
Para este caso, un ejemplo sería:
```
irsend SEND_ONCE lg KEY_POWER
```
Y el comando debe emitirse. Se mostrarán los errores relevantes de ser necesario. 

Si el comando no funciona (y no hay errores), puede ser que el emisor IR no esté colocado en posición (apuntando a la televisión). Puede probarse la funcionalidad del comando utilizando un LED convencional. Al ejecutarse el comando, el LED debe parpadear rápidamente.

__NOTA: debe de estar configurado y colocado correctamente el sensor IR emisor para que esto funcione.__

## 2019-03-09 - AVS-4 Preparación del sensor IR
Se logró integrar el circuito con los sensores infrarrojo, y se ajustó el modelo para las necesidades del proyecto. 

Para realizar la configuración de `lirc` para el control de televisión deseado, se debe seguir este procedimiento:

Modificar los siguientes parámetros del archivo `/etc/lirc/lirc_options.conf` (no modificar otros parámetros):
##### `/etc/lirc/lirc_options.conf`
```
driver = default
device = /dev/lirc0
```

Agregar la siguiente configuración en `/etc/lirc/hardware.conf`:
##### `/etc/lirc/hardware.conf`
```
## /etc/lirc/hardware.conf

# Arguments which will be used when launching lircd
LIRCD_ARGS="--uinput"

# Don't start lircmd even if there seems to be a good config file
# START_LIRCMD=false

# Don't start irexec, even if a good config file seems to exist.
# START_IREXEC=false

# Try to load appropriate kernel modules
LOAD_MODULES=true

# Run "lircd --driver=help" for a list of supported drivers.
DRIVER="default"

# usually /dev/lirc0 is the correct setting for systems using udev
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"

# Default configuration files for your hardware if any
LIRCD_CONF=""
LIRCMD_CONF=""
```

Agregar la siguiente configuración en `/boot/config.txt`:
##### `/boot/config.txt`
```
dtoverlay=lirc-rpi,gpio_in_pin=23,gpio_out_pin=22
```

Agregar la siguiente configuración en `/etc/modules`:
##### `/etc/modules`
```
lirc_dev
lirc_rpi gpio_in_pin=23 gpio_out_pin=22
```

Para que los cambios tengan efecto, reiniciar el servicio de `lirc`:
```bash
sudo service lircd stop && sudo service lircd start
```

Reiniciar el equipo:
```bash
sudo reboot
```

Verificar estado del servicio (opcional):
```bash
sudo service lircd status
```

__NOTA: El servicio puede llamarse `lirc` o `lircd`, dependiendo de la instalación.__

## 2019-03-04 - AVS-5 Dependencias
Se creó la estructura general del proyecto en el repositorio, las únicas dependencias necesarias hasta el momento son la librería __click__. Comando para instalación:

```bash
pip3 install click
```

Así pues, se definió el primer modo de ejecución (modo "cli"), el cual peuede ser ejecutado de la siguiente manera:

```bash
python main.py cli
```

## 2019-03-04 - AVS-6 Circuito principal
Se diseñó el circuito para el sistema de infrarojos, esto para integrarlo al sistema de Synaptics AudioSmart.

![Circuito](https://raw.githubusercontent.com/erickduran/avs-remote-controller/master/docs/img/01-circuit.png)

## 2019-02-26 - AVS-2, AVS-3 y AVS-4 Certificados e instalaciones
Se instalaron los certificados necesarios para el funcionamiento dentro de la red de CETYS Universidad. El archivo `cert.crt` fue colocado en la carpeta `/usr/share/ca-certificates` y se ejecutaron los siguietnes comandos para instalarlo:

```bash
sudo dpkg-reconfigure ca-certificates
```

Adicionalmente, se instaló la paquetería necesaria para realizar la interacción con los sensores infrarrojo (IR) a través de los pines GPIO. Para esto, se ejecutó:

```bash
sudo apt-get install lirc
```

En caso de enfrentarse con el error "No package candidate found" o errores similares, verificar las fuentes de `apt-get`:
##### `/etc/apt/sources.list.d/raspi.list` 
```
deb http://raspbian.raspberrypi.org/raspbian/ stretch main contrib non-free rpi
```
Esta fuente es necesaria para encontrar el paquete `lirc`.


## 2019-02-19 - AVS-1 y AVS-2 Wi-Fi
Se realizó la configuración inicial de la red Wi-Fi de CETYS Universidad. La configuración se realzó en el archivo `/etc/wpa_supplicant.conf` de la RPi. A continuación se muestra la configuración agregada:

##### `/etc/wpa_supplicant.conf`
```
network={
    ssid="CETYS_Alumnos"
    key_mgmt=WPA-EAP
    eap=PEAR
    identity="username"
    password="password"
    phase2="auth=MSCHAPv2"
}
```
