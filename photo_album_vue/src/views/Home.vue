<template>
  <el-container>
    <el-aside :width="leftSize" class="aside">
      <Left v-on:listenToChildEvent="updateLeft"></Left>
    </el-aside>
    <el-container>
      <!-- 面包屑 -->
      <el-header style="height: 40px;">
        <Breadcrumb></Breadcrumb>
      </el-header>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import Breadcrumb from '../components/Breadcrumb'
import Left from '../components/Left'

export default {
  name: 'Home',
  components: {
    Left,
    Breadcrumb
  },
  data () {
    return {
      imgUrl: require('../assets/logo.png'),
      leftSize: '40px'
    }
  },
  methods: {
    updateLeft (isCollapse) {
      if (isCollapse === true) {
        this.leftSize = '40px'
      } else {
        this.leftSize = '120px'
      }
    }
  }
}
</script>

<style scoped>
  .el-aside {
    min-height:100vh;
  }
  .el-header {
    background-color: #ffffff;
    color: #333;
    line-height: 40px;
  }
</style>
