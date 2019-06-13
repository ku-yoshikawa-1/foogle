<template>
    <div class="search-result-item">
        <a class="search-result-link" :href="info.url">
            <div class="title">{{info.title}}</div>
        </a>
        <div>
            <img :src="info.imgUrl" height="200" width="300"/>
            <img :src='info.mapUrl' :id="info.id" height="200" width="300" style="display: none"/>
            <button type="button" @click="show(info.id)">Map</button>
        </div>
        <div class="period">Period: {{info.period}}</div>
        <div class="url">Website: {{info.url}}</div>
        <div class="location">Address: {{info.location}}</div>
        <div class="distance">Distance: {{info.distance}}</div>
        <div class="ori_price">Original Price: {{info.ori_price}}</div>
        <div class="price">Discounted Price: {{info.price}}</div>
        <div class="quantity">Quantity: {{info.quantity}}</div>
    </div>

</template>

<script>
    export default {
        props:["info"],
        methods:{
            show(mapid){
                if (document.getElementById(mapid).style.display == "none"){
                    document.getElementById(mapid).style.display = "block";
                }
                else {
                    document.getElementById(mapid).style.display = "none";

                }
            }
        },
    }

</script>


<style lang="sass" scoped>
    .search-result-item
        // border: solid 2px red
        text-align: left
        padding: 20px
    .title
        color: #190daa
        font-size: 1.15em
    .period
        color: #545454
    .url
        color: #006620
        font-weight: 600
    .location
        color: #006620
        font-weight: 600
    .distance
        color: #006620
        font-weight: 600
    .ori_price
        color: #006620
        font-weight: 600
    .price
        color: #006620
        font-weight: 600
    .quantity
        color: #006620
        font-weight: 600
    .search-result-link
        text-decoration: none
</style>