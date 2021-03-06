import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import * as VueGoogleMaps from 'vue2-google-maps'



// Sets defaults
axios.defaults.baseURL = 'http://localhost:5000'
axios.defaults.headers.common['Accept'] = "application/json"
// axios.defaults.headers.common['user-key'] = process.env.VUE_APP_ZOMATO_KEY;

// Registers plugins
Vue.use(Vuex)
Vue.use(Vuetify)
Vue.use(VueGoogleMaps, {
  load: {
    key: process.env.VUE_APP_GOOGLE_MAP_KEY || ''
  }
})