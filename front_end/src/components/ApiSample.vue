<template>
  <div class="api_sample">
    <h1>{{info.test}}</h1>
  </div>
</template>

<script>
export default {
  name: 'ApiSample',
  props: {
    info: Object
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
