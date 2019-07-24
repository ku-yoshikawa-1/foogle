export default {
  state () {
    return {
      query: '',
      searchType: 'Recommender',
      markers: [],
      sidebarOpen: false
    }
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
  },
  getters: {
    query: state => state.query,
    searchType: state => state.searchType,
    markers: state => state.markers,
  }
}