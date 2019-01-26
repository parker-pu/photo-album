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
              <el-button icon="el-icon-view" type="primary" plain></el-button>
              <el-button @click="deletePhoto(item)" icon="el-icon-delete" type="danger" plain></el-button>
            </el-button-group>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>
<script>
import imgApi from '../../api/images' // 配置了图片上传接口地址的js文件

export default {
  data () {
    return {
      imageList: [],
      pid: '',
      isEnlargeImage: false
    }
  },
  created () {
    this.photoList()
  },
  methods: {
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
              id: temp[t].id
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
    border: 1px solid rgba(0,0,0,0.3);
    background-color: rgba(0,0,0,0.4);
  }
  .itemImgChild button {
    position: relative; /* 相对定位 */
    top: 50px;
    left: 16%;
  }
</style>
