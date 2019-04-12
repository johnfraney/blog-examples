<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>Phrases from Django API:</h1>
    <p
      v-for="(phrase, index) in phrases_from_api"
      :key="index"
    >
      {{ phrase }}
    </p>
    <button type="button" @click="fetchPhrases">
      Fetch Phrases
    </button>
  </div>
</template>

<script>
export default {
  name: 'app',

  data: function() {
    return {
      phrases_from_api: [],
    }
  },

  methods: {
    async fetchPhrases() {
      const response = await this.$http.get('/api/phrases/')
      this.phrases_from_api = response.body.data
    }
  }

}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
