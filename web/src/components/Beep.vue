<template>
  <div>
    <p>{{ text }}</p>
    <p>
      <router-link :to="{ name: 'user', params: { username: username } }">{{ username }}</router-link>
      at {{ (new Date(date)).toLocaleString() }}
    </p>
  </div>
</template>

<script>
  export default {
    name: 'Beep',
    props: ['text', 'username', 'date']
  }
</script>

<style scoped>

</style>
