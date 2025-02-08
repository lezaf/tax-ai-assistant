<script setup>
import { RouterView } from "vue-router";
</script>

<template>
  <header>
    <div class="wrapper">
      <h1>Tax AI Assistant</h1>
      <p>
        Welcome to the Tax Filing AI Assistant, a tool that provides tax filing
        advice! Input the financial data required in the fields along with a tax
        related question and benefit from the insights of our AI-powered
        assistant. Start a conversation!
      </p>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
  margin-bottom: 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
  }

  header .wrapper {
    display: flex;
    flex-direction: column;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
