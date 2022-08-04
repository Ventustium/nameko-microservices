<?php
  session_start();

$home = "";
$library = "";
$login = "";
$status = "";
if (str_contains($_SERVER['REQUEST_URI'], '/library')) { 
  $library = "active";
}


if ($_SERVER['REQUEST_URI'] == '/') { 
  $home = "active";
}

if ($_SERVER['REQUEST_URI'] == '/login.php') { 
  $login = "active";
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
      
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="assets/css/bootstrap.min.css" rel="stylesheet">
      <link href="assets/css/main.css" rel="stylesheet">
      <script src="assets/js/bootstrap.bundle.min.js"></script>
      <title>Nameko Library</title>
</head>

<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Nameko <strong>Library</strong></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-lg-0">
        <li class="nav-item">
          <a class="nav-link <?= $home ?>" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link <?= $library ?>" href="/">Library</a>
        </li>
      </ul>
      <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <?php
              if(isset($_SESSION['SESSID'])){
              
              ?>
            <a class="nav-link <?= $login ?> " href="logout.php">Logout</a>
            <?php
              } else{
            ?>
            <a class="nav-link <?= $login ?> " href="login.php">Login</a>
            <?php
            }
            ?>
            </li>
      </ul>
    </div>
  </div>
</nav>