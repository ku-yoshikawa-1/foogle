<template>
    <div class="home-search-bar">
        <input type="text" class="input-search" v-model="searchText" @keydown.enter="doSearch">
        <button class="btn-search" @click="doSearch">Search</button>
    </div>
</template>

<script>
    export default {
        name:"home-search-bar",
        data() {
            return {
                searchText:""
            }
        },
        methods: {
            doSearch(){

                if (this.searchText!=="") {
                    this.$store.dispatch('initSearch', this.searchText)
                    this.$router.push(`/search/${this.searchText}`)

                }
            }
        },

    }
</script>

<style lang="sass" scoped>
    .home-search-bar
        max-width: 660px


    .input-search
        height: 55px
        width: 70%
        box-sizing: border-box
        border: solid 1px #dfe1e5
        vertical-align: bottom
        font-size: 1.2em
        outline: none
        border-top-left-radius: 5px
        border-bottom-left-radius: 5px
        padding: 18px
    .btn-search
        height: 55px
        width: 30%
        box-sizing: border-box
        color: white
        background-color: #38f
        font-size: 1.35em
        border: none
        border-top-right-radius: 5px
        border-bottom-right-radius: 5px
        cursor: pointer
</style>