<script setup>
import { ref, onMounted } from 'vue';
// import quizApiService from "@/services/QuizApiService";

onMounted(async () => {
  console.log('New Quiz page mounted');
});
data() {
  return {
    username: ''
  }
}
function launchNewQuiz() {
    console.log('Launch new quiz with', this.username);

}
</script>

<template>
  <h1>New quiz page</h1>

  <p>Saisissez votre nom :</p>
  <input type="text" v-model="username" />
  <p>{{ Username }}</p>
  <button @click="launchNewQuiz">Go</button>
</template>
