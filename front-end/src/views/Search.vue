<template>
  <v-app>
    <v-navigation-drawer
      app
      fixed
      clipped
      v-model="drawer"
      class="grey lighten-4"
    >
      <!-- Restaurants list -->
      <app-list></app-list>

    </v-navigation-drawer>
<!--    <v-navigation-drawer-->
<!--            app-->
<!--            fixed-->
<!--            clipped-->
<!--            v-model="drawer_plus"-->
<!--            class="grey lighten-4"-->
<!--    >-->
<!--      &lt;!&ndash; Restaurants list &ndash;&gt;-->
<!--      <app-grid></app-grid>-->
<!--    </v-navigation-drawer>-->



    <v-toolbar color="#4169E1" app absolute clipped-left>
      <v-toolbar-side-icon @click="drawer = !drawer"></v-toolbar-side-icon>
      <span class="title ml-3 mr-5" :style="{ color: '#ffffff' }"><span class="font-weight-light">Let's</span>Foogle</span>
      <!-- Search bar -->
      <app-search-bar></app-search-bar>
    </v-toolbar>

    <v-content clipped-left>
      <v-container fluid fill-height class="grey lighten-4">
        <v-layout>
          <!-- Google map -->
          <app-google-map></app-google-map>
        </v-layout>
      </v-container>
      <app-grid></app-grid>
    </v-content>
  </v-app>
</template>

<script>
  import SearchBar from '@/components/SearchBar'
  import GoogleMap from '@/components/GoogleMap'
  import List from '@/components/List'
  import AppGrid from "../components/AppGrid";

  export default {
    name: 'search',
    data: () => ({
      drawer: null,
    }),
    components: {
      appSearchBar: SearchBar,
      appGoogleMap: GoogleMap,
      appList: List,
      appGrid: AppGrid,
    },
  }
</script>

<style>
.search-btn {
  height: 48px;
  margin: 0px 8px;
}
</style>
