<?php
include 'header.php';
require 'function.php';
?>

<section class="vh-100" style="background-color: #9A616D;">
	<div class="container py-5 h-100">
		<div class="row d-flex justify-content-center align-items-center h-100">
			<div class="col col-xl-10">
				<div class="card" style="border-radius: 1rem;">
					<div class="row g-0">
						<div class="col-md-6 col-lg-7 d-flex align-items-center">
							<div class="card-body p-4 p-lg-5 text-black">

								<form action="" method="post">

									<div class="d-flex align-items-center mb-3 pb-1">
										<i class="fas fa-cubes fa-2x me-3" style="color: #ff6219;"></i>
										<span class="h1 fw-bold mb-0"></span>
									</div>

									<h5 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Register</h5>

									<div class="form-outline mb-4">
										<label class="form-label" for="name">Your name</label>
										<input type="text" id="name" name="name" class="form-control form-control-lg" required/>
									</div>

									<div class="form-outline mb-4">
										<label class="form-label" for="email">Email address</label>
										<input type="email" id="email" name="email_address" class="form-control form-control-lg" required/>
									</div>

									<div class="form-outline mb-4">
										<label class="form-label" for="name">Password</label>
										<input type="password" id="password" name="password" value="" class="form-control form-control-lg" required/>
									</div>
									<div class="form-outline mb-4">
										<label class="form-label" for="retype">Re-type password</label>
										<input type="password" id="retype" name="retype" value="" class="form-control form-control-lg" required/>
									</div>
									<div class="pt-1 mb-4">
										<button class="btn btn-dark btn-lg btn-block" type="button" id="button_register" name="register_button" value="1">Register</button>
									</div>
									<p class="mb-5 pb-lg-2" style="color: #393f81;">Already have account? <a href="login.php" style="color: #393f81;">Login here</a></p>
								</form>

							</div>
						</div>
						<div class="col-md-6 col-lg-5 d-none d-md-block">
							<img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/img1.webp" alt="login form" class="img-fluid" style="border-radius: 1rem 0 0 1rem;" />
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<div class="toast-container top-0 end-0 p-3" id="toast_register_container">
	
</div>

<script src="https://code.jquery.com/jquery-3.6.0.js"></script>
<script type="text/javascript">
	$(document).ready(function (){
		$("#button_register").on('click', function (){
			var name = $("#name").val();
			var email = $("#email").val();
			var password = $("#password").val();
			var retype = $("#retype").val();
			
			$.ajax(
				{
					url: '/assets/ajax/register.php',
					method: 'POST',
					data: {
						register: 1,
						name: name,
						email: email,
						password: password,
						retype: retype
					},
					success: function (response){
						$("#toast_register_container").html(response);
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