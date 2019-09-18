FROM raspbian/stretch

#switch on systemd init system in container
ENV INITSYSTEM on

RUN apt update && apt install -y python3 python3-rpi.gpio python3-requests

COPY . /usr/src/app
WORKDIR /usr/src/app

CMD ["python", "leds.py"]
