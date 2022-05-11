# docker build -t wol .

FROM     python:3.10-bullseye AS base-shell
LABEL    maintainer=rene.schmit@plaakert.lu

ENV      TZ=Europe/Luxembourg
ENV      WOL_HOST=0.0.0.0
ENV      WOL_PORT=30502

COPY     ./requirements.txt /code/requirements.txt
RUN      pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE   30502

COPY     ./WOL.py /code/WOL.py

WORKDIR  /code
CMD      python3 WOL.py

