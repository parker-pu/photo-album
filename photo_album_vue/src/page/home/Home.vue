<template>
  <el-container>
    <!--头部-->
    <el-header height="36px">
      <Header></Header>
    </el-header>
    <el-container>
      <el-aside :width="leftSize">
        <Left v-on:listenToChildEvent="updateLeft"></Left>
      </el-aside>
      <el-main>
        <router-view/>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import Header from '../../components/Header'
import Left from '../../components/Left'

export default {
  name: 'Dashboard',
  components: {
    Header,
    Left
  },
  data () {
    return {
      imgUrl: require('../../assets/logo.png'),
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

</style>
