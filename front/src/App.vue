<template>
  <v-app>
    <v-navigation-drawer
      app
      fixed
      clipped
      v-model="sidebarOpen"
      class="grey lighten-4"
    >
      <!-- Restaurants list -->
      <app-sidebar></app-sidebar>
    </v-navigation-drawer>

    <v-app-bar app dark color="#4169E1" >
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <span class="title ml-3 mr-5">Foogle&nbsp;<span class="font-weight-light">Mock</span></span>

      <v-layout wrap align-center>
        <v-flex md6>
          <v-text-field
            solo-inverted
            flat
            hide-details
            label="Search"
            prepend-inner-icon="search"
          ></v-text-field>
        </v-flex>
        <v-flex md1 ml-3>
          <v-btn
            block
            large
            color="error"
            class="search-btn"
            @click="getBargains"
          >
            Search
          </v-btn>
        </v-flex>
        <v-spacer/>
        <v-flex md1>
          <v-btn
            fab
            color="warning"
          >
          <v-icon>account_circle</v-icon>
          </v-btn>
        </v-flex>
      </v-layout>
    </v-app-bar>

    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import Sidebar from './components/Sidebar'
import { mapGetters } from 'vuex'
import axios from 'axios'


export default {
  name: 'App',
  data: () => ({
    query: '',
    searchType: 'Recommender',
    searchTypes: ['Recommender','Products','Shops'],
    searchResults:[],
  }),
  computed: {
    ...mapGetters([
      'sidebarOpen',
    ])
  },
  components: {
    appSidebar: Sidebar,
  },
  methods: {
    getBargains () {
      axios.get(`/bargains`, {
        params: {
          product: this.query,
        }
      })
        .then(response => {
          if (response.data && response.data.length > 0) {
            // Prepares markers
            const markers = response.data.map(bargain => {
              return {
                end_time: bargain.end_time,
                id: bargain.id,
                item_size: bargain.item_size,
                pack_ll: bargain.pack_ll,
                pack_ul: bargain.pack_ul,
                pack_type: bargain.pack_type,
                price: bargain.price,
                ori_price: parseInt(bargain.price * 1.3),
                price_peritem: bargain.price_peritem,
                product_name: bargain.product_name,
                // address: restaurant.restaurant.location.address,
                featuredImg: "https://img.kurashinista.jp/get/2019/02/12/7c04e57109036c5c9392408841aa7573.jpg?size=700&v=1",
                shop_name: bargain.shop_name,
                // descrip: shop.shop.shop_description,
                position: {
                  lat: parseFloat(bargain.latitude),
                  lng: parseFloat(bargain.longitude),
                },
                shop_img: bargain.shop_img,
                shop_url: bargain.shop_url
              }
            })

            // Initializes various states
            this.$store.dispatch('setQuery', this.query)
            this.$store.dispatch('setSearchType', this.searchType)
            this.$store.dispatch('setMarkers', markers)
            this.$store.dispatch('toogle_sidebar', true)

            // Updates center position of the map
            eventManager.$emit('updateCenterPosition', markers[0].position)
          }
        })
        .catch(error => {
          alert(error.message)
        })
    }
  }
};
</script>
