<script setup>
const taxData = defineModel("taxData");
const errorMsg = defineModel("errorMsg");
</script>

<template>
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
      placeholder="Talk to AI for a tax filing related matter..."
      rows="5"
      required
    />
  </div>
</template>

<style scoped>
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

.error-msg {
  font-style: italic;
}

/* Remove arrows in browsers. */
/* input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type="number"] {
  -appearance: none;
  -moz-appearance: textfield;
} */
</style>
