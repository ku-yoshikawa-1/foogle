export default {
  state () {
    return {
      search: 'ほうれん草',
      type: 'Recommender',
      shop: '河原町今出川店',
      markers: [],
      shop_markers: [],
    }
  },
  mutations: {
    'SET_SEARCH' (state, search) {
      state.search = search
    },
    'SET_TYPE' (state, type) {
      state.type = type
    },
    'SET_SHOP' (state, shop) {
      state.shop = shop
    },
    'SET_MARKERS' (state, markers) {
      state.markers = markers
    },
    'APPEND_MARKERS' (state, appendMarkers) {
      state.markers = state.markers.concat(appendMarkers)
    },
    'SET_SHOP_MARKERS' (state, shop_markers) {
      state.shop_markers = shop_markers
    }
  },
  actions: {
    initSearch: ({ commit }, search) => {
      commit('SET_SEARCH', search)
    },
    initType: ({ commit }, type) => {
      commit('SET_TYPE', type)
    },
    initShop: ({ commit }, shop) => {
      commit('SET_TYPE', shop)
    },
    initMarkers: ({ commit }, markers) => {
      commit('SET_MARKERS', markers)
    },
    appendMarkers: ({ commit }, appendMarkers) => {
      commit('APPEND_MARKERS', appendMarkers)
    },
    initShopMarkers: ({ commit }, shop_markers) => {
      commit('SET_SHOP_MARKERS', shop_markers)
    },
  },
  getters: {
    search: state => state.search,
    type: state => state.type,
    shop: state => state.shop,
    markers: state => state.markers,
    shop_markers: state => state.shop_markers,
  }
}