<?php
if(session_status() != 2)
session_start();

require 'vendor/autoload.php';
require 'api-url.php';

use GuzzleHttp\Client;
use GuzzleHttp\Psr7\Response;
use GuzzleHttp\Exception\RequestException;
use GuzzleHttp\Exception\ClientException;
use GuzzleHttp\Cookie\CookieJar;

$client = new Client(['base_uri' => 'http://nginx', 'cookies' => true]);

if(isset($_SESSION['SESSID'])){
      $cookieJar = CookieJar::fromArray([
            'SESSID' => $_SESSION['SESSID']
        ], 'nginx');
}
else{
      $cookieJar = CookieJar::fromArray([
            'SESSID' => ''
        ], 'nginx');
}

function get_libray(){
      global $client;
      $response = $client->request('GET', '/api/library/lightnovel', []);
      return json_decode($response->getBody(), true);
}

function get_libray_detail($uuid){
      global $client;
      $response = $client->request('GET', '/api/library/lightnovel/detail/'.$uuid, []);
      return json_decode($response->getBody(), true);
}

function get_libray_async(){
      global $client;
      $response = $client->requestAsync('GET', '/api/library/lightnovel', []);

      $response->then(
            function (Response $res){
                  echo $res->getBody();
            },
            function (RequestException $e){
                  echo $e->getMessage();
            }
      );
      $response->wait();
}

function user_register($name, $email_address, $password){
      global $client;
     
      try {
            $response = $client -> request('POST', '/api/user', [
                  'json' => [
                        'name' => $name,
                        'email_address' => $email_address,
                        'password' => $password,
                  ]
            ]);
            return json_decode($response->getBody(), true);
      } catch (ClientException $e){
            $response = $e->getResponse();
            return json_decode($response->getBody(), true);
      }
      
}

function user_login($name, $password){
      global $client, $cookieJar;

      try {
            $response = $client -> request('POST', '/api/user/login', [
                  'cookies' => $cookieJar,
                  'json' => [
                        'email_address' => $name,
                        'password' => $password,
                  ]
            ]);
            if ($response->hasHeader('Content-Length')) {
                  $cookie = $response->getHeader('set-cookie');
                  $cookie = explode(";", $cookie[0]);
                  $sessionid = explode("=", $cookie[0]);
                  
                  $cookie_name = $sessionid[0];
                  $cookie_value = $sessionid[1];

                  $response = json_decode($response->getBody(), true);
                  $response['cookie']['name'] = $cookie_name;
                  $response['cookie']['value'] = $cookie_value;
                  $_SESSION['SESSID'] = $cookie_value;
                  return($response);
              }
              
              
      }catch (ClientException $e){
            $response = $e->getResponse();
            return (json_decode($response->getBody(), true));
      }catch(RequestException $e){
            $response = $e->getResponse();
            return (json_decode($response->getBody(), true));
      }
}

function user_logout(){
      global $client, $cookieJar;
      
      
      try {
            $response = $client -> request('POST', '/api/user/logout', [
                  'cookies' => $cookieJar
            ]);

            if ($response->hasHeader('Content-Length')) {
                  
              }
            // var_dump(json_decode($response->getBody(), true));
              
      }catch (ClientException $e){
            $response = $e->getResponse();
            // var_dump(json_decode($response->getBody(), true));
      }catch(RequestException $e){
            // var_dump($e);
      }
} 
?>