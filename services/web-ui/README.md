# User Interface (Website) using Apache PHP

If you want to build your own WebUI you need to install Apache, PHP First.
<br>
There's a lot of tutorial on the Internet, so you can use that one

I will install php8.0 on my Machine
```
$ sudo apt install php8.0 -y
```

And I will use Bootstrap 5.2
```
$ mkdir assets/
$ cd assets/
$ mkdir css js
$ wget https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css -P css
$ wget https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js -P js
```

For the HTTP Client, I will use Guzzle
```
curl -sS https://getcomposer.org/installer | php
composer require guzzlehttp/guzzle:^7.4.5
```