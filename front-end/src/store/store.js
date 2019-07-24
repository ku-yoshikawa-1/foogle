import Vuex from 'vuex'
import general_state from './general_state'
import googleMap from './googleMap'


export default new Vuex.Store({
  modules: {
    general_state,
    googleMap,
  }
})