<template>
  <div>
    <div v-for="value in imageList" :key="value.id" class="clear">
      <ul >
        <img :src="value.data"/>
      </ul>
    </div>
  </div>
</template>
<script>
import imgApi from '../../api/images' // 配置了图片上传接口地址的js文件

export default {
  data () {
    return {
      imageList: []
    }
  },
  created () {
    this.photoList()
  },
  methods: {
    // 获取图片
    photoList () {
      let temp = []
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
    }
  }
}
</script>
