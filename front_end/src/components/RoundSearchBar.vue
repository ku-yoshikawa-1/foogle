<template>
    <div class="round-search-bar">
        <!-- <span>{{search}}</span> -->
        <input v-model="search" class="input-search" @keydown.enter="doSearch">
        <button class="btn-search" @click="doSearch">
            <img class="icon-search" src="./../assets/icon_search.svg" alt="">
        </button>
    </div>
</template>
<script>
    export default {
        name:"round-search-bar",
        props:['search'],
        methods: {
            doSearch(){

                if (this.searchText!=="") {
                    this.$router.push(`/search/${this.search}`)

                }
            }
        },


    }
</script>

<style lang="sass" scoped>
    .round-search-bar
        width: 400px
        position: relative
        display: inline-block
    .input-search
        width: 100%
        height: 50px
        border-radius: 25px
        border: solid 1px #dfe1e5
        outline: none
        box-sizing: border-box
        padding: 18px
    .btn-search
        height: 50px
        border-radius: 25px
        border: none
        background: none
        outline: none
        position: absolute
        right: 0
        top: 50%
        transform: translateY(-50%)
        .icon-search
            width: 25px
            height: 25px
            padding-right: 10px
            cursor: pointer

</style>