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
python3 cli.py MODE [OPTIONS]
``` 

- `MODE` is used to specify the mode of operation, current modes are `cli`, `api`, `alexa` and `training`.

Some available options are:
- `-d` or `--device`: the name of the device, configured with `lirc`, necessary for `cli`, `api`, `alexa` and `training` modes.
- `-r` or `--review_mode`: option that doesn't execute the commands, just for testing if everything is working properly and simulations.

## Modes

### `cli`
This mode is created as an interactive interface to use your `lirc` commands directly from your bash console. The device should be configured properly in `lirc` in order for it to work. You may use raw commands (as defined in `lirc`) by starting your command with `raw`, or composite commands, which let you interact in a more user-friendly way (e.g. `POWER`, `CHANNEL 15`, etc.).

### `api`
A REST API to interact with the CLI wirelessly. Review mode may be used to interact with the CLI without sending actual commands.

### `training`
This mode creates the `lirc` configuration for a new device. You may use this option or do it by yourself. Please remember to move your configuration file to the corresponding `lirc` directory.

### `alexa`
An API to interact with _Alexa Voice Service_. This API uses the `flask-ask` library to parse AVS requests and send the corresponding commands using `lirc`. You may find the skill interaction model under `resources/alexa`.

## Running the tests
For this project, we used the `unittest` framework to create our unit tests. In order to run them, run the following command:

```bash
python3 -m unittest discover -s tests -t tests -p *_test.py
```

### Version
This repository stores v1.0 of the our AVS Remote Controller.

## Authors
Copyright © 2019, Sebastián Pérez, Cesar Torres and Erick Durán. CETYS Universidad.

## License
Released under the MIT License.