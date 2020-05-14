<template>
  <div>
    <form @submit.prevent="login" class="login">
      <h1>Sign in</h1>
      <label for="username">Username</label>
      <div>
        <input id="username" minlength="4" placeholder="Username" required type="text" v-model="username"/>
      </div>
      <label for="password">Password</label>
      <div>
        <input id="password" placeholder="Password" required type="password" v-model="password"/>
      </div>
      <hr/>
      <button type="submit">Login</button>
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
    login: function () {
      const username = this.username
      const password = this.password
      this.$store.dispatch('login', { username, password })
        .then(() => this.$router.push('/'))
        .catch(err => console.log(err))
    }
  }
}
</script>
