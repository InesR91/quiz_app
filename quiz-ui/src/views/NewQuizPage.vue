<script setup>
import { ref, onMounted } from 'vue';
import participationStorageService from '@/services/ParticipationStorageService';
import { useRouter } from 'vue-router';

const router = useRouter();

onMounted(async () => {
  console.log('New Quiz page mounted');
});

const username = ref('');

function launchNewQuiz() {
  console.log('Launch new quiz with', username.value);
  participationStorageService.savePlayerName(username);
  router.push('/questions');
}
</script>

<template>
  <h1>New quiz page</h1>

  <p>Saisissez votre nom :</p>
  <input type="text" v-model="username" />
  <button @click="launchNewQuiz">Go</button>
</template>
