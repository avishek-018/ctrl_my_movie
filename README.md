# Control My Movie

It's fun type mini script on python. Suppose you and your friend are watching a same movie but on different laptops.
Your friend Can control your media player.
Like, he/she can pause/mute/volume_up/volume_down/forward/rewind .

## Supported Media Players
1. Pot Player
2. KM Player

## Installation
1. Clone the repo
```bash
git clone 
```
2. Install requirements
```bash
pip install -r requirements.txt
```


### or
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install necessary packages.
1. python-firebase
2. pynput

```bash
pip install python-firebase,pynput
```
## Database Setup
You need a central database to pass the controls.

Firebase is handy.

##### 1. Setup a Firebase Realtime Database Just like the structure below.

![image](https://user-images.githubusercontent.com/19516280/58494446-efd06400-8196-11e9-883a-533bd03f6239.png)
##### 2. Change both the 'controller' and 'simulator' files as below.

```python
dbase = 'https://database_name.firebaseio.com/' #use your firebase database destination here
```



## Usage
##### If you want to control
1. Run the controller.py in your machine.
2. Run the simulator.py in your friend's machine.

##### If you want to be controlled
1. Run the simulator.py in your machine.
2. Run the controller.py in your friend's machine.

==> Press Esc Button Anytime to Exit
## Contributing
Pull requests are welcome. 

## Project status
Currently this is working in a simplex method(one way communication).
Enthusiasts are welcome to develop it.

Please make sure to update tests as appropriate.
