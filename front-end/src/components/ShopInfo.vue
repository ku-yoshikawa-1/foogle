<template>
  <v-data-table
    :headers="headers"
    :items="bargains"
    :items-per-page="10"
    class="elevation-1"
  >
  </v-data-table>
</template>

<script>
  import axios from 'axios'
  //import { mapGetters } from 'vuex'

  export default {
    name: 'shop',
    data () {
      return {
        headers: [
          {text: 'id', value:'id' },
          {text: 'product_name', value:'product_name' },
        ],
        bargains: []
      }
    },
    props: {
      name: String
    },
    mounted () {
      axios.get(`/bargains`, {
        params: {
          shop: this.name,
        }
      })
        .then(response => {
          if (response.data && response.data.length > 0) {
            // Prepares markers
            const bargains = response.data.map(bargain => {
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
              }
            })

            console.log(bargains)
            this.bargains = bargains
            
          }
        })
        .catch(error => {
          alert(error.message)
        })
    },

  }
</script>