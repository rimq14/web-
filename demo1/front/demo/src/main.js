// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import ElementUI from 'element-ui'  // 引入element-ui相关组件
import 'element-ui/lib/theme-chalk/index.css';  // 引入element-ui相关组件
import router from './router' // 引入路由



Vue.use(ElementUI)   // 使用element-ui


Vue.config.productionTip = false  // 设置为false 以阻止 vue 在启动时生成生产提示


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
 render: h => h(App)
})
