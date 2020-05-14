<template>
  <Feed v-bind:url="'all'"/>
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
