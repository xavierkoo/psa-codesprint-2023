<script setup>
import { ref } from "vue";
</script>

<template>
	<div class="container col-xxl-8 px-4 py-5">
		<div class="row flex-lg-row-reverse align-items-center g-5 py-5">
			<div class="col-10 col-sm-8 col-lg-6">
				<img
					src="https://images.unsplash.com/photo-1577563908411-5077b6dc7624?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"
					class="d-block mx-lg-auto img-fluid"
					alt="Bootstrap Themes"
					width="700"
					height="500"
					loading="lazy"
				/>
			</div>
			<div class="col-lg-6">
				<h1 class="display-5 fw-bold lh-1 mb-3">PortBot</h1>
				<p class="lead">
					PortBot, our virtual HR assistant, streamlines engagement
					from day one. It's not just about reducing administrative
					tasks; it's about creating meaningful connections with
					candidates, ensuring a positive start to their journey with
					us.
				</p>
				<div class="d-grid gap-2 d-md-flex justify-content-md-start">
					<a class="btn btn-primary btn-lg px-4 me-md-2" href="https://portbot-int.streamlit.app/" target="_blank">
						Internal Demo
					</a>
					<a class="btn btn-outline-secondary btn-lg px-4"  href="https://portbot.streamlit.app/" target="_blank">
						External Demo
					</a>
				</div>
			</div>
		</div>
	</div>
</template>
