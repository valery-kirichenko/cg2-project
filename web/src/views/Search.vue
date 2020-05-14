<template>
  <div>
    <form @submit.prevent="search">
      <label for="search">Search: </label>
      <input id="search" placeholder="Search text" required type="text" v-model="text" v-on:keyup="launchSuggestionTimer">
      <button type="submit">Search...</button>
    </form>
    <div v-if="suggestions !== null && suggestions.length > 0">
      <h6>Suggested users</h6>
      <span v-for="(suggestion, key) of suggestions" v-bind:key="suggestion">
        <router-link :to="{ name: 'user', params: { username: suggestion } }">{{ suggestion }}</router-link><span v-if="key+1 !== suggestions.length">, </span>
      </span>
    </div>
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
  data () {
    return {
      beeps: null,
      text: '',
      error: '',
      suggestions: null,
      suggestion_timer: null
    }
  },
  methods: {
    search () {
      axios.get('/search/beep', {
        params: {
          text: this.text
        }
      })
        .then((resp) => {
          this.beeps = resp.data
          this.error = ''
        })
        .catch((error) => {
          this.error = error.response.data.msg
          this.beeps = null
        })
    },
    launchSuggestionTimer () {
      if (this.suggestion_timer !== null) {
        clearTimeout(this.suggestion_timer)
      }
      this.suggestion_timer = setTimeout(this.suggest, 150)
    },
    suggest () {
      if (this.text.length < 3) {
        return
      }
      axios.get('/search/suggest', {
        params: {
          text: this.text
        }
      })
        .then((resp) => {
          this.suggestions = resp.data
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
