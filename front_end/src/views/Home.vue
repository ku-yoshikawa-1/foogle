<template>
    <div class="home">
        <div class="home-search-panel">
            <MySearchLogo class="my-search-logo"/>
            <HomeSearchBar class="home-search-bar"/>

        </div>

        <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->

    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'
    import MySearchLogo from '@/components/FoogleLogo.vue'
    import HomeSearchBar from '@/components/HomeSearchBar.vue'
    export default {
        name: 'home',
        components: {
            // HelloWorld,
            MySearchLogo,
            HomeSearchBar
        }
    }
</script>

<style lang="sass" scoped>
    .my-search-logo
        margin-top: 120px
        margin-bottom: 40px
    .home-search-bar
        margin: auto

</style>