<template id="header">
  <!-- 头部 -->
  <div>
    <el-row>
      <el-col :span="16">
        <div class="grid-content">
        </div>
      </el-col>
      <el-col :span="1">
          <el-badge :value="12" class="item">
            <el-button size="small" class="el-icon-message">
            </el-button>
          </el-badge>
      </el-col>
      <el-col :span="1">
          <el-button size="small" class="el-icon-share"></el-button>
      </el-col>
      <el-col :span="6">
        我的名称与退出登陆按钮
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data () {
    return {}
  }
}
</script>
<style>
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
</style>
<style scoped>

</style>
