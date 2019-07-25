<template>
  <v-list two-line>
    <template v-for="(marker, index) in markers">
      
      <!-- Restaurant list -->
      <v-list-tile
        ripple
        :key="marker.product_name"
        @click="onClickList(marker, index)"
      >
        <!-- Restaurant avatar -->
        <v-avatar
          :tile="true"
          :size="56"
          :style="{ marginRight: '8px' }"
        >
          <v-img
            aspect-ratio="1"
            :src="marker.shop_img"
            class="grey lighten-2"
          >
            <v-layout
              slot="placeholder"
              fill-height
              align-center
              justify-center
              ma-0
            >
              <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
            </v-layout>
          </v-img>
        </v-avatar>

        <!-- Restaurant short desc -->
        <v-list-tile-content>
          <v-list-tile-title>{{ marker.product_name }}</v-list-tile-title>
          <v-list-tile-sub-title class="text--primary">Price: {{ marker.price }}</v-list-tile-sub-title>
          <v-list-tile-sub-title>Original Price: {{ marker.ori_price }}</v-list-tile-sub-title>
          <v-list-tile-sub-title>Quantity: {{ marker.pack_ll }} to {{ marker.pack_ul }}</v-list-tile-sub-title>
        </v-list-tile-content>
      </v-list-tile>

      <!-- Restaurant divider -->
      <v-divider
        :key="index"
        v-if="index + 1 < markers.length"
      ></v-divider>

    </template>

    <!-- Infinite Loader -->
    <infinite-loading @infinite="infiniteHandler" spinner="spiral">
      <div slot="no-more" class="no-more">The End</div>
      <div slot="no-results" class="no-results">No restaurants found.</div>
    </infinite-loading>

  </v-list>
</template>

<script>
  import axios from 'axios'
  import { mapGetters } from 'vuex'
  import { eventManager } from '../main'
  import InfiniteLoading from 'vue-infinite-loading'

  export default {
    data: () => ({
      start: 0,
    }),
    computed: {
      ...mapGetters([
        'search',
        'type',
        'markers',
      ])
    },
    methods: {
      onClickList(marker, index) {
        eventManager.$emit('isRestaurantClicked', marker, index)
      },
      infiniteHandler($state) {
        axios.get('/bargains', {
          params: {
            product: this.search,
          }
        })
          .then(response => {
            if (response.data && this.start < parseInt(response.data.length + 20)) {
              const appendMarkers = response.data.map(bargain => {
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


              // Increases the start
              this.start += 20

              if (appendMarkers.length > 0) {
                // Updates map center position
                eventManager.$emit('updateCenterPosition', appendMarkers[0].position)
                
                // Appends markers to the state
                this.$store.dispatch('appendMarkers', appendMarkers)
              }

              $state.loaded()
            } else {
              $state.complete()
            }
          })
          .catch(error => {
            alert(error.message)
          })
      }
    },
    components: {
      InfiniteLoading,
    }
  }
</script>

<style>
.no-more, .no-results {
  color: grey;
  margin: 10px 0 0;
}
</style>

