
import Vue from 'vue'
import Router from 'vue-router'
import GoogleMap from './components/GoogleMap'
import ShopInfo from './components/ShopInfo'

 Vue.use(Router)

 export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Search',
      component: GoogleMap
    },
    {
      path: '/shop/:shop_name',
      name: 'Shop',
      component: ShopInfo,
      props: route => ({
        name: String(route.params.shop_name)
      })
    }
  ]
})