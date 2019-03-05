# Changelog
En este archivo se documentarán todos los cambios relevantes realizados en todos los ambientes para el desarrollo del presente proyecto. Esto incluye tanto instalaciones como desarrollo del código.

## 2019-02-26 - AVS-2, AVS-3 y AVS-4
Se instalaron los certificados necesarios para el funcionamiento dentro de la red de CETYS Universidad. El archivo `cert.crt` fue colocado en la carpeta `/usr/share/ca-certificates` y se ejecutaron los siguietnes comandos para instalarlo:

```bash
sudo dpkg-reconfigure ca-certificates
```

Adicionalmente, se instaló la paquetería necesaria para realizar la interacción con los sensores infrarrojo (IR) a través de los pines GPIO. Para esto, se ejecutó:

```bash
sudo apt-get install lirc
```

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
## 2019-03-04 - System Circuit
Se diseño el circuito para el sistema de infrarojos, esto para integrarlo al sistema de audiosmart.
