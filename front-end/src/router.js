import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Search from './views/Search.vue'
import ShopInfo from './views/ShopInfo.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            // path: '/',
            path: '/search/:searchText',
            name: 'search',
            // route level code-splitting
            // this generates a separate chunk (search.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            // component: () => import(/* webpackChunkName: "search" */ './views/Search.vue')
            component: Search,
            props: route => ({
                searchText: String(route.params.searchText)
            })
        },
        {
            path: '/shop/:shop_name',
            name: 'Shop',
            component: ShopInfo,
            props: route => ({
              name: String(route.params.shop_name)
            })
        }
        // {
        //     path: '/detail/:ID',
        //     name: 'detail',
        //     component: Detail
        // },
    ]
})