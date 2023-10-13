<template>
  <h5 class="form-label mt-3">Choose a skill:</h5>
  <div class="dropdown">
    <input
      type="text"
      class="form-control mt-3"
      @focus="showSkills"
      v-model="searchQuery"
      @input="filterSkills"
      placeholder="Search for a skill"
    />
    <ul class="dropdown-list text-start" v-if="showSkillsList" @click.stop>
      <li
        v-for="(skill, index) in filteredSkills"
        :key="index"
        @click="selectSkill(skill)"
        :class="{ active: selectedSkill === skill }"
      >
        {{ skill }}
      </li>
    </ul>
  </div>
  <div>
    <h5 class="form-label mt-3">Skill Level:</h5>
    <div
      class="form-check form-check-inline"
      v-for="(label, value) in skillLevels"
    >
      <input
        class="form-check-input"
        type="radio"
        :value="value"
        v-model="selectedLevel"
        :id="'skillLevel_' + value"
        :disabled="selectedSkill == ''"
      />
      <label class="form-check-label" :key="value">
        {{ label }}
      </label>
    </div>
    <br />
    <button
      :disabled="selectedSkill == ''"
      class="btn btn-primary mt-3"
      @click="addToTSList"
    >
      Add
    </button>
    <hr />

    <div v-for="(v, k) in TSList" class="card">
      <div class="card-body">
        <p>{{ v.skill }} - {{ v.title }}</p>
        <div class="progress">
          <div
            class="progress-bar"
            role="progressbar"
            :style="{
              width: v.level + '%',
              backgroundColor:
                v.level < 50 ? 'orange' : v.level < 75 ? '#a1eb34' : 'green',
            }"
            aria-valuenow="50"
            aria-valuemin="0"
            aria-valuemax="100"
          ></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, defineEmits } from "vue";

const searchQuery = ref("");
const filteredSkills = ref([]);
const showSkillsList = ref(false);
const selectedSkill = ref(""); // Store the selected skill

const skillLevels = {
  0: "No Experience",
  25: "Beginner",
  50: "Intermediate",
  75: "Expert",
  100: "Professional",
};

const selectedLevel = ref(0);

const filterSkills = () => {
  filteredSkills.value = technicalSkills.filter((skill) =>
    skill.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
};

const hideSkills = () => {
  showSkillsList.value = false; // Hide the filtered list when input loses focus
  window.removeEventListener("click", onClickOutside);
};

const showSkills = () => {
  filterSkills(); // Apply filtering before showing
  showSkillsList.value = true;
};

const selectSkill = (skill) => {
  selectedSkill.value = skill; // Set the selected skill
  searchQuery.value = skill;
  console.log(skill);
  showSkillsList.value = false; // Hide the filtered list when a skill is selected
};

const onClickOutside = (event) => {
  if (!event.target.closest(".dropdown")) {
    hideSkills();
  }
};
onMounted(() => {
  return () => {
    window.removeEventListener("click", onClickOutside);
  };
});
const emit = defineEmits(["sendData"]);
const TSList = ref([]);
const addToTSList = () => {
  TSList.value.push({
    skill: selectedSkill.value,
    level: selectedLevel.value,
    title: skillLevels[selectedLevel.value],
  });

  // Clear the form
  searchQuery.value = "";
  selectedLevel.value = 0;
  selectedSkill.value = "";
  // Sort the TSList array by level
  TSList.value.sort((a, b) => b.level - a.level);
  const response = ref("These are the technical skills I have: ");
  for (let i = 0; i < TSList.value.length; i++) {
    response.value +=
      TSList.value[i].title + " in " + TSList.value[i].skill + ", ";
  }
  response.value += ".";
  emit("sendData", [response.value, TSList.value]);
};

const technicalSkills = [
  "Maritime Operations",
  "Container Terminal Management",
  "Vessel Traffic Management",
  "Port Security Systems",
  "Cargo Handling and Warehousing",
  "Supply Chain Management",
  "Logistics and Inventory Control",
  "Customs and Trade Compliance",
  "Maritime Safety and Regulations",
  "Port Automation and Robotics",
  "Transportation Management Systems (TMS)",
  "RFID and Barcode Technology",
  "Geographic Information Systems (GIS)",
  "Maintenance and Repair of Port Equipment",
  "Data Analytics and Reporting",
  "Cybersecurity for Maritime Infrastructure",
  "Environmental Sustainability in Ports",
  "Port Infrastructure Design and Engineering",
  "Navigational Aids and GPS Systems",
  "Port Facility Security Plans (PFSP)",
  "Emergency Response and Crisis Management",
  "Radio Communication and AIS",
  "Port Planning and Expansion",
  "Intermodal Transportation",
  "Dredging and Harbor Maintenance",
];
technicalSkills.sort((a, b) => a.localeCompare(b));
</script>
<style scoped>
.dropdown {
  position: relative;
  display: inline-block;
  width: 100%;
}

.dropdown-list {
  position: absolute;
  top: 100%;
  left: 30;
  width: 100%;
  border: 1px solid #ccc;
  max-height: 150px;
  overflow-y: auto;
  background-color: #ffffff;
  list-style: none;
  margin: 0;
  padding: 0;
  z-index: 1;
}

.dropdown-list li {
  cursor: pointer;
  padding: 8px;
  transition: background-color 0.2s;
}

.dropdown-list li:hover {
  background-color: #f0f0f0;
}

.dropdown-list .active {
  background-color: #007bff;
  color: #fff;
}
</style>
