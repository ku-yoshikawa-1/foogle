import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    query: '',
    searchType: 'Recommender',
    markers: [],
    sidebarOpen: false,
  },
  mutations: {
    'SET_QUERY' (state, query) {
      state.query = query
    },
    'SET_SEARCH_TYPE' (state, searchType) {
      state.searchType = searchType
    },
    'SET_MARKERS' (state, markers) {
      state.markers = markers
    },
    'TOOGLE_SIDEBAR' (state, sidebarOpen) {
      state.sidebarOpen = sidebarOpen
    },
  },
  actions: {
    setQuery: ({ commit }, query) => {
      commit('SET_QUERY', query)
    },
    setSearchType: ({ commit }, type) => {
      commit('SET_SEARCH_TYPE', type)
    },
    setMarkers: ({ commit }, markers) => {
      commit('SET_MARKERS', markers)
    },
    toogle_sidebar: ({ commit }, sidebarOpen) => {
      commit('TOOGLE_SIDEBAR', sidebarOpen)
    },
  },
  getters: {
    query: state => state.query,
    searchType: state => state.searchType,
    markers: state => state.markers,
    sidebarOpen: state => state.sidebarOpen,
  }
})
