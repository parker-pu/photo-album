<template lang="html">
  <div>
    <div class="resetPd">
      <el-form :model="pdForm" :rules="rules" ref="pdForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="旧密码" prop="oldPass">
          <el-input v-model="pdForm.oldPass"></el-input>
        </el-form-item>
        <el-form-item label="新密码" prop="pass">
          <el-input v-model="pdForm.pass"></el-input>
        </el-form-item>
        <el-form-item label="再次输入" prop="checkPass">
          <el-input v-model="pdForm.checkPass"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitForm('pdForm')">立即修改</el-button>
          <el-button @click="resetForm('pdForm')">重置</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import userApi from '../../api/user'

export default {
  name: 'Password',
  data () {
    var passRules = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.pdForm.checkPass !== '' && value !== this.pdForm.checkPass) {
          callback(new Error('两次输入密码不一致!'))
        }
        callback()
      }
    }
    var checkPassRules = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.pdForm.pass) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      pdForm: {
        oldPass: '',
        pass: '',
        checkPass: ''
      },
      userInfo: {},
      rules: {
        oldPass: [{ required: true, message: '请输入旧密码', trigger: 'blur' }],
        pass: [{ required: true, validator: passRules, trigger: 'blur' }],
        checkPass: [{ required: true, validator: checkPassRules, trigger: 'blur' }]
      }
    }
  },
  created () {
    userApi.userInfo().then((response) => {
      this.userInfo = response.data
    })
  },
  methods: {
    // 提交修改信息
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$confirm('是否更改密码？', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
          }).then(() => {
            this.userInfo.password = this.pdForm.pass
            userApi.userPut(this.userInfo).then(() => {
              this.$notify({
                title: '成功',
                message: '修改成功',
                type: 'success'
              })
              this.$router.push({ path: '/list-img' })
            }).catch((error) => {
              console.log(error)
            })
          }).catch(() => {
            this.$notify.info({
              title: '取消',
              message: '已取消删除'
            })
          })
        } else {
          return false
        }
      })
    },
    // 重置输入信息
    resetForm (formName) {
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<style scoped>
  .resetPd {
    position: absolute; /* 相对定位 */
    top: 10%;
    left: 30%;
    width: 40%;
  }
</style>
