<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style>
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
