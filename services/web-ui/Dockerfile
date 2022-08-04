FROM php:8.1-apache

RUN pecl install xdebug-3.1.5 \
      && docker-php-ext-enable xdebug

COPY . /var/www/html