<template>
  <el-container>
    <el-aside :width="leftSize" class="aside">
      <Left v-on:listenToChildEvent="updateLeft"></Left>
    </el-aside>
    <el-main style="padding:0px;">
      <router-view/>
    </el-main>
  </el-container>
</template>

<script>
import Left from '../components/Left'

export default {
  name: 'Dashboard',
  components: {
    Left
  },
  data () {
    return {
      imgUrl: require('../assets/logo.png'),
      leftSize: '65px'
    }
  },
  methods: {
    updateLeft (isCollapse) {
      if (isCollapse === true) {
        this.leftSize = '65px'
      } else {
        this.leftSize = '151px'
      }
    }
  }
}
</script>

<style scoped>
  .el-aside {
    min-height:100vh;
  }
</style>
