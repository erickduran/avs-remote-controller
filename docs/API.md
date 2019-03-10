# avs-remote-controller API

## Objetivo
El presente documento tiene como objetivo principal documentar el uso del API para enviar instrucciones a la TV a través de peticiones HTTP.


## Requisitos
- Software cliente HTTP
- Conocimientos básicos sobre peticiones HTTP

## Comandos
La versión actual de la implementación del presente proyecto acepta __dos__ tipos de comandos, comandos "directos" (_raw-commands_) y commandos simples (_commands_). 

Los __comandos directos__ son los comandos implementados por la librería `lirc`, los cuales hacen referencia directamente a las teclas del control de televisión. Algunos ejemplos de estos comandos son:
- `KEY_POWER`
- `KEY_VOLUMEUP`
- `KEY_CHANNELDOWN`
- `KEY_3`

La lista completa de los comandos directos se pueden encontrar [aquí](https://github.com/erickduran/avs-remote-controller/blob/master/remote-controller/resources/commands/raw-commands.yml).

Los __comandos simples__ son una versión simplificada implementada por los miembros del equipo para facilitar la interacción con el control. Algunos ejemplos son:
- `POWER`
- `CHANNEL 315`
- `VOLUME_UP`

Como puede verse, algunos de estos comandos aceptan parámetros adicionales, los cuales evitan enviar `KEY_3`, `KEY_1` y `KEY_5`, y en su lugar se envía `CHANNEL 315`. Adicionalmente, los nombres se simplifican quitando la cadena `KEY_`.

La lista completa de los comandos simples se pueden encontrar [aquí](https://github.com/erickduran/avs-remote-controller/blob/master/remote-controller/resources/commands/commands.yml).

## Peticiones
En la etapa actual del proyecto, el API permite enviar peticiones `POST` al _endpoint_ __vcrc.erickduran.com:5000__. Las peticiones toman los siguientes parámetros como `body` en formato `application/json`:
- `raw-command`: booleano para indicar si se trata de un comando directo (`true`) o simple (`false`).
- `command`: nombre del comando a enviar.
- `value` (opcional): parámetro adicional para comandos que acepten valores. En caso de que no se especifique, se utilizará el valor por defecto.

### Ejemplo para comandos directos

```json
{
	"raw-command" : true,
	"command" : "KEY_POWER"
}
```


### Ejemplo para comandos simples

```json
{
	"raw-command" : false,
	"command" : "CHANNEL_UP"
}
```

### Ejemplo para comandos simples con valores adicionales

```json
{
	"raw-command" : false,
	"command" : "CHANNEL",
	"value" : 315
}
```

### Ejemplo para obtener ayuda sobre un comando específico
```json
{
	"help" : "SETTINGS"
}
```