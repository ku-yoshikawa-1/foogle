<template>
  <v-list two-line>
    <template v-for="(marker, index) in markers">
      
      <!-- Restaurant list -->
      <v-list-tile
        ripple
        :key="marker.id"
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
        <v-btn class="ma-2" text icon color="blue lighten-2">
          <v-icon @click='onLike'>thumb_up</v-icon>
        </v-btn>
      </v-list-tile>

      <!-- Restaurant divider -->
      <v-divider
        :key="index"
        v-if="index + 1 < markers.length"
      ></v-divider>

    </template>

  </v-list>
</template>

<script>
  import { mapGetters } from 'vuex'
  import { eventManager } from '../main'
  import axios from 'axios'

  export default {
    data: () => ({
      start: 0,
    }),
    computed: {
      ...mapGetters([
        'markers',
      ])
    },
    methods: {
      onClickList(marker, index) {
        eventManager.$emit('isRestaurantClicked', marker, index)
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
.no-more, .no-results {
  color: grey;
  margin: 10px 0 0;
}
</style>

