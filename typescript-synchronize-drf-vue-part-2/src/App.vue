<template>
  <div id="app">
    <h1>User</h1>
    <form>
      <div
        v-for="(field, fieldName) in user"
        :key="fieldName"
      >
        <label v-text="field.label" />
        <input
          :name="fieldName"
          :required="field.required"
        >
      </div>
    </form>
    <pre v-text="user" />
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

import User from  './metadata/User.json'

export default Vue.extend({
  name: 'App',

  data() {
    return {
      user: User,
    }
  },
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  margin-top: 60px;
}
</style>
