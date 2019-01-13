import instance from '../axios'

export default {
  // 用户注册
  uploadUrl () {
    return '/api/v1/photos/'
  },
  // 用户登录
  userLogin (data) {
    return instance.post('/api-token-auth/', data)
  }
}
