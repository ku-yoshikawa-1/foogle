<!--<template>-->
<!--  <div id="app">-->
<!--    <img alt="Vue logo" src="./assets/logo.png">-->
<!--    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
<!--    <hr />-->
<!--    <ApiSample v-bind:info="info"/>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import HelloWorld from './components/HelloWorld.vue'-->
<!--import ApiSample from './components/ApiSample.vue'-->
<!--import axios from 'axios'-->

<!--export default {-->
<!--  name: 'app',-->
<!--  components: {-->
<!--    HelloWorld,-->
<!--    ApiSample-->
<!--  },-->
<!--  data () {-->
<!--    return {-->
<!--      info: {-->
<!--        test: 'test'-->
<!--      }-->
<!--    }-->
<!--  },-->
<!--  mounted () {-->
<!--    axios-->
<!--      .get('http://0.0.0.0:5000/')-->
<!--      .then(response => this.info = response.data)-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style>-->
<!--#app {-->
<!--  font-family: 'Avenir', Helvetica, Arial, sans-serif;-->
<!--  -webkit-font-smoothing: antialiased;-->
<!--  -moz-osx-font-smoothing: grayscale;-->
<!--  text-align: center;-->
<!--  color: #2c3e50;-->
<!--  margin-top: 60px;-->
<!--}-->
<!--</style>-->



<template>
  <div id="app">

    <router-view/>
  </div>
</template>

<style lang="scss">
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
  #nav {
    padding: 30px;
    a {
      font-weight: bold;
      color: #2c3e50;
      &.router-link-exact-active {
        color: #42b983;
      }
    }
  }
</style>