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
    },
    setGrades(state, grades) {
      if (grades) {
        state.grades = grades
      } else if (grades == null) { //登出
        sessionStorage.setItem('grades', null)
        state.grades = []
      }
    },
  },
});
export default store