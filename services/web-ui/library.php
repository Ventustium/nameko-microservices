<?php
require 'function.php';
?>

<div class="container mt-4">
	<form action="library-detail.php" method="POST">
		<div class="row">
			<?php
			foreach (get_libray()['data'] as $row) {
			?>
				<div class="col-lg-3 col-md-4 col-sm-6 mb-2 mb-4 ">
					<div class="card mh-100 mx-auto" style="width: 14rem;">
						<img src="..." class="card-img-top" alt="...">
						<div class="card-body">
							<a class="nounderline text-center text-dark" href="library-detail.php?id=<?= $row['uuid'] ?>">
								<p class="card-title"><?= $row['title'] ?></p>
							</a>
							<!-- <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p> -->
						</div>
					</div>
				</div>
			<?php
			}
			?>
		</div>
	</form>

</div>