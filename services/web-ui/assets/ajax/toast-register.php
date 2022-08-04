<?php
if ($_SERVER['REQUEST_METHOD'] == "POST") {
	if (isset($_POST['register_button'])) {
		$password = $_POST['password'];
		$retype = $_POST['retype'];
		if ($password == $retype) {
			$response = user_register($_POST['name'], $_POST['email_address'], $_POST['password']);
			if ($response['status'] == "error") {
				echo ($response['message']);
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
				<script>
					const toastLiveExample = document.getElementById('liveToast');
					document.getElementById('ToastMessage').innerHTML = "Register Success";
					const toast = new bootstrap.Toast(toastLiveExample);
					toast.show();
				</script>

			<?php
			}
		} else {
			?>
			<script>
				const toastLiveExample = document.getElementById('liveToast');
				document.getElementById('ToastMessage').innerHTML = "Password don't match";
				const toast = new bootstrap.Toast(toastLiveExample);
				toast.show();
			</script>
<?php
		}
	}
}
?>