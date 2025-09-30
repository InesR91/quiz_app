<script setup>
import { ref } from 'vue';
import { RouterLink } from 'vue-router';

// --- Données test (à remplacer par les données du back-end) ---
const userScore = ref(85); // Score de l'utilisateur actuel

// Classement des meilleurs scores
const highScores = ref([
  { id: 1, name: 'Alice', score: 98 },
  { id: 2, name: 'Bob', score: 92 },
  { id: 3, name: 'Charlie', score: 88 },
  { id: 4, name: 'David', score: 85 },
  { id: 5, name: 'Eve', score: 76 },
]);

// Classement de l'utilisateur
const userRank = ref(4);
// --- Fin test ---
</script>

<template>
  <div class="score-view">
    <div class="score-container">
      <h1>Résultats du Quiz</h1>

      <!-- Affichage du score de l'utilisateur -->
      <div class="user-score-section">
        <h2>Votre Score</h2>
        <p class="score">{{ userScore }} / 100</p>
        <p class="rank">Votre classement : {{ userRank }} sur {{ highScores.length }}</p>
      </div>

      <!-- Affichage des meilleurs scores -->
      <div class="high-scores-section">
        <h2>Meilleurs Scores</h2>
        <ul class="scores-list">
          <li v-for="score in highScores" :key="score.id" class="score-item">
            <span class="player-name">{{ score.name }}</span>
            <span class="player-score">{{ score.score }}</span>
          </li>
        </ul>
      </div>

      <!-- Bouton de retour à l'accueil -->
      <div class="actions">
        <RouterLink to="/" class="home-button">Retour à l'accueil</RouterLink>
      </div>
    </div>
  </div>
</template>
