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
      commit('TOOGLE_SIDEBAR', sidebarOpen)
    },
  },
  getters: {
    sidebarOpen: state => state.sidebarOpen,
  }
}