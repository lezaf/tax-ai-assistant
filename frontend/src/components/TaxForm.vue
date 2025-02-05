<script setup>
import { ref } from "vue";
import axios from "axios";

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
  try {
    const response = await axios.post(
      "http://127.0.0.1:8000/api/advice/generate",
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
      }
    );
    console.log("Form submitted successfully!");
    console.log("Response:", response.data);
  } catch (e) {
    console.error("Error submitting the form: ", e);
  }
};

// Handler for form submission
const onSubmit = () => {
  if (validateForm()) {
    console.log("Submitted");
  }

  getAdvice();
};
</script>

<template>
  <div class="form-container">
    <h2>Tax information</h2>

    <form @submit.prevent="onSubmit">
      <div class="form-field">
        <label for="income">Annual income (EUR):</label>
        <input
          type="number"
          id="income"
          v-model="taxData.income"
          placeholder="Input income"
          required
        />
        <p v-if="errorMsg.income" class="error-msg">{{ errorMsg.income }}</p>
      </div>

      <div class="form-field">
        <label for="expenses">Annual expenses (EUR):</label>
        <input
          type="number"
          id="expenses"
          v-model="taxData.expenses"
          placeholder="Input expenses"
          required
        />
        <p v-if="errorMsg.expenses" class="error-msg">
          {{ errorMsg.expenses }}
        </p>
      </div>

      <div class="form-field">
        <label for="propertiesNum">Number of properties owned:</label>
        <input
          type="number"
          id="propertiesNum"
          v-model="taxData.propertiesNum"
          placeholder="Input # properties"
          required
        />
        <p v-if="errorMsg.propertiesNum" class="error-msg">
          {{ errorMsg.propertiesNum }}
        </p>
      </div>

      <div class="form-field">
        <label for="userPrompt">Prompt:</label>
        <textarea
          v-model="taxData.userPrompt"
          placeholder="Talk to AI.."
          rows="5"
          required
        />
      </div>

      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<style scoped>
.form-container {
  min-height: 400px;
  max-width: 400px;
  margin: auto;
  padding: 10px;
  text-align: center;
  border: 1px solid var(--vt-c-indigo);
  border-radius: 5px;
}

h2 {
  margin-bottom: 30px;
}

.form-field {
  margin-bottom: 20px;
  text-align: left;
}

.form-field input,
textarea {
  border: 3px solid var(--vt-c-indigo);
  border-radius: 2px;
  background-color: var(--color-background);
  color: var(--color-text);
}

label {
  display: block;
  font-weight: bolder;
}

input {
  width: 100%;
  padding: 10px;
  margin-top: 4px;
}

textarea {
  resize: none;
  width: 100%;
  margin-top: 4px;
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

.error-msg {
  font-style: italic;
}
</style>
