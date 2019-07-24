import Vuex from 'vuex'
import general_state from './general_state'
import maps from './maps'


export default new Vuex.Store({
  modules: {
    general_state,
    maps,
  }
})