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
    setText(state, text) {
      if (text) {
        state.text = text
      } else if (text == null) { //登出
        sessionStorage.setItem('text', null)
        state.text = []
      }
    },
    setCourse(state, course) {
      if (course) {
        state.course = course
      } else if (course == null) { //登出
        sessionStorage.setItem('course', null)
        state.course = []
      }
    },
    setTeacher(state, teacher) {
      if (teacher) {
        state.teacher = teacher
      } else if (teacher == null) { //登出
        sessionStorage.setItem('teacher', null)
        state.teacher = []
      }
    },
  },
});
export default store