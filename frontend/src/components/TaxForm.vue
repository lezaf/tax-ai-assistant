<script setup>
import { ref } from "vue";
import axios from "axios";
import TaxFormFields from "./TaxFormFields.vue";

const props = defineProps(["answer", "isLoading"]);
const emit = defineEmits(["update:answer", "update:isLoading"]);

// Reactive variables for form inputs
const taxData = ref({
  income: null,
  expenses: null,
  propertiesNum: null,
  userPrompt: null,
});
const errorMsg = ref({
  income: "",
  expenses: "",
  propertiesNum: "",
});

// Form validation function
const validateForm = () => {
  if (taxData.value.income < 0) {
    errorMsg.value.income = "Income cannot be negative!";
    return false;
  }
  errorMsg.value.income = ""; // Reset msg if user inserted a value

  if (taxData.value.expenses < 0) {
    errorMsg.value.expenses = "Expenses cannot be negative!";
    return false;
  }
  errorMsg.value.expenses = "";

  if (taxData.value.propertiesNum < 0) {
    errorMsg.value.propertiesNum = "Properties number cannot be negative!";
    return false;
  }
  errorMsg.value.propertiesNum = "";

  return true;
};

// Make the backend API call to get AI-generated advice
const getAdvice = async () => {
  emit("update:isLoading", true);

  try {
    const response = await axios.post(
      "http://localhost:8000/api/advice/generate",
      {
        userData: {
          income: taxData.value.income,
          expenses: taxData.value.expenses,
          propertiesNum: taxData.value.propertiesNum,
        },
        userPrompt: taxData.value.userPrompt,
      },
      {
        headers: {
          "Content-Type": "application/json",
        },
        // Make the requests with credentials to use session id
        // to persist user data
        withCredentials: true,
      }
    );
    console.log("Form submitted successfully!");
    console.log("Response:", response.data.answer);

    // Update answer to parent
    emit("update:answer", response.data.answer);
  } catch (e) {
    console.error("Error submitting the form: ", e);
  } finally {
    emit("update:isLoading", false);
  }
};

// Handler for form submission
const onSubmit = () => {
  if (validateForm()) {
    console.log("Submitted");

    getAdvice();
  }
};
</script>

<template>
  <div class="form-container">
    <h2>Tax information</h2>

    <form @submit.prevent="onSubmit">
      <TaxFormFields v-model:taxData="taxData" v-model:errorMsg="errorMsg" />
      <button type="submit">Generate</button>
    </form>
  </div>
</template>

<style scoped>
.form-container {
  /* min-height: 400px; */
  max-width: 400px;
  width: 100%;
  margin: 20px 10px 20px 10px;
  padding: 20px;
  text-align: center;
  border: 1px solid var(--vt-c-indigo);
  border-radius: 5px;
}

h2 {
  margin-bottom: 30px;
}

button {
  width: 100%;
  padding: 10px;
  background-color: var(--vt-c-indigo);
  color: var(--text-color);
  border: 1px solid var(--vt-c-indigo);
  cursor: pointer;
  font-size: 1rem;
}

button:hover {
  background-color: var(--vt-c-black-mute);
  transition: 0.2s;
}

button:active {
  transform: scale(0.98);
}
</style>
