export default {
  state () {
    return {
      search: '',
      type: 'Recommender',
      markers: [],
      sidebarOpen: false
    }
  },
  mutations: {
    'SET_SEARCH' (state, search) {
      state.search = search
    },
    'SET_TYPE' (state, type) {
      state.type = type
    },
    'SET_MARKERS' (state, markers) {
      state.markers = markers
    },
    'APPEND_MARKERS' (state, appendMarkers) {
      state.markers = state.markers.concat(appendMarkers)
    }
  },
  actions: {
    initSearch: ({ commit }, search) => {
      commit('SET_SEARCH', search)
    },
    initType: ({ commit }, type) => {
      commit('SET_TYPE', type)
    },
    initMarkers: ({ commit }, markers) => {
      commit('SET_MARKERS', markers)
    },
    appendMarkers: ({ commit }, appendMarkers) => {
      commit('APPEND_MARKERS', appendMarkers)
    }
  },
  getters: {
    search: state => state.search,
    type: state => state.type,
    markers: state => state.markers,
  }
}