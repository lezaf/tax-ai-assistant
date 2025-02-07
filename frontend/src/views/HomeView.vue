<script setup>
import { ref } from "vue";
import TaxForm from "@/components/TaxForm.vue";
import AIAnswer from "@/components/AIAnswer.vue";

const answer = ref("");
</script>

<template>
  <div class="main-container">
    <TaxForm v-model:answer="answer" />
    <AIAnswer v-model:answer="answer" />
  </div>
</template>

<style scoped>
.main-container {
  display: flex;
  flex-direction: column;
}

@media (min-width: 1024px) {
  .main-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    padding: 0 2rem;
  }
}
</style>
