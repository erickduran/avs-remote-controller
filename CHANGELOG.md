# Changelog
En este archivo se documentarán todos los cambios relevantes realizados en todos los ambientes para el desarrollo del presente proyecto. Esto incluye tanto instalaciones como desarrollo del código.

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

Agregar la siguiente configuración en `/boot/config.txt`:
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

## 2019-03-04 - AVS-5
Se creó la estructura general del proyecto en el repositorio, las únicas dependencias necesarias hasta el momento son la librería __click__. Comando para instalación:
```pip install click```

Así pues, se definió el primer modo de ejecución (modo "cli"), el cual peuede ser ejecutado de la siguiente manera:
```python main.py cli```

## 2019-03-04 - AVS-6 Circuito principal
Se diseñó el circuito para el sistema de infrarojos, esto para integrarlo al sistema de Synaptics AudioSmart.

![Circuito](https://raw.githubusercontent.com/erickduran/avs-remote-controller/develop/docs/img/01-circuit.png)

## 2019-02-26 - AVS-2, AVS-3 y AVS-4
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


## 2019-02-19 - AVS-1 y AVS-2
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
