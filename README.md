# avs-remote-controller
A voice-controlled universal remote using Amazon AVS and Raspberry Pi.

## Getting started
### Prerequisites
This compiler was implemented using __Python 3__ (3.5.3) and it is designed for it. You will need to have this installed prior to usage, along with some additional modules. To install these dependencies, use the following command:


```bash
pip3 install -r requirements.txt
```

### Usage
To use our __ARC__, use the following command:

```bash
python3 remote-controller/main.py MODE [OPTIONS]
``` 

- `MODE` is used to specify the mode of operation, current modes are `cli` and `api`.

Some available options are:
- `-d` or `--device`: the name of the device, configured with `lirc`, necessary for `cli` mode.
- `-r` or `--review_mode`: option that doesn't execute the commands, just for testing if everything is working properly and simulations.

## Running the tests
For this project, we used the `unittest` framework to create our unit tests. In order to run them, run the following command:

```bash
python3 -m unittest discover -s remote-controller/tests -t remote-controller/tests -p *_test.py
```

### Version
This repository stores v1.0 of the our AVS Remote Controller.

## Authors
Copyright © 2019, Sebastián Pérez, Cesar Torres and Erick Durán. CETYS Universidad.

## License
Released under the MIT License.