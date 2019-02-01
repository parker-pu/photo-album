import instance from '../axios'

export default {
  // 修改密码
  userInfo () {
    return instance.get('/api/v1/users/')
  },
  // 修改密码
  userPut (data) {
    return instance.put('/api/v1/users/' + data.id + '/', data)
  }
}
