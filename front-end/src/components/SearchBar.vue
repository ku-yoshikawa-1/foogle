<template>
  <v-form :style="{ width: '100%' }">
    <v-layout align-start justify-start row mt-2>
      <!-- Search box -->
      <v-flex md8>
        <v-text-field
          solo
          flat
          hide-details
          v-model="search"
          label="Type food name"
          prepend-inner-icon="search"
        ></v-text-field>
      </v-flex>

      <!-- Select box -->
      <v-flex md2 ml-2>
        <v-select
          solo
          flat
          label="Category"
          item-text="text"
          item-value="value"
          :items="types"
          v-model="type"
        ></v-select>
      </v-flex>

      <!-- Search button -->
      <v-flex md2>
        <v-btn
          color="error"
          class="search-btn"
          @click="getRestaurantMarkers"
        >
          Search
        </v-btn>
      </v-flex>
    </v-layout>
  </v-form>
</template>

<script>
  import axios from 'axios'
  import { eventManager } from '../main'

  export default {
    data: () => ({
      search: 'ほうれん草',
      type: 'Products',
      types: ['Recommender','Products','Shops'],
      searchResults:[]
    }),
    methods: {
      getRestaurantMarkers () {
        axios.get(`/bargains`, {
          params: {
            product: this.search,
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
                  price: bargain.price,
                  ori_price: parseInt(bargain.price * 1.3),
                  price_peritem: bargain.price_peritem,
                  product_name: bargain.product_name,
                  // address: restaurant.restaurant.location.address,
                  featuredImg: "https://img.kurashinista.jp/get/2019/02/12/7c04e57109036c5c9392408841aa7573.jpg?size=700&v=1",
                  shop_name: bargain.shop_name,
                  // descrip: shop.shop.shop_description,
                  position: {
                    // lat: parseFloat(bargain.bargain.latitude),
                    // lng: parseFloat(bargain.bargain.longitude),
                    lat: 35.02632 + Math.random()*0.01,
                    lng: 135.78095 + Math.random()*0.01,
                  },
                }
              })

              // Initializes various states
              this.$store.dispatch('initSearch', this.search)
              this.$store.dispatch('initType', this.type)
              this.$store.dispatch('initMarkers', markers)

              // Updates center position of the map
              eventManager.$emit('updateCenterPosition', markers[0].position)
            }
          })
          .catch(error => {
            alert(error.message)
          })
      }
    },
    // created () {
    //   // Gets cuisines as defaults
    //   axios.get('/cuisines', {
    //     params: {
    //       lat: 1.0,
    //       lon: 1.0,
    //     }
    //   })
    //     .then( response => {
    //       if (response.data && response.data.cuisines.length > 0) {
    //         const cuisines = response.data.cuisines.map(cuisine => {
    //           return {
    //             text: cuisine.cuisine.cuisine_name,
    //             value: cuisine.cuisine.cuisine_id,
    //           }
    //         })
    //
    //         cuisines.unshift({ text: 'Choose Cuisine', value: 0 })
    //         this.cuisines = cuisines
    //       }
    //     })
    //     .catch(error => {
    //       alert(error.message)
    //     })
    // }
  }
</script>
