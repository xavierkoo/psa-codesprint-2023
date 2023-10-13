<template>
  <div>
    <h5 class=" mt-3" >Select a job that you are interested:</h5>
    <div
      v-for="(jobRole, index) in jobRolesWithPercentages"
      :key="index"
      class="job-role-item pb-3"
      @click="selectedRole(jobRole)"
    >
      <div
        class="card-body border-bottom rounded p-3 shadow-sm"
        :class="{ 'bg-light border': jobRole.jobRole == roleDetails.jobRole }"
      >
        <div class="row">
          <div class="col-10 col-md-10 col-xl-10 col-xxl-10">
            <h5
              class="card-title"
              :class="{
                'no-underline': jobRole.jobRole != roleDetails.jobRole,
              }"
            >
              <a href="#" class="card-link text-normal">{{
                jobRole.jobRole
              }}</a>
              <span
                class="fw-bold badge rounded-pill bg-light text-dark ms-2"
                style="font-size: small"
                ><span :class="percentageClass(jobRole.percentage)">{{
                  jobRole.percentage
                }}</span>
                % match</span
              >
            </h5>
          </div>
          <div class="col">
            <p class="badge rounded-pill bg-primary text-white p-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-send"
                viewBox="0 0 16 16"
              >
                <path
                  d="M15.854.146a.5.5 0 0 1 .11.54l-5.819 14.547a.75.75 0 0 1-1.329.124l-3.178-4.995L.643 7.184a.75.75 0 0 1 .124-1.33L15.314.037a.5.5 0 0 1 .54.11ZM6.636 10.07l2.761 4.338L14.13 2.576 6.636 10.07Zm6.787-8.201L1.591 6.602l4.339 2.76 7.494-7.493Z"
                />
              </svg>
            </p>
          </div>
        </div>
        <div class="mb-2">
          <div
            v-for="(roleSkill, index2) in jobRole.role_skills"
            :key="index2"
            class="badge rounded-pill bg-light text-dark p-2 me-2"
          >
            {{ roleSkill }}
          </div>
        </div>
        <p class="card-text">
          {{ truncateText(jobRole.role_listing_desc, 150) }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

function truncateText(text, maxLength) {
  if (text.length <= maxLength) {
    return text;
  } else {
    return text.substring(0, maxLength) + "...";
  }
}

const jobRoles = ref([
  {
    jobRole: "Maritime Operations Specialist",
    role_skills: [
      "Maritime Operations",
      "Vessel Traffic Management",
      "Port Security Systems",
    ],
    role_listing_desc:
      "Join our team as a Maritime Operations Specialist to oversee vessel traffic and port security.",
  },
  {
    jobRole: "Cargo Handling Supervisor",
    role_skills: [
      "Cargo Handling and Warehousing",
      "Supply Chain Management",
      "Logistics and Inventory Control",
    ],
    role_listing_desc:
      "We're hiring a Cargo Handling Supervisor to manage warehousing and logistics operations efficiently.",
  },
  {
    jobRole: "Customs Compliance Officer",
    role_skills: [
      "Customs and Trade Compliance",
      "Maritime Safety and Regulations",
    ],
    role_listing_desc:
      "Join us as a Customs Compliance Officer to ensure trade compliance and maritime safety.",
  },
  {
    jobRole: "Port Automation Engineer",
    role_skills: [
      "Port Automation and Robotics",
      "Transportation Management Systems (TMS)",
      "Data Analytics and Reporting",
    ],
    role_listing_desc:
      "We're looking for a Port Automation Engineer to work on automation, TMS, and data analytics projects.",
  },
  {
    jobRole: "Environmental Sustainability Analyst",
    role_skills: [
      "Environmental Sustainability in Ports",
      "Port Infrastructure Design and Engineering",
    ],
    role_listing_desc:
      "Join our team as an Environmental Sustainability Analyst to work on port infrastructure design and sustainability projects.",
  },
  {
    jobRole: "Dredging and Harbor Maintenance Technician",
    role_skills: [
      "Dredging and Harbor Maintenance",
      "Navigational Aids and GPS Systems",
    ],
    role_listing_desc:
      "We're hiring a Dredging and Harbor Maintenance Technician to maintain navigational aids and harbor infrastructure.",
  },
  {
    jobRole: "Port Security Coordinator",
    role_skills: [
      "Port Facility Security Plans (PFSP)",
      "Emergency Response and Crisis Management",
      "Cybersecurity for Maritime Infrastructure",
    ],
    role_listing_desc:
      "Join our team as a Port Security Coordinator to oversee facility security and emergency response plans.",
  },
  {
    jobRole: "Logistics Analyst",
    role_skills: [
      "Logistics and Inventory Control",
      "Intermodal Transportation",
      "RFID and Barcode Technology",
    ],
    role_listing_desc:
      "We're looking for a Logistics Analyst to optimize inventory control and intermodal transportation processes.",
  },
  {
    jobRole: "GIS Specialist",
    role_skills: [
      "Geographic Information Systems (GIS)",
      "Maintenance and Repair of Port Equipment",
    ],
    role_listing_desc:
      "Join us as a GIS Specialist to work on geographic information systems and port equipment maintenance.",
  },
  {
    jobRole: "Communication Systems Manager",
    role_skills: ["Radio Communication and AIS", "Port Planning and Expansion"],
    role_listing_desc:
      "We're hiring a Communication Systems Manager to manage radio communication and port planning projects.",
  },
]);

const props = defineProps({
  staffSkills: {
    type: Object,
    required: true,
    default: () => ({
      staff_skills: ["TBC"],
    }),
  },
});
const percentage = ref(0);

const calPercentage = (roleSkills) => {
  if (roleSkills.length == 0) {
    percentage.value = 100;
  } else if (props.staffSkills.length == 0) {
    percentage.value = 0;
  } else {
    let match = 0;
    for (let i = 0; i < roleSkills.length; i++) {
      for (let j = 0; j < props.staffSkills.length; j++) {
        if (
          roleSkills[i] == props.staffSkills[j].skill &&
          props.staffSkills[j].level >= 50
        ) {
          match++;
        }
      }
    }
    percentage.value = Math.floor((match / roleSkills.length) * 100);
  }
  return percentage.value;
};

function percentageClass(percentage) {
  if (percentage < 50) {
    return "text-danger";
  } else if (percentage < 80) {
    return "text-warning";
  } else {
    return "text-success";
  }
}

const jobRolesWithPercentages = computed(() => {
  // Recalculate the percentages for each job role
  console.log("changed");
  jobRoles.value.forEach((role) => {
    role.percentage = calPercentage(role.role_skills);
  });

  // Sort the job roles based on the calculated percentage in descending order
  return jobRoles.value.sort((a, b) => b.percentage - a.percentage);
});

const roleDetails = ref({
  jobRole: "TBC",
  role_listing_desc: "No description available",
  role_skills: ["TBC"],
});

const emit = defineEmits(["sendData"]);
const selectedRole = (index) => {
  roleDetails.value = {
    jobRole: index.jobRole,
    role_listing_desc: index.role_listing_desc,
    role_skills: index.role_skills,
  };
  console.log(roleDetails.value);
  const response = ref(
    "I am interested in the " +
      roleDetails.value.jobRole +
      " role. " +
      roleDetails.value.role_listing_desc +
      " It is also required that I have "
  );

  for (let i = 0; i < roleDetails.value.role_skills.length; i++) {
    response.value += roleDetails.value.role_skills[i]
    if (i == roleDetails.value.role_skills.length - 1) {
      response.value += "."
    } else {
      response.value += ", "
    }
  }
  emit("sendData", [response.value, roleDetails.value.jobRole]);
};
</script>

<style scoped>
/* Add your component-specific styles here */

:hover .job-role-item {
  cursor: pointer;
} /* Remove underline by default */
.job-role-item .no-underline a {
  text-decoration: none !important;
}

/* Apply underline only when hovering over the specific <a> tag */
.job-role-item:hover .no-underline a {
  text-decoration: underline !important;
}
</style>
