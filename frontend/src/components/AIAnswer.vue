<script setup>
const answer = defineModel("answer");
// defineProps(["modelValue"]);
</script>

<template>
  <div class="answer-container">
    <h2>Response:</h2>
    <p v-if="answer">{{ answer }}</p>
    <p v-else>Waiting for a question...</p>
  </div>
</template>

<style scoped>
.answer-container {
  /* max-width: 400px; */
  width: 100%;
  margin: 20px 10px 20px 10px;
  padding: 20px;
  text-align: left;
  border: 1px solid var(--vt-c-indigo);
  border-radius: 5px;
}

h2 {
  font-weight: bold;
}
</style>
