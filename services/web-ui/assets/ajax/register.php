<?php
require '../../function.php';
 
if (isset($_POST['register'])) {
	if(filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)){
	$password = $_POST['password'];
	$retype = $_POST['retype'];
	if ($password == $retype) {
		$response = user_register($_POST['name'], $_POST['email'], $_POST['password']);
		if ($response['status'] == "error") {
?>
			<div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
				<div class="toast-header">
					<div id="toast-logo">
						<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="red" class="bi bi-x-circle-fill" viewBox="0 0 16 16">
							<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z" />
						</svg>
					</div>
					<strong class="ms-2 me-auto" id="ToastHeader">Failed</strong>
					<button type="submit" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>

				</div>
				<div class="toast-body">
					<p id="ToastMessage"><?= $response['message'] ?></p>
				</div>
			</div>
		<?php
		} else {
		?>
			<div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
				<div class="toast-header">
					<div id="toast-logo">
						<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="green" class="bi bi-check-circle-fill" viewBox="0 0 16 16">
							<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z" />
						</svg>
					</div>
					<strong class="ms-2 me-auto" id="ToastHeader">Register Success</strong>
					<button type="submit" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>

				</div>
				<div class="toast-body">
					<p id="ToastMessage">Please Login</p>
				</div>
			</div>
			
			<script>
				setTimeout(function() {
					window.location='login.php'
				}, 2500);
			
			</script>
		<?php
		}
	} else {
		?>

		<div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
			<div class="toast-header">
				<div id="toast-logo">
					<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="red" class="bi bi-x-circle-fill" viewBox="0 0 16 16">
						<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z" />
					</svg>
				</div>
				<strong class="ms-2 me-auto" id="ToastHeader">Failed</strong>
				<button type="submit" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>

			</div>
			<div class="toast-body">
				<p id="ToastMessage">Password don't match</p>
			</div>
		</div>
<?php
	}
}
else{
	?>

		<div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
			<div class="toast-header">
				<div id="toast-logo">
					<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="red" class="bi bi-x-circle-fill" viewBox="0 0 16 16">
						<path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z" />
					</svg>
				</div>
				<strong class="ms-2 me-auto" id="ToastHeader">Failed</strong>
				<button type="submit" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>

			</div>
			<div class="toast-body">
				<p id="ToastMessage">Please input valid email</p>
			</div>
		</div>
<?php
}
}
?>