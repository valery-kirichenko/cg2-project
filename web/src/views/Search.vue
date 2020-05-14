<template>
  <div>
    <form @submit.prevent="search">
      <label for="search">Search: </label>
      <input id="search" placeholder="Search text" required type="text" v-model="text">
      <button type="submit">Search...</button>
    </form>
    <div v-bind:key="beep.id" v-for="beep of beeps">
      <Beep v-bind:date="beep.date" v-bind:text="beep.text" v-bind:username="beep.username"/>
    </div>
    <span v-if="beeps && beeps.length === 0">Empty search results</span>
    <span>{{ error }}</span>
  </div>
</template>

<script>
  import axios from 'axios'
  import Beep from '../components/Beep.vue'

  export default {
    name: 'Search',
    data() {
      return {
        beeps: null,
        text: '',
        error: ''
      }
    },
    methods: {
      search() {
        axios.get('/search/beep', {
          params: {
            text: this.text
          }
        })
          .then((resp) => {
            this.beeps = resp.data;
            this.error = ''
          })
          .catch((error) => {
            this.error = error.response.data.msg;
            this.beeps = null
          })
      }
    },
    components: {
      Beep
    }
  }
</script>

<style scoped>

</style>
