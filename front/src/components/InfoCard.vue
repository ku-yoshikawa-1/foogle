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
      <div>
          <h3 class="headline mb-0">{{ marker.product_name }}</h3>
          <p><a :href="marker.url" target="_blank">From: {{ marker.shop_name }}</a></p>
          <div class="font_bk">
              <p><strong>Price: {{ marker.price }}</strong></p>
              <div>Original Price: {{ marker.ori_price }}</div>
              <div>Size: {{ marker.item_size }}</div>
              <div>Quantity: {{ marker.pack_ll }} to {{ marker.pack_ul }}</div>
              <div>Distance: 1.3KM</div>
              <div>Deadline: {{ marker.end_time }}</div>
          </div>
      </div>
    </v-card-title>
  </v-card>
</template>

<script>
  export default {
    props: {
      marker: Object
    }
  }
</script>

<style>

    .font_bk{border:1px solid #ccc;}


</style>