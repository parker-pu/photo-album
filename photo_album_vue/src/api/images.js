import instance from '../axios'

export default {
  // 图片缓存上传
  uploadUrl () {
    return '/api/v1/photos-cache/'
  },
  // 提交缓冲区中的图片
  photoAdd (data) {
    return instance.post('/api/v1/photos/', data)
  },
  // 获取缓冲区中的图片
  cachePhotoGet () {
    return instance.get('/api/v1/photos-cache/')
  },
  // 缓存的图片删除
  cachePhotoDel (data) {
    return instance.delete('/api/v1/photos-cache/' + data.id + '/')
  }
}
