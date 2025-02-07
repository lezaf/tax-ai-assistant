<script setup>
import { marked } from "marked"; // Package to render markdown

const answer = defineModel("answer");
const isLoading = defineModel("isLoading");

const clearAnswer = () => {
  answer.value = "";
};
</script>

<template>
  <div class="answer-container">
    <p v-if="isLoading" class="loading-text">Generating response...</p>

    <p v-if="answer" v-html="marked(answer)"></p>
    <p v-else-if="isLoading == false">Ask me something about taxes! &#128640</p>

    <div class="btn-container">
      <button v-if="answer" @click="clearAnswer">Clear</button>
    </div>
  </div>
</template>

<style scoped>
.answer-container {
  /* max-width: 400px; */
  /* width: 50%; */
  max-width: 500px;
  width: 100%;
  /* margin: 20px 10px 20px 10px; */
  padding: 20px;
  text-align: left;
  border: 1px solid var(--vt-c-indigo);
  border-radius: 5px;
}

h2 {
  font-weight: bold;
}

.btn-container {
  display: flex;
  width: 100%;
  margin-top: 10px;
  justify-content: flex-end;
}

button {
  width: 80px;
  height: 30px;
  text-align: center;
  font-size: 10pt;
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

@keyframes textHighlightAnimation {
  0% {
    background-position: 100% 0%;
  }
  100% {
    background-position: -100% 0%;
  }
}

.loading-text {
  background-image: linear-gradient(
    to right,
    var(--vt-c-indigo) 30%,
    #f0f0f0 50%,
    var(--vt-c-indigo) 70%
  );
  background-size: 200% auto;
  background-clip: text;
  -webkit-background-clip: text;
  color: transparent;
  animation: textHighlightAnimation 2s linear infinite;
}
</style>
