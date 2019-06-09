<template>
    <div class="search-result-toolbar">
        <img class="logo" src="./../assets/Foogle_logo_small.png" alt="" @click="goHome">
        <RoundSearchBar :search="search"/>
    </div>
</template>

<script>
    import RoundSearchBar from '@/components/RoundSearchBar.vue'
    export default {
        name: 'search-result-toolbar',
        props:['search'],
        components: {
            RoundSearchBar
        },
        methods: {
            goHome(){
                this.$router.push("/")
            }
        },
    }
</script>
<style lang="sass" scoped>
    .search-result-toolbar
        text-align: left
        padding: 25px
        border-bottom: solid 1px #dfe1e5

    .logo
        height: 40px
        vertical-align: middle
        margin-right: 20px
        cursor: pointer
</style>