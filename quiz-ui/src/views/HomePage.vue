<script setup>
import { ref, onMounted } from 'vue';
import quizApiService from '@/services/QuizApiService';

const registeredScores = ref([]);

onMounted(async () => {
  console.log('Home page mounted');

  try {
    // Appel au service API pour récupérer les scores
    const response = await quizApiService.getRegisteredScores();

    // Stockage des données dans la variable réactive
    registeredScores.value = response.data; // ou response directement selon le service
    console.log('Scores récupérés :', registeredScores.value);
  } catch (error) {
    console.error('Erreur lors du chargement des scores :', error);
  }
});
</script>

<style></style>

<template>
  <h1>Home page</h1>

  <!-- Lien vers le quiz -->
  <router-link to="/new-quiz">Démarrer le quiz !</router-link>

  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
</template>
