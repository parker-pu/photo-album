<template>
  <div>
    <el-row>
      <el-col :span="10" :offset="7">
        <el-tabs v-model="activeName">

          <el-tab-pane label="登录" name="login">
            <el-form :model="loginForm" :rules="rules" label-width="100px" ref="loginForm">
              <el-form-item label="用户名" prop="username">
                <el-input v-model="loginForm.username"></el-input>
              </el-form-item>
              <el-form-item label="密码" prop="password">
                <el-input v-model="loginForm.password" type="password"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submitForm('loginForm')">提交</el-button>
                <el-button @click="resetForm('loginForm')">重置</el-button>
              </el-form-item>
            </el-form>
          </el-tab-pane>

          <el-tab-pane label="注册" name="register">
            <Register></Register>
          </el-tab-pane>

        </el-tabs>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import api from '../../api/login'
// 引入注册组件
import Register from './Register'
import store from '../../store/index'

export default {
  store,
  data () {
    return {
      activeName: 'login', // 选项卡
      loginForm: { // 表单v-model的值
        username: '',
        password: ''
      },
      rules: { // 验证规则
        username: [
          {required: true, message: '用户名不能少', trigger: 'blur'},
          {min: 3, max: 16, message: '用户名在3到16位之间', trigger: 'blur'}
        ],
        password: [
          {required: true, message: '请输入密码', trigger: 'blur'}
        ]
      }
    }
  },
  methods: {
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) { // 验证通过
          api.userLogin(this.loginForm)
            .then(({data}) => { // 解构赋值拿到data
              if (data.token) {
                this.$message({
                  type: 'success',
                  message: '登录成功'
                })
                this.$store.dispatch('UserLogin', data.token)
                // 如果用户手动输入"/"那么会跳转到这里来，即this.$route.query.redirect有参数
                let redirectUrl = decodeURIComponent(this.$route.query.redirect || '/')
                // 跳转到指定的路由
                this.$router.push({
                  path: redirectUrl
                  // path: '/'
                })
              } else {
                this.$message({
                  type: 'info',
                  message: '登录失败！'
                })
              }
            })
        } else {
          // 验证不通过
          return false
        }
      })
    }
  },
  components: {
    Register
  }
}
</script>
<style scoped>

</style>
