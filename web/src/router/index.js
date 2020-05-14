import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store.js'
import Home from '../views/Home.vue'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import SendBeep from '../views/SendBeep.vue'
import Feed from '../views/Feed'
import Search from '../views/Search'
import User from '../views/User'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {
      guest: true
    }
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
    meta: {
      guest: true
    }
  },
  {
    path: '/send-beep',
    name: 'send-beep',
    component: SendBeep,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/feed',
    name: 'feed',
    component: Feed,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/search',
    name: 'search',
    component: Search
  },
  {
    path: '/u/:username',
    name: 'user',
    component: User,
    props: true
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      next()
      return
    }
    next('/login')
  } else {
    next()
  }
})

export default router
