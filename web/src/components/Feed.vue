<template>
  <div>
    <div v-bind:key="beep.id" v-for="beep of beeps">
      <Beep v-bind:date="beep.date" v-bind:text="beep.text" v-bind:username="beep.username"/>
    </div>
    <button @click="prev" v-if="offset !== 0">Prev</button>
    <div v-if="beeps === null">
      Loading
    </div>
    <div v-else-if="beeps.length === 0">
      Empty feed
    </div>
    <button @click="next" v-else-if="beeps.length === 10">Next</button>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import Beep from '../components/Beep.vue'

export default {
  name: 'Home',
  props: ['url', 'config'],
  data () {
    return {
      beeps: null,
      offset: 0
    }
  },
  created () {
    this.update()
  },
  methods: {
    next () {
      this.offset += 10
      this.update()
    },
    prev () {
      this.offset -= 10
      this.update()
    },
    update () {
      axios.get('/feed/' + this.url + '?offset=' + this.offset, this.config)
        .then(resp => {
          this.beeps = resp.data.beeps
        })
        .catch(e => console.error(e))
    }
  },
  components: {
    Beep
  }
}
</script>
