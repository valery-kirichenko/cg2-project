<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Latest beeps</router-link>
      |
      <router-link to="/search">Search</router-link>
      |
      <span v-if="isLoggedIn">
        <router-link to="/feed">Feed</router-link> |
        <router-link to="/send-beep">Send a beep</router-link> |
        <a @click="logout" href="#">Logout ({{ username }})</a></span>
      <span v-else>
        <router-link to="/login">Login</router-link> |
        <router-link to="/register">Register</router-link>
      </span>
    </div>
    <router-view/>
  </div>
</template>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  #nav {
    padding: 30px;
  }

  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }

  /*noinspection CssUnusedSymbol*/
  #nav a.router-link-exact-active {
    color: #42b983;
  }
</style>

<script>
import jwtDecode from 'jwt-decode'

export default {
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isLoggedIn
    },
    username: function () {
      return jwtDecode(this.$store.state.token).identity
    }
  },
  methods: {
    logout: function () {
      this.$store.dispatch('logout')
        .then(() => {
          this.$router.push('/login')
        })
    }
  }
}
</script>
