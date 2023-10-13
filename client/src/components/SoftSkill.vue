<template>
  <div class="mt-3">
    <div class="transition-container">
      <h5 style="height: 40px">{{ currentState.question }}</h5>
      <div class="input-group">
        <textarea class="form-control" v-model="currentState.answer"></textarea>
      </div>
    </div>
    <div class="progress" style="height: 5px">
      <div
        class="progress-bar"
        role="progressbar"
        :style="{
          width: progressWidth,
        }"
        aria-valuenow="100"
        aria-valuemin="0"
        aria-valuemax="100"
      ></div>
    </div>
    <div class="d-flex justify-content-between">
      <div>
        <button
          class="btn btn-light mt-3 me-2"
          @click="prevQuestion"
          :hidden="currentState.prev === null"
        >
          Previous
        </button>
        <button
          :class="{
            'btn btn-success mt-3': currentState.answer != '',
            'btn btn-warning mt-3': currentState.answer == '',
          }"
          @click="nextQuestion"
          :hidden="currentState.next === null"
        >
          {{ currentState.answer != "" ? "Next" : "Skip" }}
        </button>
      </div>
      <button class="btn btn-primary mt-3" @click="save">Save</button>
    </div>
  </div>
  <hr />
</template>

<script setup>
import { ref, computed, defineEmits } from "vue";
const stateMachine = {
  currentState: 0,
  states: [
    {
      category: "Communication Skills",
      question:
        "How comfortable are you when speaking in public or giving presentations?",
      answer: "",
      next: 1,
      prev: null,
    },
    {
      category: "Communication Skills",
      question: "Do you actively listen to others during conversations?",
      answer: "",
      next: 2,
      prev: 0,
    },
    {
      category: "Communication Skills",
      question: "How well do you express your ideas and thoughts in writing?",
      answer: "",
      next: 3,
      prev: 1,
    },
    {
      category: "Communication Skills",
      question:
        "Are you able to adapt your communication style to different audiences?",
      answer: "",
      next: 4,
      prev: 2,
    },
    {
      category: "Communication Skills",
      question:
        "How effectively do you provide feedback to colleagues or team members?",
      answer: "",
      next: 5,
      prev: 3,
    },
    {
      category: "Teamwork and Collaboration",
      question: "How do you handle conflicts within a team?",
      answer: "",
      next: 6,
      prev: 4,
    },
    {
      category: "Teamwork and Collaboration",
      question: "Are you open to others' ideas and willing to compromise?",
      answer: "",
      next: 7,
      prev: 5,
    },
    {
      category: "Teamwork and Collaboration",
      question:
        "Do you take on different roles within a team to support its goals?",
      answer: "",
      next: 8,
      prev: 6,
    },
    {
      category: "Teamwork and Collaboration",
      question: "How do you contribute to a positive team atmosphere?",
      answer: "",
      next: 9,
      prev: 7,
    },
    {
      category: "Teamwork and Collaboration",
      question:
        "Are you skilled at building relationships and networks within your organization?",
      answer: "",
      next: 10,
      prev: 8,
    },
    {
      category: "Adaptability and Flexibility",
      question: "How well do you handle change and uncertainty?",
      answer: "",
      next: 11,
      prev: 9,
    },
    {
      category: "Adaptability and Flexibility",
      question: "Are you open to trying new approaches and methods?",
      answer: "",
      next: 12,
      prev: 10,
    },
    {
      category: "Adaptability and Flexibility",
      question:
        "Can you adjust to shifting priorities and work on multiple tasks simultaneously?",
      answer: "",
      next: 13,
      prev: 11,
    },
    {
      category: "Adaptability and Flexibility",
      question: "How do you respond to unexpected challenges or setbacks?",
      answer: "",
      next: 14,
      prev: 12,
    },
    {
      category: "Adaptability and Flexibility",
      question:
        "Are you willing to learn and adapt in response to new information?",
      answer: "",
      next: 15,
      prev: 13,
    },
    {
      category: "Leadership and Influence",
      question:
        "Have you taken on leadership roles in the past, even informally?",
      answer: "",
      next: 16,
      prev: 14,
    },
    {
      category: "Leadership and Influence",
      question:
        "How do you motivate and inspire others to achieve common goals?",
      answer: "",
      next: 17,
      prev: 15,
    },
    {
      category: "Leadership and Influence",
      question:
        "Are you comfortable making decisions and taking responsibility for outcomes?",
      answer: "",
      next: 18,
      prev: 16,
    },
    {
      category: "Leadership and Influence",
      question:
        "Do you actively seek opportunities to lead or influence within your team or organization?",
      answer: "",
      next: 19,
      prev: 17,
    },
    {
      category: "Leadership and Influence",
      question:
        "How well do you manage conflicts and resolve disputes as a leader?",
      answer: "",
      next: 20,
      prev: 18,
    },
    {
      category: "Problem Solving and Decision-Making",
      question: "How do you approach complex problems or challenges?",
      answer: "",
      next: 21,
      prev: 19,
    },
    {
      category: "Problem Solving and Decision-Making",
      question:
        "Are you skilled at gathering information and analyzing data to make decisions?",
      answer: "",
      next: 22,
      prev: 20,
    },
    {
      category: "Problem Solving and Decision-Making",
      question: "Can you identify creative solutions to problems?",
      answer: "",
      next: 23,
      prev: 21,
    },
    {
      category: "Problem Solving and Decision-Making",
      question:
        "How do you prioritize tasks and make decisions in high-pressure situations?",
      answer: "",
      next: 24,
      prev: 22,
    },
    {
      category: "Problem Solving and Decision-Making",
      question:
        "Do you involve others in the decision-making process when appropriate?",
      answer: "",
      next: 25,
      prev: 23,
    },
    {
      category: "Emotional Intelligence",
      question:
        "Are you aware of your own emotions and how they impact your behavior?",
      answer: "",
      next: 26,
      prev: 24,
    },
    {
      category: "Emotional Intelligence",
      question:
        "How well do you recognize and empathize with the emotions of others?",
      answer: "",
      next: 27,
      prev: 25,
    },
    {
      category: "Emotional Intelligence",
      question:
        "Can you manage and regulate your emotions effectively in stressful situations?",
      answer: "",
      next: 28,
      prev: 26,
    },
    {
      category: "Emotional Intelligence",
      question:
        "Are you skilled at building rapport and establishing trust with colleagues?",
      answer: "",
      next: 29,
      prev: 27,
    },
    {
      category: "Emotional Intelligence",
      question:
        "How do you handle difficult or emotional conversations with sensitivity?",
      answer: "",
      next: null,
      prev: 28,
    },
  ],
};

