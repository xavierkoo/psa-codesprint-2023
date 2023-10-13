<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-lg-6 col-12">
        <h2>
          Lighthouse<img
            src="data:image/png;base64,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"
            width="50"
          />
        </h2>
        <h6 class="text-muted fst-italic mb-3">
          Guiding your career ahead, recreating dreams
        </h6>
        <ul class="nav nav-tabs" id="myTab" role="tablist">
          <li class="nav-item" role="presentation">
            <button
              class="nav-link active"
              id="home-tab"
              data-bs-toggle="tab"
              data-bs-target="#home"
              type="button"
              role="tab"
              aria-controls="home"
              aria-selected="true"
            >
              Technical Skills
            </button>
          </li>
          <li class="nav-item" role="presentation">
            <button
              class="nav-link"
              id="profile-tab"
              data-bs-toggle="tab"
              data-bs-target="#profile"
              type="button"
              role="tab"
              aria-controls="profile"
              aria-selected="false"
            >
              Soft Skills
            </button>
          </li>
          <li class="nav-item" role="presentation">
            <button
              class="nav-link"
              id="contact-tab"
              data-bs-toggle="tab"
              data-bs-target="#contact"
              type="button"
              role="tab"
              aria-controls="contact"
              aria-selected="false"
            >
              Jobs
            </button>
          </li>
        </ul>
        <div class="tab-content" id="myTabContent">
          <div
            class="tab-pane fade show active"
            id="home"
            role="tabpanel"
            aria-labelledby="home-tab"
          >
            <TechnicalSkills @sendData="promptTechSkill" />
          </div>
          <div
            class="tab-pane fade"
            id="profile"
            role="tabpanel"
            aria-labelledby="profile-tab"
          >
            <SoftSkills @sendData="promptSoftSkill" />
          </div>
          <div
            class="tab-pane fade"
            id="contact"
            role="tabpanel"
            aria-labelledby="contact-tab"
          >
            <Jobs :staff-skills="PTSList" @sendData="promptRoleDetail" />
          </div>
        </div>
      </div>
      <div class="col">
        <h2>Gaps and Roadmap recommandations</h2>
        <button
          class="btn btn-primary mt-3"
          @click="fetchData"
          :disabled="
            parentRoleDetail == '' ||
            parentSoftSkill == '' ||
            parentTechSkill == ''
          "
        >
          Get Feedback <span v-if="jobRole">for</span> {{ jobRole }}
        </button>
        <ol class="my-3 fw-bold">
          <li :hidden="parentTechSkill != ''">Fill in Technical Skills</li>
          <li :hidden="parentSoftSkill != ''">Fill in Soft Skills</li>
          <li :hidden="parentRoleDetail != ''">Select an interested Job</li>
        </ol>
        <div v-if="loading" class="text-center">
          <loader />
        </div>
        <div v-if="responseData.job_fit != 'NA'">
          <h5>
            Base on our analysis, you are {{ responseData.job_fit }} for this
            job.
          </h5>
          <h5 class="mt-3 text-muted">Technical Skills Recommendations:</h5>
          <ul>
            <li v-for="skill in responseData.technical_skills_recommendations">
              {{ skill }}
            </li>
          </ul>
          <hr />
          <h5 class="mt-3 text-muted">Soft Skills Recommendations:</h5>
          <ul>
            <li v-for="skill in responseData.soft_skills_recommendations">
              {{ skill }}
            </li>
          </ul>
          <hr />
          <h5 class="mt-3 text-muted">Personalised Career Roadmap:</h5>
          <ul>
            <li v-for="skill in responseData.personalise_career_roadmap">
              {{ skill }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import TechnicalSkills from "../components/TechnicalSkill.vue";
import SoftSkills from "../components/SoftSkill.vue";
import Jobs from "../components/Jobs.vue";
import { ref } from "vue";
import loader from "../components/loader.vue";

import axios from "axios";

const loading = ref(false);

const responseData = ref({
  job_fit: "NA",
  technical_skills_recommendations: ["NA"],
  soft_skills_recommendations: ["NA"],
  personalise_career_roadmap: ["NA"],
  // job_fit: "Not a strong fit",
  // technical_skills_recommendations: [
  //   "Obtain formal training or certification in Supply Chain Management",
  //   "Gain more experience and knowledge in Maritime Operations",
  // ],
  // soft_skills_recommendations: [
  //   "Develop public speaking and presentation skills",
  //   "Enhance active listening skills",
  //   "Improve written communication skills",
  //   "Work on adapting communication style to different audiences",
  //   "Learn additional conflict resolution strategies",
  //   "Further develop skills in building relationships and networks",
  //   "Enhance ability to handle change and uncertainty",
  //   "Continuously seek opportunities to lead and influence",
  //   "Strengthen problem-solving skills in complex situations",
  //   "Work on involving others in the decision-making process",
  //   "Continuously develop emotional intelligence, particularly in managing and regulating emotions effectively",
  // ],
  // personalise_carrer_roadmap: [
  //   "Take courses or workshops on conflict resolution and mediation to further strengthen skills in managing conflicts within a team",
  //   "Participate in public speaking or presentation workshops to enhance communication skills in speaking to larger audiences",
  //   "Seek out opportunities to lead or manage projects to gain formal leadership experience",
  //   "Enroll in courses or training programs on supply chain management and logistics to deepen technical knowledge in these areas",
  //   "Participate in workshops or seminars on emotional intelligence to further develop skills in recognizing and managing emotions in the workplace",
  // ],
});

const content = ref("");
async function fetchData() {
  content.value =
    parentRoleDetail.value + parentTechSkill.value + parentSoftSkill.value;
  loading.value = true;
  try {
    const response = await axios.post("http://localhost:8080/generate_chat", {
      // Replace with your API key
      content: content.value,
    });
    console.log(response.data);
    responseData.value = JSON.parse(response.data);
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
}

const jobRole = ref("");
const parentRoleDetail = ref("");
const promptRoleDetail = (data) => {
  parentRoleDetail.value = data[0];
  jobRole.value = data[1];
};

const parentTechSkill = ref("");
const PTSList = ref([]);
function promptTechSkill(data) {
  parentTechSkill.value = data[0];
  PTSList.value = data[1];
}

const parentSoftSkill = ref("");
const promptSoftSkill = (data) => {
  parentSoftSkill.value = data;
};
</script>
<style scoped></style>
