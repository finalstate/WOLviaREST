# docker build -t dpython .

FROM     python:3.14-bullseye AS base-shell
LABEL    maintainer=rene.schmit@plaakert.lu

ENV      TZ=Europe/Luxembourg

COPY     ./requirements.txt /code/requirements.txt
RUN      pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE   30502

COPY     ./WOL.py /code/WOL.py

WORKDIR  /code
CMD      python3 WOL.py

