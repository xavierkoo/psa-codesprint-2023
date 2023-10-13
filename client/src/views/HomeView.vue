<script setup>
import { ref } from "vue";

// randomly select a motivation message
const motivationMessages = [
	"Believe in yourself, for you are capable of achieving greatness beyond your wildest dreams.",
	"Every small step you take today brings you closer to your big goals tomorrow. Keep moving forward!",
	"Success is not the absence of failure; it's the determination to keep going despite it.",
	"Your potential knows no bounds. Embrace the challenges, and let them fuel your growth.",
	"The road to success may be steep, but the view from the top is worth every climb.",
	"You have the power to turn your dreams into reality. Stay focused, work hard, and never give up.",
	"Don't wait for the perfect moment; take the moment and make it perfect.",
	"Every day is a new opportunity to become a better version of yourself. Seize it!",
	"Challenges are like weights in the gym; they make you stronger. Embrace them!",
	"You are the author of your own story. Write a tale of resilience, determination, and success.",
	"Success is not about being the best; it's about being better than you were yesterday.",
	"Your journey may be tough, but so are you. Keep pushing forward, and you'll reach your destination.",
	"The only way to predict the future is to create it. Start writing your success story today.",
	"Every setback is a setup for a comeback. Keep going, and your comeback will be legendary.",
	"You are capable of achieving greatness, and your efforts today are the building blocks of your tomorrow.",
	"Remember, the only limit that exists is the one you place on yourself. Break free and soar!",
	"Success is not about luck; it's about persistence, hard work, and unwavering belief in yourself.",
	"Your journey may be challenging, but each obstacle is an opportunity to grow stronger and wiser.",
	"The path to success is not a straight line; it's a series of steps, stumbles, and lessons. Keep walking.",
	"You are stronger than you think, and your potential is limitless. Keep striving for your dreams!",
];

const users= [
  "Ray Quek",
  "Aaron Kwah",
  "Maurice Ho",
  "Xavier Koo",
]

const user = ref(
  users[Math.floor(Math.random() * users.length)]
);


const motivationMessage = ref(
	motivationMessages[Math.floor(Math.random() * motivationMessages.length)]
);
</script>

<template>
	<main class="home-page mx-3">
		<div
			class="px-4 py-5 my-5 text-center border-bottom"
			style="background-color: white"
		>
			<!-- Add a logo in the center -->
			<img
				class="d-block mx-auto mb-4"
				src="https://cdn.icon-icons.com/icons2/2699/PNG/512/docker_tile_logo_icon_168248.png"
				alt=""
				width="200"
				height="200"
			/>
			<h1 class="display-5 fw-bold">Welcome to Opportunity Portal</h1>
			<div class="col-lg-6 mx-auto">
				<p class="lead mb-4">
					Where we start digitally transforming traditional
					interactions in the End-to-End Employee Lifecycle Solution
				</p>
			</div>
		</div>

		<div class="container col-xxl-8 px-4">
			<div class="row flex-lg-row-reverse align-items-center g-5 py-5">
				<div class="col-10 col-sm-8 col-lg-6">
					<img
						src="https://images.unsplash.com/photo-1561702469-c4239ced3f47?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1932&q=80"
						class="d-block mx-lg-auto img-fluid"
						alt="Bootstrap Themes"
						width="700"
						height="500"
						loading="lazy"
					/>
				</div>
				<div class="col-lg-6">
					<h1 class="display-5 fw-bold lh-1 mb-3">
						Welcome Back <br /><strong>{{user}}</strong>
					</h1>
					<h2 class="fw-bold lh-1 mb-3">Daily Motivation Message</h2>
					<p class="lead">{{ motivationMessage }}</p>
					<div
						class="d-grid gap-2 d-md-flex justify-content-md-start"
					></div>
				</div>
			</div>
		</div>

		<div class="row justify-content-center align-items-center g-2 px-4">
			<div class="col">
				<router-link to="/portbot" style="text-decoration: none">
					<div class="card">
						<img
							src="https://images.unsplash.com/photo-1577563908411-5077b6dc7624?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"
							class="card-img-top"
							alt="..."
						/>
						<div class="card-body">
							<h5 class="card-title">PortBot</h5>
							<p class="card-text">
								Streamlining Talent Management
							</p>
						</div>
					</div>
				</router-link>
			</div>
			<div class="col">
				<router-link to="/lighthouse" style="text-decoration: none">
					<div class="card">
						<img
							src="https://images.unsplash.com/photo-1559061156-4a46ec29107d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"
							class="card-img-top"
							alt="..."
						/>
						<div class="card-body">
							<h5 class="card-title">LightHouse</h5>
							<p class="card-text">Empowering Employee Growth</p>
						</div>
					</div>
				</router-link>
			</div>
			<div class="col">
				<router-link
					to="/portconnections"
					style="text-decoration: none"
				>
					<div class="card">
						<img
							src="https://images.unsplash.com/photo-1545987796-200677ee1011?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"
							class="card-img-top"
							alt="..."
						/>
						<div class="card-body">
							<h5 class="card-title">PortConnections</h5>
							<p class="card-text">
								Cultivating Well-Being and Culture
							</p>
						</div>
					</div>
				</router-link>
			</div>
		</div>
	</main>
</template>

<style scoped="scss">
/* Custom CSS for the text overlay */
.image-container {
	position: relative;
}

.overlay-text {
	position: absolute;
	top: 0;
	left: 0;
	background-color: rgba(0, 0, 0, 0.5); /* Background color with opacity */
	color: #fff; /* Text color */
	padding: 20px; /* Adjust padding as needed */
}

.overlay-text h2 {
	font-size: 24px; /* Adjust font size */
}
</style>
