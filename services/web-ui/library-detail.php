<?php
include('header.php');
require('function.php');
$uuid = $_GET['id'];
$data = get_libray_detail($uuid)['data'];
?>

<div class="container">
	<div class="container mt-4">
		<div class="row">
			<div class="col-md-4">
				<h4>Title:</h4>
				<p><?= $data['title'] ?></p>
				<h5>Author:</h5>
				<p><?= $data['author'] ?></p>
				<h5>Genre:</h5>
				<p><?= $data['genre'] ?></p>
				<h5>SubGenre:</h5>
				<p><?= $data['subgenre'] ?></p>
				<h5>Height:</h5>
				<p><?= $data['height'] ?></p>
				<h5>Publisher:</h5>
				<p><?php
				if($data['publisher'] == ''){
					echo("Unknown");
				} 
				else {
					echo $data['publisher'];
				} ?> </p>
			</div>

		</div>
	</div>
</div>
<?php
include('footer.php')
?>