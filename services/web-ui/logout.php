<?php
require('function.php');
if(session_status() != 2)
session_start();

user_logout();
header('Location: login.php');

session_unset();
session_destroy();
?>