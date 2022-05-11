#! python3
####################################################################################################

import os
import sys

import fastapi
import uvicorn
import wakeonlan

####################################################################################################

C_WOL_HOST = 'localhost'
C_WOL_PORT = 30502

####################################################################################################

app = fastapi.FastAPI()

####################################################################################################

@app.get  ( '/WOL/{Mac}',
            status_code    = 204,
            response_class = fastapi.Response
          )
async def WOL(Mac : str):
    try:
        wakeonlan.send_magic_packet(Mac)

    except ValueError:
        raise fastapi.HTTPException(status_code=400, detail=f'''Illegal MAC address: {Mac}\n''')
        
    except Exception as l_Exception:
        raise fastapi.HTTPException(status_code=500, detail=f'''Unknown exception: {l_Exception}\n''')
 
####################################################################################################

def main():
    return app

##################################################

if __name__ == '__main__':
    l_Host = os.environ.get('WOL_HOST', C_WOL_HOST)
    l_Port = os.environ.get('WOL_PORT', C_WOL_PORT)

    try:
        l_Port = int(l_Port)
    except ValueError:
        print(f'''Error: {l_Port} is not a valid port number''')
        sys.exit(1)

    uvicorn.run('WOL:main', host=l_Host, port=l_Port, log_level='info')

####################################################################################################

