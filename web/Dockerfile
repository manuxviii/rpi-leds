FROM ulsmith/rpi-raspbian-apache-php
MAINTAINER contact@manuxviii.ovh

RUN rm /var/www/html/index.html
COPY . /var/www/html
RUN chmod -R 0766 /var/www/html

EXPOSE 80
CMD ["/run.sh"]
