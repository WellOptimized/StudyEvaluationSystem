// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import ElementUI from 'element-ui' 

import 'element-ui/lib/theme-chalk/index.css' 

Vue.config.productionTip = false

Vue.use(ElementUI)

import axios from 'axios'
Vue.prototype.$http = axios

import store from './store'
Vue.prototype.$store=store
/* eslint-disable no-new */

import * as echarts from 'echarts';
Vue.prototype.$echarts = echarts

require('echarts-wordcloud');

new Vue({
  el: '#app',
  router,
  store,
  echarts,
  components: { App },
  template: '<App/>'
})

