<template>
  <Feed v-bind:config="{ headers: { Authorization: 'Bearer ' + this.$store.state.token } }" v-bind:url="''"/>
</template>

<script>
import Feed from '../components/Feed.vue'

export default {
  name: 'Home',
  components: {
    Feed
  }
}
</script>
