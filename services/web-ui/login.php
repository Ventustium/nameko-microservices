<?php
  session_start();

  if(isset($_SESSION['SESSID'])){
	header('Location: index.php');
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
          <a class="nav-link" aria-current="page" href="/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/">Library</a>
        </li>
      </ul>
      <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <li class="nav-item">
            <a class="nav-link active" href="login.php">Login</a>
            </li>
      </ul>
    </div>
  </div>
</nav>

<section class="vh-100" style="background-color: #9A616D;">
	<div class="container py-5 h-100">
		<div class="row d-flex justify-content-center align-items-center h-100">
			<div class="col col-xl-10">
				<div class="card" style="border-radius: 1rem;">
					<div class="row g-0">
						<div class="col-md-6 col-lg-5 d-none d-md-block">
							<img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/img1.webp" alt="login form" class="img-fluid" style="border-radius: 1rem 0 0 1rem;" />
						</div>
						<div class="col-md-6 col-lg-7 d-flex align-items-center">
							<div class="card-body p-4 p-lg-5 text-black">

								<form method="post" action="">

									<div class="d-flex align-items-center mb-3 pb-1">
										<i class="fas fa-cubes fa-2x me-3" style="color: #ff6219;"></i>
										<span class="h1 fw-bold mb-0"></span>
									</div>

									<h5 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Sign into your account</h5>

									<div class="form-outline mb-4">
										<label class="form-label" for="email">Email address</label>
										<input type="email" id="email" name="email" class="form-control form-control-lg" />

									</div>

									<div class="form-outline mb-4">
										<label class="form-label" for="password">Password</label>
										<input type="password" id="password" name="password" class="form-control form-control-lg" />
									</div>

									<div class="pt-1 mb-4">
										<button class="btn btn-dark btn-lg btn-block" type="button" id="button_login">Login</button>
									</div>
									<p class="mb-5 pb-lg-2" style="color: #393f81;">Don't have an account? <a href="register.php" style="color: #393f81;">Register here</a></p>
								</form>

							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<div class="toast-container top-0 end-0 p-3" id="toast_login_container">
	
</div>

<script src="https://code.jquery.com/jquery-3.6.0.js"></script>
<script type="text/javascript">
	$(document).ready(function (){
		$("#button_login").on('click', function (){
			var email = $("#email").val();
			var password = $("#password").val();
			
			$.ajax(
				{
					url: '/assets/ajax/login.php',
					method: 'POST',
					data: {
						login: 1,
						email: email,
						password: password
					},
					success: function (response){
						$("#toast_login_container").html(response);
						const toastLiveExample = document.getElementById('liveToast');
						const toast = new bootstrap.Toast(toastLiveExample);
						toast.show();
						console.log(response);
					}, datatype: 'text'
				}
			)

		});
	});
</script>

<?php
include 'footer.php'
?>