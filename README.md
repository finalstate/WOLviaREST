# Minimal REST server to send a WakeOnLan magic packet to a server.

## Requirements

You need to have a working python3 installation on your computer.

Additionally, WOLviaREST depends on the following 4 libraries:

- fastapi
- uvicorn
- pydantic
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

### From Git repository

In the source directory, execute
```
python3 WOL.py
```


You may change the host and port by setting the following environment variables:

```
export WOL_HOST=0.0.0.0
export WOL_PORT=8009
```

### Using Docker

Alternatively, you can create and run a docker image/container:


```
docker image build -t wol .
docker run -itd --network host --name wol wol
```

*Remark*: We need to use the host network to send the magic token...

Change the Host and Port in the dockerfile.

## API Usage

Then use the following URL to send the WakeOnLan packet

[http://localhost:30502/WOL/](http://localhost:30502/WOL/01:23:45:67:89:ab)

passing the MAC address at the very end of the URL. Using curl, it looks like this
```
curl -X GET http://localhost:30502/WOL/01:23:45:67:89:ab
```

See also the [Swagger page](http://localhost:30502/docs), available when your WOLviaREST server is running.


**DISCLOSURE** : 
this project is mainly a test bed to play with GitHub. Very minimal (but working, so might be useful). See also in the [Wiki](https://github.com/finalstate/WOLviaREST/wiki)
