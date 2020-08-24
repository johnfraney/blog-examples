<template>
  <div id="app">
    <h1>User Form</h1>
    <form @submit.prevent="onSubmit">
      <div v-for="(inputData, inputName) in fields" :key="inputName">
        <label v-text="inputData.label" />
        <input
          v-model="form[inputName]"
          v-bind="inputData.inputAttributes"
        >
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

import User from  './metadata/User.json'

type UserForm = {
  [UserField in keyof typeof User]?: typeof User[UserField]["initial"]
}

interface InputAttributes {
  [key: string]: boolean | number | string
}

interface InputData {
  inputAttributes: InputAttributes
  label: string
}

function convertFieldMetadataToInputData(fieldMetadata: typeof User[keyof typeof User]): InputData {
  const label = fieldMetadata.label
  const inputAttributes: InputAttributes = {
    name: fieldMetadata.field_name,
    required: fieldMetadata.required,
    type: fieldMetadata.type,
  }
  // Add non-universal properties
  if ('max_length' in fieldMetadata) {
    inputAttributes.maxlength = fieldMetadata.max_length
  }
  if ('pattern' in fieldMetadata) {
    inputAttributes.maxlength = fieldMetadata.pattern
  }
  return {
    inputAttributes,
    label,
  }
}

export default Vue.extend({
  name: 'App',

  data() {
    return {
      fields: {
        [User.first_name.field_name]: convertFieldMetadataToInputData(User.first_name),
        [User.last_name.field_name]: convertFieldMetadataToInputData(User.last_name),
        [User.email.field_name]: convertFieldMetadataToInputData(User.email),
        [User.username.field_name]: convertFieldMetadataToInputData(User.username),
      },
      form: {},
    }
  },

  methods: {
    onSubmit() {
      console.info({...this.form})
    },
  },
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}

input {
  margin-bottom: 1rem;
}

label {
  display: block;
}
</style>
