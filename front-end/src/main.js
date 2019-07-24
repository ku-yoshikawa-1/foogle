import Vue from 'vue'
import './plugins'
import App from './App.vue'
import router from './router'
import store from './store/store'

// Makes the vue's event manager available
// across the app
export const eventManager = new Vue


Vue.config.productionTip = false


new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
