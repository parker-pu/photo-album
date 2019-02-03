<template lang="html">
  <div>
    <el-row>
      <el-col :span="22">
         <div class="breadcrumb">
          <el-breadcrumb separator="/">
            <el-breadcrumb-item :to="{ path: '/list-img' }">我的图片</el-breadcrumb-item>
            <el-breadcrumb-item>x</el-breadcrumb-item>
          </el-breadcrumb>
        </div>
      </el-col>
      <el-col :span="2">
        <div class="grid-content bg-purple-light">
          <el-dropdown trigger="click">
            <span class="el-dropdown-link userinfo-inner">
            <i class="iconfont icon-user"></i> {{ userInfo.username }}
            <i class="el-icon-caret-bottom"></i></span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item divided @click.native="goUserInfo">
                <div><span style="color: #555;font-size: 14px">个人信息</span></div>
              </el-dropdown-item>
              <el-dropdown-item divided @click.native="logout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
      </el-col>
    </el-row>
    <div>
      <el-dialog
        title="个人信息"
        :visible.sync="openUserInfo"
        :close-on-click-modal="false"
      >
        <el-form
            :model="seeUserInfo"
            label-width="100px">
          <el-form-item label="用户名：" :label-width="seeWidth">
            <span style="float: left">{{ seeUserInfo.username }}</span>
          </el-form-item>
          <el-form-item label="用户状态：" :label-width="seeWidth">
            <span style="float: left">{{ seeUserInfo.is_active }}</span>
          </el-form-item>
          <el-form-item :formatter="dateFormat" label="最近登录：" :label-width="seeWidth">
            <span style="float: left">{{ seeUserInfo.last_login }}</span>
          </el-form-item>
          <el-form-item label="超级用户：" :label-width="seeWidth">
            <span style="float: left">{{ seeUserInfo.is_superuser }}</span>
          </el-form-item>
          <el-form-item label="姓：" :label-width="seeWidth">
            <span style="float: left">{{ seeUserInfo.first_name }}</span>
          </el-form-item>
          <el-form-item label="名：" :label-width="seeWidth">
            <span style="float: left">{{ seeUserInfo.last_name }}</span>
          </el-form-item>
          <el-form-item label="邮箱：" :label-width="seeWidth">
            <span style="float: left">{{ seeUserInfo.email }}</span>
          </el-form-item>
          <el-form-item :formatter="dateFormat" label="创建时间：" :label-width="seeWidth">
            <span style="float: left">{{ seeUserInfo.date_joined }}</span>
          </el-form-item>
        </el-form>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import userApi from '../api/user'
import moment from 'moment'
import store from '../store/index'

export default {
  store,
  data () {
    return {
      userInfo: {},
      openUserInfo: false,
      seeUserInfo: {},
      seeWidth: '120px'
    }
  },
  name: 'NavMenu',
  // 在页面加载的时候，调这个函数
  mounted: function () {
    this.getUserInfo()
  },
  methods: {
    // 时间格式化
    dateFormat (row, column) {
      let date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    },
    goUserInfo () {
      this.seeUserInfo = this.userInfo
      this.openUserInfo = true
    },
    getUserInfo () {
      // 发起get请求
      // then 指成功之后的回调 (注意：使用箭头函数，可以不考虑this指向)
      userApi.userInfo().then(({ data }) => {
        this.userInfo = data
      })
    },
    logout () {
      // 清除token
      this.$store.dispatch('UserLogout')
      if (!this.$store.state.token) {
        this.$router.push('/login')
        this.$message({
          type: 'success',
          message: '登出成功'
        })
      } else {
        this.$message({
          type: 'info',
          message: '登出失败'
        })
      }
    }
  }
}
</script>

<style scoped>
.breadcrumb {
  position: relative;
  left: 40px
}
.el-breadcrumb {
  font-size: 18px;
  line-height: 2.5
}
</style>
