<template>
  <v-card>
<!--     Card image -->
    <v-img
      :src="marker.featuredImg"
      aspect-ratio="2.75"
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

    <!-- Card details -->
    <v-card-title primary-title>
      <v-list-tile-content>
          <h3 class="headline mb-0">{{ marker.product_name }}</h3>
          <button @click="getShopMarkers"><router-link v-bind:to="{ name: 'Shop', params: { shop_name: marker.shop_name}}">From: {{ marker.shop_name }}</router-link></button>
          <div class="font_bk">
              <p><strong>Price: {{ marker.price }}</strong></p>
              <div>Original Price: {{ marker.ori_price }}</div>
              <div>Size: {{ marker.item_size }}</div>
              <div>Quantity: {{ marker.pack_ll }} to {{ marker.pack_ul }}</div>
              <div>Distance: 1.3KM</div>
              <div>Deadline: {{ marker.end_time }}</div>
          </div>
      </v-list-tile-content>
    </v-card-title>
    <v-card-actions>
      <v-btn class="ma-2" text icon color="blue lighten-2">
        <v-icon @click='onLike'>thumb_up</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>

    import axios from 'axios'
    import { eventManager } from '../main'

  export default {
    props: {
      marker: Object
    },
    methods:{
        getShopMarkers () {
            axios.get(`/bargains`, {
                params: {
                    shop: this.marker.shop_name,
                }
            })
                .then(response => {
                    if (response.data && response.data.length > 0) {
                        // Prepares markers
                        const markers = response.data.slice(0,6).map(bargain => {
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

                        this.$store.dispatch('initShopMarkers', markers)
                        this.$store.dispatch('initShop', this.marker.shop_name)

                        // Updates center position of the map
                        eventManager.$emit('updateCenterPosition', markers[0].position)
                    }
                })
                .catch(error => {
                    alert(error.message)
                })
        },
        onLike(marker) {
          axios.get(`/like`, {
            params: {
              bargain_id: marker.id,
            }
          })
        }
    }
  }
</script>

<style>

    .font_bk{border:1px solid #ccc;}


</style>