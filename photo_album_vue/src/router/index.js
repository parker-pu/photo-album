import Vue from 'vue'
import Router from 'vue-router'
import Home from '../page/home/Home'
import Login from '../page/login/Login'
import store from '../store/index.js'
import UploadImg from '../page/photo/Upload'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/',
      name: 'Home',
      component: Home,
      meta: {
        requiresAuth: true
      },
      children: [
        // 上传图片
        {
          path: '/upload_img',
          name: 'UploadImg',
          component: UploadImg,
          meta: {
            requiresAuth: true
          }
        }
      ]
    }
  ]
})

// 注册全局钩子用来拦截导航
router.beforeEach((to, from, next) => {
  // 获取store里面的token
  let token = store.state.token
  // 判断要去的路由有没有requiresAuth
  if (to.meta.requiresAuth) {
    if (token) {
      next()
    } else {
      next({
        path: '/login',
        query: {redirect: to.fullPath}
        // 将刚刚要去的路由path（却无权限）作为参数，方便登录成功后直接跳转到该路由
      })
    }
  } else {
    next()// 如果无需token,那么随它去吧
  }
})

export default router
