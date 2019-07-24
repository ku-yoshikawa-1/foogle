export default {
  state () {
    return {
      sidebarOpen: false,
    }
  },
  mutations: {
    'TOOGLE_SIDEBAR' (state, sidebarOpen) {
      state.sidebarOpen = sidebarOpen
    },
  },
  actions: {
    toogle_sidebar: ({ commit }, sidebarOpen) => {
      commit('SET_SEARCH', sidebarOpen)
    },
  },
  getters: {
    sidebarOpen: state => state.sidebarOpen,
  }
}