<?php
require('function.php');
include('header.php');
$uuid = $_GET['id'];
$data = get_libray_detail($uuid)['data'];
?>

<div class="container">
	<div class="container mt-4">
		<div class="row">
			<div class="col-md-4">
				<h4>Title:</h4>
				<p><?= $data['title'] ?></p>
				<h4>Description:</h4>
				<p><?= $data['description'] ?></p>
			</div>

		</div>
	</div>
</div>
<?php
include('footer.php')
?>