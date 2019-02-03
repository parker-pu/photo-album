<template id="left">
  <!-- 左边 -->
  <div>
    <el-menu default-active="/"
             class="el-menu-vertical-demo"
             :collapse="isCollapse" router>
      <el-menu-item index="">
        <div class="el-menu-item-div">
          <i class="el-icon-arrow-right" v-if="isCollapse" @click="openLeft"></i>
          <i class="el-icon-arrow-left" v-else @click="closeLeft"></i>
        </div>
      </el-menu-item>
      <el-menu-item index="/list-img">
        <div class="el-menu-item-div">
          <i class="el-icon-picture-outline"></i>
          <span slot="title">我的图片</span>
        </div>
      </el-menu-item>
      <el-menu-item index="/upload-img">
        <div class="el-menu-item-div">
          <i class="el-icon-upload"></i>
          <span slot="title">上传图片</span>
        </div>
      </el-menu-item>
      <el-menu-item index="/put-password">
        <div class="el-menu-item-div">
          <i class="el-icon-setting"></i>
          <span slot="title">设置</span>
        </div>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  data () {
    return {
      isCollapse: true
    }
  },
  methods: {
    closeLeft () {
      this.isCollapse = true
      this.$emit('listenToChildEvent', this.isCollapse)
    },
    openLeft () {
      this.isCollapse = false
      this.$emit('listenToChildEvent', this.isCollapse)
    }
  }
}
</script>

<style scoped>
  .el-menu-vertical-demo {
    position: absolute;
    left: 0;
    top: 0;
    min-height: 100vh;
    color: #999;
    background-color: #323544;
  }
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 120px;
    min-height: 100vh;
    color: #999;
    background-color: #323544;
  }
  .el-menu--collapse {
    width: 40px;
  }
  .el-menu-item {
    font-size: 14px;
    color: #999;
    cursor: pointer;
    padding-left: 10px;
  }
  /*.el-tooltip {*/
  .el-menu-item-div {
    position: absolute;
    left: 0;
    top: 0;
    height: 100%;
    width: 100%;
    display: inline-block;
    box-sizing: border-box;
    padding: 0 9px;
  }
  /* 鼠标移动到字体的颜色 */
  .el-menu-item:hover {
    background: #404351;
    cursor: pointer;
    color: #fff;
  }
  /* 设置图标的颜色 */
  .el-menu-item i {
    color: rgb(184, 190, 196);
  }
  .el-menu-item i:hover {
    color: #fff;
  }
</style>

<style scoped>

</style>
