// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import {
  Button, Select, MessageBox, Message, MenuItem, Menu,
  Tabs, Row, Col, Upload, TabPane, Form, FormItem, Input,
  ButtonGroup, Dialog, Container, Aside, Main, Notification
} from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)
Vue.use(Button)
Vue.use(ButtonGroup)
Vue.use(Select)
Vue.use(Menu)
Vue.use(MenuItem)
Vue.use(Tabs)
Vue.use(Row)
Vue.use(Col)
Vue.use(Upload)
Vue.use(TabPane)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Dialog)
Vue.use(Container)
Vue.use(Aside)
Vue.use(Main)

Vue.prototype.$confirm = MessageBox.confirm // 提示删除
Vue.prototype.$notify = Notification // 左上脚弹出
Vue.prototype.$message = Message // 消息提示

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})