function save() {
  const response = ref("");
  for (let i = 0; i < stateMachine.states.length; i++) {
    if (stateMachine.states[i].answer != "") {
      response.value += "When asked about ";
      response.value += stateMachine.states[i].category + ", ";
      response.value += stateMachine.states[i].question;
      response.value += " I answered, ";
      response.value += stateMachine.states[i].answer + ". ";
    }
  }

  emit("sendData", response.value);
}

const currentState = ref(stateMachine.states[stateMachine.currentState]);
const emit = defineEmits(["sendData"]);
function nextQuestion() {
  if (currentState.value.next !== null) {
    currentState.value = stateMachine.states[currentState.value.next];
  }
}

function prevQuestion() {
  if (currentState.value.prev !== null) {
    currentState.value = stateMachine.states[currentState.value.prev];
  }
}

const progressWidth = computed(() => {
  if (currentState.value.next === null) {
    return "100%";
  }
  const progress = (currentState.value.next / stateMachine.states.length) * 100;
  return progress + "%";
});

const softSkills = [
  "Communication Skills",
  "Teamwork and Collaboration",
  "Adaptability and Flexibility",
  "Problem Solving",
  "Leadership and Management",
  "Time Management",
  "Customer Service",
  "Negotiation and Conflict Resolution",
  "Attention to Detail",
  "Critical Thinking",
  "Decision Making",
  "Creativity and Innovation",
  "Emotional Intelligence",
  "Stress Management",
  "Cross-Cultural Competence",
  "Effective Presentation",
  "Conflict Resolution",
  "Customer Relationship Management",
  "Interpersonal Skills",
  "Networking",
  "Ethical Decision-Making",
  "Crisis Management",
  "Business Acumen",
  "Self-Motivation",
  "Resilience",
];
softSkills.sort((a, b) => a.localeCompare(b));
</script>
<style scoped>
.transition-container {
  transition: opacity 0.5s;
}

.question-enter-active,
.question-leave-active {
  transition: opacity 1s; /* Add this line for opacity transition */
  opacity: 1;
}

.question-enter,
.question-leave-to {
  transition: opacity 1s; /* Add this line for opacity transition */
  opacity: 0;
}
</style>
