<template>
  <div>
    <form @submit.prevent="send" class="login">
      <label for="text">Text</label>
      <div>
        <textarea id="text" required v-model="text"></textarea>
      </div>
      <button type="submit">Send</button>
    </form>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'SendBeep',
    data() {
      return {
        text: ''
      }
    },
    methods: {
      send() {
        const text = this.text
        axios.post('/beep', {text: text}, {headers: {Authorization: 'Bearer ' + this.$store.state.token}})
          .then(() => this.$router.push('/'))
          .catch(err => console.log(err))
      }
    }
  }
</script>
