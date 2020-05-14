<template>
  <div>
    <h4>Profile of {{ username }}</h4>
    <div v-if="!loading">
      <button v-if="isLoggedIn && isFollowing" v-on:click="unfollow">Unfollow</button>
      <button v-else-if="isLoggedIn && !isSameUser" v-on:click="follow">Follow</button>
    </div>
    <Feed v-bind:url="username"/>
  </div>
</template>

<script>
import Feed from '../components/Feed'
import axios from 'axios'
import jwtDecode from 'jwt-decode'

export default {
  name: 'User',
  props: ['username'],
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isLoggedIn
    },
    isSameUser: function () {
      return jwtDecode(this.$store.state.token).identity === this.username
    }
  },
  data () {
    return {
      isFollowing: null,
      loading: true
    }
  },
  created () {
    this.checkFollowing()
  },
  methods: {
    checkFollowing () {
      axios.get('/follow', {
        params: {
          username: this.username
        },
        headers: {
          Authorization: 'Bearer ' + this.$store.state.token
        }
      })
        .then((resp) => {
          this.isFollowing = resp.data.is_following
          this.loading = false
        })
        .catch((error) => {
          console.log(error)
          return false
        })
    },
    follow () {
      axios.post('/follow', {
        username: this.username
      }, {
        headers: {
          Authorization: 'Bearer ' + this.$store.state.token
        }
      })
        .then(() => {
          this.isFollowing = true
        })
        .catch((error) => {
          console.log(error)
          console.log(error.response)
        })
    },
    unfollow () {
      axios.delete('/follow', {
        params: {
          username: this.username
        },
        headers: {
          Authorization: 'Bearer ' + this.$store.state.token
        }
      })
        .then(() => {
          this.isFollowing = false
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  components: {
    Feed
  }
}
</script>

<style scoped>

</style>
