<template>
  <div class="scene -gallery" ref="gallery" id="app">
    <h1 ref="heading">{{shop}}</h1>
    <div
      @click="expand(item, $event)"
      v-for="item in shop_markers"
      class="item"
      :key="item.product_name"
      :data-key="item.product_name"
      ref="itemimg"
    >
      <img :src="item.featuredImg" :alt="item.product_name" :ref="item.product_name">
      <h4>{{ item.shop_name }}</h4>
    </div>
    <app-details
      v-if="isShowing && !isMobile"
      :currentItem="currentItem"
      :topImg="topImg"
      :rects="rects"
    ></app-details>
  </div>
</template>

<script>
import AppDetails from "./AppDetails.vue";
import { TweenMax, Sine } from "gsap";
import { mapGetters } from 'vuex'

export default {
  components: {
    AppDetails,
  },
  data() {
    return {
      isShowing: false,
      isMobile: false,
      currentItem: null,
      rects: {
        first: null,
        last: null
      },
      imgOffset: 0,
      topImg: 0
    };
  },
  computed: {
    ...mapGetters([
      'shop_markers',
            'shop',
    ])
  },
  watch: {
    isShowing() {
      window.matchMedia("(min-width: 768px)").matches
        ? (this.isMobile = false)
        : (this.isMobile = true);
    }
  },
  methods: {
    expand(item, event) {
      if (window.matchMedia("(min-width: 768px)").matches) {
        const itemEl = event.target;
        const elImg = this.$refs[item.name][0];

        this.rects.first = itemEl.getBoundingClientRect();
        this.rects.last = this.$refs.gallery.getBoundingClientRect();

        if (!this.isShowing) {
          this.isShowing = true;
          this.currentItem = item;
          this.topImg = this.$refs.gallery.scrollTop;

          let deltaW = this.rects.first.left - this.rects.last.left;
          let deltaH = this.rects.first.top - this.rects.last.top;
          let deltaS = (this.rects.last.width - 30) / this.rects.first.width;

          TweenMax.to(elImg, 0.3, {
            x: -deltaW,
            y: -deltaH,
            scale: deltaS,
            transformOrigin: "0 0",
            zIndex: 1000,
            ease: Sine.easeOut
          });
        } else {
          TweenMax.to(elImg, 0.3, {
            x: 0,
            y: 0,
            scale: 1,
            transformOrigin: "0 0",
            zIndex: 0,
            ease: Sine.easeIn
          });

          this.isShowing = false;
          this.currentItem = null;
        }
      } else {
        this.isShowing = true;
        this.currentItem = item;
      }
    }
  }
};
</script>

<!--<style lang="scss">-->
<!--.scene {-->
<!--  display: flex;-->
<!--  position: relative;-->
<!--  top: 0;-->
<!--  left: 0;-->
<!--  width: $app-width;-->
<!--  height: $app-height;-->
<!--  max-height: 100%;-->

<!--  &.-gallery {-->
<!--    position: relative;-->
<!--    flex-direction: row;-->
<!--    flex-wrap: wrap;-->
<!--    justify-content: space-between;-->
<!--    align-items: flex-start;-->

<!--    > .item {-->
<!--      flex-basis: 30%;-->
<!--      flex-grow: 0;-->
<!--      flex-shrink: 0;-->
<!--      height: auto;-->
<!--      min-height: $app-width / 3;-->
<!--    }-->
<!--  }-->
<!--}-->

<!--.item {-->
<!--  transform-origin: top left;-->
<!--  cursor: pointer;-->
<!--  position: relative;-->
<!--  transform-origin: 0 0;-->

<!--  > img {-->
<!--    height: auto;-->
<!--    width: 100%;-->
<!--    position: relative;-->
<!--    backface-visibility: hidden;-->
<!--  }-->
<!--}-->

<!--h4 {-->
<!--  margin: 8px 0 30px;-->
<!--  font-weight: normal;-->
<!--}-->

<!--h1 {-->
<!--  text-align: center;-->
<!--  width: 100%;-->
<!--}-->
<!--</style>-->