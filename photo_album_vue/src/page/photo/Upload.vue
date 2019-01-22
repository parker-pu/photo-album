<template>
  <div style="padding: 50px;">
    <el-form class="form-wrapper padding"
             ref="editForm"
             :model="editForm"
             :rules="editRules"
             label-width="110px">
      <el-form-item label="描述：">
        <el-input
          type="textarea"
          :autosize="{ minRows: 1, maxRows: 4}"
          placeholder="请输入内容"
          v-model="fileData.describe">
        </el-input>
      </el-form-item>
      <el-form-item label="上传图片：" prop="photo">
        <el-upload
          :action="upLoadUrl"
          :before-upload="beforeUploadPicture"
          multiple
          accept="image/png, image/jpeg, image/jpg"
          list-type="picture-card"
          :on-preview="handlePictureCardPreview"
          :on-remove="photoRemoveFun"
          :on-progress="uploadProgress"
          :on-success="uploadSuccess"
          :on-error="uploadError"
          name="photo"
          :data="fileData"
          :file-list="editFiles"
          :headers="myHeaders"
          :show-file-list="true">
          <i class="el-icon-plus"></i>
        </el-upload>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="photoSubmit">保存</el-button>
      </el-form-item>
    </el-form>
    <el-dialog class="preview-modal" :visible.sync="imgVisible" append-to-body>
      <img width="100%" :src="dialogImageUrl" alt="photo">
    </el-dialog>
  </div>
</template>
<script>
import imgApi from '../../api/images' // 配置了图片上传接口地址的js文件
import store from '../../store'

export default {
  data () {
    return {
      editVisible: false,
      fileData: {
        describe: null
      },
      myHeaders: {
        Authorization: store.state.token
      },
      editForm: { // 编辑表单
        photo: '', // 活动图片
        describe: '' // 图片描述
      },
      editRules: { // 表单验证规则
        photo: [{required: true, message: '请上传活动图片', trigger: 'blur'}]
      },
      removeData: '',
      editFiles: [],
      // submitImg: [], // 需要提交的图片
      uploadComplete: true,
      upLoadUrl: imgApi.uploadUrl(),
      imgVisible: false, // 上传图片预览
      dialogImageUrl: '' // 图片预览地址
    }
  },
  created () {
    this.initInfo()
  },
  methods: {
    // 获取缓存的图片
    initInfo () {
      // 这里photo应从服务器获取，存储的是数组，请按照相应格式获取图片url（这里直接给值）
      let temp = []
      imgApi.cachePhotoGet().then((response) => {
        temp = response.data
        if (temp.length > 0) {
          for (let t = 0; t < temp.length; t++) {
            // 通过[{name: 'name', url: 'url地址'}]格式初始化照片墙
            this.editFiles.push({
              name: temp[t].name,
              url: 'data:image/png;base64,' + temp[t].thumbnail,
              id: temp[t].id
            })
          }
        }
        this.editVisible = true
      }).catch((error) => {
        console.log(error)
      })
    },
    // 提交图片
    photoSubmit () {
      if (!this.uploadComplete) {
        this.$message.error('图片正在提交')
        return
      }
      // 调用提交接口
      imgApi.photoAdd(this.fileData).then(() => {
        this.$notify({
          title: '成功',
          message: '提交成功',
          type: 'success'
        })
      }).catch((error) => {
        console.log(error)
      })
    },
    // 上传图片前调用方法
    beforeUploadPicture (file) {
      if (file.size > 10 * 1024 * 1024) {
        this.$message.error('上传图片不能大于10M')
        return false
      }
    },
    // 上传图片时调用
    uploadProgress (event, file, fileList) {
      this.uploadComplete = false
    },
    // 上传图片成功
    uploadSuccess (res, file, fileList) {
      this.uploadComplete = true
      // this.$set(this.submitImg, res.id, res.name)
      // this.fileChange(fileList)
    },
    // 上传图片出错
    uploadError () {
      // uploadError (err, file, fileList) {
      this.$message.error('上传出错')
    },
    // 移除图片
    photoRemoveFun (file, fileList) {
      if (file.id === undefined) {
        this.removeData = file.response
      } else {
        this.removeData = file
      }
      imgApi.cachePhotoDel(this.removeData).then(() => {
        this.$notify({
          title: '成功',
          message: '删除成功',
          type: 'success'
        })
      }).catch((error) => {
        console.log(error)
      })
    },
    // 图片预览
    handlePictureCardPreview (file) {
      this.dialogImageUrl = file.url
      this.imgVisible = true
    }
  }
}
</script>
