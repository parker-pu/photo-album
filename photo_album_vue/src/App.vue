<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style>
  #app {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 100%;
    width: 100%;
    background-color: #f0f0f0;
  }
</style>

<script>
export default {
  name: 'App',
  data () {
    return {
      imgUrl: require('./assets/logo.png')
    }
  }
}
</script>
