<template>
  <el-upload
    class="upload-demo"
    drag
    name="file"
    :action="startUpload()"
    multiple
    enctype="multipart/form-data"
    :on-error="uploadError"
    :on-success="handleAvatarSuccess"
    :before-upload="beforeUpload">
    <i class="el-icon-upload"></i>
    <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
  </el-upload>
</template>

<script>
export default {
  data () {
    return {}
  },
  methods: {
    startUpload () {
      // 生产环境和开发环境的判断
      // return process.env.BASE_API + '/api/v1/photos/'
      return '/api/v1/photos/'
    },
    beforeUpload (file) {
      this.files = file
      const extension = file.name.split('.')[1].toUpperCase() === 'JPG'
      const extension2 = file.name.split('.')[1].toUpperCase() === 'PNG'
      const isLt2M = file.size / 1024 / 1024 < 20
      if (!extension && !extension2) {
        this.$message.warning('上传的图片格式只能是 jpg 或者是 png')
      }
      if (!isLt2M) {
        this.$message.warning('上传图片大小不能超过 20MB!')
      }
      // this.fileName = file.name
      return true // 返回false不会自动上传
    },
    uploadError () {
      this.$message.error('上传失败，请重新上传')
    },
    handleAvatarSuccess (res, file) {
      alert(res)
      console.log(res)
      alert(file)
    }
  }
}
</script>

<style scoped>

</style>
