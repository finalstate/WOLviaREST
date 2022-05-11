#! python3
####################################################################################################

import fastapi
import uvicorn
import wakeonlan

####################################################################################################

app = fastapi.FastAPI()

####################################################################################################

@app.get  ( "/WOL/{Mac}",
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

if __name__ == "__main__":
    uvicorn.run("WOL:main", host="0.0.0.0", port=30502, log_level="info")

####################################################################################################

