<template>
  <div id="box" class="">
    <ul>
      <li v-for="item in imageList" :key="item.id">
        <div class="itemImg">
          <img v-bind:src="item.data" alt=""
               @mouseover="mouseOver(item)"
               @mouseout="mouseOut(item)">
          <div v-if="pid === item.id" class="itemImgChild">
            <el-button-group>
              <el-button @click="showPhoto(item)" icon="el-icon-view" type="primary" plain></el-button>
              <el-button @click="deletePhoto(item)" icon="el-icon-delete" type="danger" plain></el-button>
            </el-button-group>
          </div>
        </div>
      </li>
    </ul>
    <el-dialog :visible.sync="showImg" width="80%" title="" append-to-body>
      <el-container>
        <el-aside width="50%">
          <img width="100%" height="100%" :src="showData.imgData" alt="">
        </el-aside>
        <el-main>
          <el-form :model="showData"
                   ref="editForm">
            <el-form-item label="名称" :label-width="formLabelWidth">
              <el-input v-model="showData.name" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="描述" :label-width="formLabelWidth">
              <el-input v-model="showData.describe" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="创建时间" :label-width="formLabelWidth">
              <el-date-picker type="date" v-model="showData.insertTime"
                @change="dateFormat" style="width:100%;">
              </el-date-picker>
              <!--<span>{{ showData.insertTime }}</span>-->
            </el-form-item>
            <el-form-item label="更新时间" :label-width="formLabelWidth">
              <span>{{ showData.updateTime }}</span>
            </el-form-item>
          </el-form>
        </el-main>
      </el-container>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" icon="el-icon-refresh" @click="downloadImg">更新</el-button>
        <el-button type="primary" icon="el-icon-download" @click="downloadImg">下载</el-button>
      </div>
    </el-dialog>
  </div>
</template>
<script>
import imgApi from '../../api/images' // 配置了图片上传接口地址的js文件
// import moment from 'moment'

export default {
  data () {
    return {
      showImg: false,
      showData: {},
      formLabelWidth: '100px',
      imageList: [],
      pid: '',
      isEnlargeImage: false
    }
  },
  created () {
    this.photoList()
  },
  methods: {
    // 时间格式化
    dateFormat (date) {
      // let date = row[column.property]
      // if (date === undefined) {
      //   return ''
      // }
      return date
      // return moment(date).format('YYYY-MM-DD HH:mm:ss')
    },
    // 获取图片
    photoList () {
      let temp = []
      this.imageList = []
      imgApi.photoGet().then((response) => {
        temp = response.data
        if (temp.length > 0) {
          for (let t = 0; t < temp.length; t++) {
            this.imageList.push({
              name: temp[t].name,
              data: 'data:image/png;base64,' + temp[t].thumbnail,
              id: temp[t].id,
              describe: temp[t].describe,
              insertTime: temp[t].insert_time,
              updateTime: temp[t].update_time
            })
          }
        }
      }).catch((error) => {
        console.log(error)
      })
    },
    // 鼠标移动到图片
    mouseOver (row) {
      this.pid = row.id
    },
    // 鼠标移出
    mouseOut (row) {
    },
    showPhoto (row) {
      this.showImg = true
      imgApi.orgPhotoGet(row).then((response) => {
        let imgData = 'data:image/png;base64,' +
          btoa(new Uint8Array(response.data).reduce((data, byte) =>
            data + String.fromCharCode(byte), ''))
        this.showData = Object.assign({}, row) // 这句是关键
        this.showData.imgData = imgData
      })
    },
    deletePhoto (row) {
      this.$confirm('此操作将永久删除该图片, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        imgApi.photoDel(row).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success'
          })
          this.photoList()
        }).catch((error) => {
          console.log(error)
        })
      }).catch(() => {
        this.$notify.info({
          title: '取消',
          message: '已取消删除'
        })
      })
    },
    downloadImg () {
      // 生成一个a元素
      let a = document.createElement('a')
      // 创建一个单击事件
      let event = new MouseEvent('click')
      // 为下载的图片设置一个名称
      a.download = name || this.showData.name
      // 将生成的URL设置为a.href属性
      a.href = this.showData.imgData
      // 触发a的单击事件
      a.dispatchEvent(event)
    }
  }
}
</script>

<style scoped>
  #box ul {
    display: flex;
    flex-wrap: wrap;
  }

  #box li {
    list-style: none;
  }

  .itemImg {
    position: relative; /* 相对定位 */
    width: 148px;
    height: 148px;
    margin-right: 1px;
    border: 2px solid #eee;
  }

  .itemImg img {
    position: absolute; /* 据对定位 */
    width: 100%;
    height: 100%;
  }

  .itemImgChild {
    position: absolute; /* 据对定位 */
    width: 100%;
    height: 100%;
    border: 1px solid rgba(0, 0, 0, 0.3);
    background-color: rgba(0, 0, 0, 0.4);
  }

  .itemImgChild button {
    position: relative; /* 相对定位 */
    top: 50px;
    left: 16%;
  }
</style>
