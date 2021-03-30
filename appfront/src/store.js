import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const store = new Vuex.Store({
	state: {
    userName: "",
    isLogin: false,
	},
	mutations: {
    setUser(state, user) {
      if (user) {
        state.userName = user
        state.isLogin=true
      } else if (user == null) { //登出
        sessionStorage.setItem('userName', null)
        sessionStorage.setItem('isLogin', false)
        state.userName = ''
        state.isLogin = false
      }
    }


  },
});
export default store