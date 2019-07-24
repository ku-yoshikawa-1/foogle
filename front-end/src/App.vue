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

    <v-toolbar color="#4169E1" app absolute clipped-left>
      <v-toolbar-side-icon @click="drawer = !drawer"></v-toolbar-side-icon>
      <span class="title ml-3 mr-5" :style="{ color: '#ffffff' }"><span class="font-weight-light">Let's</span>&nbsp;Foogle</span>
      <!-- Search bar -->
      <app-search-bar></app-search-bar>
    </v-toolbar>

    <v-content>
      <v-container fluid fill-height class="grey lighten-4">
        <v-layout>
          <router-view/>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import SearchBar from './components/SearchBar'
  import Sidebar from './components/Sidebar'
  import { mapGetters } from 'vuex'

  export default {
    computed: {
      ...mapGetters([
        'sidebarOpen',
      ])
    },
    components: {
      appSearchBar: SearchBar,
      appSidebar: Sidebar,
    }
  }
</script>

<style>
.search-btn {
  height: 48px;
  margin: 0px 8px;
}
</style>
