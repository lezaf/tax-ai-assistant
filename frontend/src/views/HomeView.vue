<script setup>
import { ref } from "vue";
import TaxForm from "@/components/TaxForm.vue";
import AIAnswer from "@/components/AIAnswer.vue";

const answer = ref("");
const isLoading = ref(false);
</script>

<template>
  <div class="main-container">
    <TaxForm v-model:answer="answer" v-model:isLoading="isLoading" />
    <AIAnswer v-model:answer="answer" v-model:isLoading="isLoading" />
  </div>
</template>

<style scoped>
.main-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

@media (min-width: 1024px) {
  .main-container {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    /* grid-template-columns: 1fr 1fr;
    padding: 0 2rem; */
  }
}
</style>
