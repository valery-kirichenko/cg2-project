import Vue from 'vue'
import Vuex from 'vuex'
import store from './store.js'
import App from './App.vue'
import router from './router'
import axios from 'axios'

Vue.use(Vuex)
axios.defaults.baseURL = 'http://localhost:5000/api/'

new Vue({
  router,
  render: h => h(App),
  store: store
}).$mount('#app')
