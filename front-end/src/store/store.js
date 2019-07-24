import Vuex from 'vuex'
import general_state from './general_state'
import search from './search'


export default new Vuex.Store({
  modules: {
    general_state,
    search,
  }
})