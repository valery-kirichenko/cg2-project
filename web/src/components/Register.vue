<template>
  <div>
    <h4>Register</h4>
    <form @submit.prevent="register">
      <label for="username">Username</label>
      <div>
        <input autofocus id="username" minlength="4" required type="text" v-model="username">
      </div>
      <label for="password">Password</label>
      <div>
        <input id="password" required type="password" v-model="password">
      </div>
      <div>
        <button type="submit">Register</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    register: function () {
      const data = {
        username: this.username,
        password: this.password
      }
      this.$store.dispatch('register', data)
        .then(() => this.$router.push('/login'))
        .catch(err => console.log(err))
    }
  }
}
</script>
