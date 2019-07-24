
import Vue from 'vue'
import Router from 'vue-router'
import GoogleMap from './components/GoogleMap'

 Vue.use(Router)

 export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/search',
      name: 'Search',
      component: GoogleMap
    }
  ]
})