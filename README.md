# avs-remote-controller
A voice-controlled universal remote using Amazon AVS and Raspberry Pi.

## Getting started
### Prerequisites
This compiler was implemented using __Python 3__ (3.5.3) and it is designed for it. You will need to have this installed prior to usage, along with the __click__ library. To install this, use the following command:


```bash
pip install click
```

### Usage
To use our __ARC__, use the following command:

```bash
python remote-controller.py [OPTIONS] MODE
``` 

Where ```MODE```  is used to specify the mode of operation, only ```cli``` is supported currently.

### Version
This repository stores v0.0 of the our AVS Remote Controller.

## Authors
Copyright © 2019, Sebastián Pérez, Cesar Torres and Erick Durán. CETYS Universidad.

## License
Released under the MIT License.