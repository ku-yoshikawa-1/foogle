<template>
    <div class="search-page">
        <button type="button" @click="goHome"> Homepage </button>
        <SearchResultToolBar :search="search"/>
        <div v-for="info in searchResultList" :key="info.id">
            <SearchResultItem :info="info"/>
            <!-- <div>{{info}}</div> -->

        </div>
    </div>
</template>

<script>
    import SearchResultToolBar from "@/components/SearchResultToolBar.vue"
    import SearchResultItem from "@/components/SearchResultItem.vue"
    const DB = require("../data/search.json")
    export default {
        data(){
            return {
                searchResultList:[],
            }
        },
        computed:{
            search(){
                return this.$route.params.searchText
            }
        },
        created(){
            this.doSearchResult()
        },
        beforeRouteUpdate(to, from, next){
            next()
            this.doSearchResult();
        },
        methods:{
            doSearchResult(){
                const { searchText } = this.$route.params;
                if(DB.hasOwnProperty(searchText)){
                    this.searchResultList = DB[searchText]
                }else{
                    this.searchResultList = []
                }
                console.log("doSearchResult->",searchText,this.searchResultList)
            },
            goHome() {
                this.$router.push("/")
            }
        },
        components:{
            SearchResultToolBar,
            SearchResultItem
        },
    }
</script>