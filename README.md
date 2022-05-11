# Minimal REST server to send a WakeOnLan magic packet to a server.

## Requirements

You need to have a working python3 installation on your computer.

Additionally, WOLviaREST depends on the following 3 libraries:

- fastapi
- uvicorn
- wakeonlan

They can be installed with:

```
pip3 install -r requirements.txt
```

## Installation

Clone the directory using:

```
git clone https://github.com/finalstate/WOLviaREST.git
```

## Running

In the source directory, execute
```
python3 WOL.py
```
Then use the following URL to send the WakeOnLan packet

[http://localhost:30502/WOL/](http://localhost:30502/WOL/01:23:45:67:89:ab)

passing the MAC address at the very end of the URL. Using curl, it looks like this
```
curl -X GET http://localhost:30502/WOL/01:23:45:67:89:ab
```

You may change the host and port by setting the following environment variables:

```
export WOL_HOST=0.0.0.0
export WOL_PORT=8009
```


**DISCLOSURE** : 
this project is mainly a test bed to play with GitHub. Very minimal (but working, so might be useful). See also in the [Wiki](https://github.com/finalstate/WOLviaREST/wiki)
