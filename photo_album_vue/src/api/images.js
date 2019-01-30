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
  // 删除图片
  photoDel (data) {
    return instance.delete('/api/v1/photos/' + data.id + '/')
  },
  // 获取图片
  photoGet () {
    return instance.get('/api/v1/photos/')
  },
  // 获取源图片
  orgPhotoGet (url) {
    return instance.get(url)
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
