<template>
<div id="app">
  <h1 id="1">课程评学</h1>
  <br/>
  <br/>
  <el-input
    type="textarea"
    :autosize="{ minRows: 5, maxRows: 10}"
    placeholder="请输入内容"
    v-model="textarea3">
  </el-input>

  <br/>
  <br/>
  <br/>
  <br/>
  <br/>

  <el-button @click="commit">提交评价</el-button>
</div>
</template>

<script>
var course_name
var teacher_name
export default {
  data() {
    return {
      textarea3: '',
    }
  },
  created: function () {
    if(sessionStorage.getItem('userName')){
      this.$store.commit('setUser',sessionStorage.getItem('userName'))
    }else{
      this.$store.commit('setUser',null)
    }
    console.log('文本评价界面：'+this.$store.state.isLogin + this.$store.state.userName)
    if(sessionStorage.getItem('course')){
      this.$store.commit('setCourse',sessionStorage.getItem('course'))
    }else{
      this.$store.commit('setCourse',null)
    }
    course_name=JSON.parse(this.$store.state.course)
    if(sessionStorage.getItem('teacher')){
      this.$store.commit('setTeacher',sessionStorage.getItem('teacher'))
    }else{
      this.$store.commit('setTeacher',null)
    }
    teacher_name=JSON.parse(this.$store.state.teacher)
    console.log(course_name,teacher_name)

  },
  mounted:function(){
    document.getElementById("1").innerHTML=course_name;
  },
  methods:{
    commit(){
        this.$http.post('http://127.0.0.1:8000/api/add_textcomment',{
            course_name:course_name,
            teacher_name:teacher_name,
            author_name:this.$store.state.userName,
            content:this.textarea3,
        }).then(response=>{
            if (response.data.error_num == 0) {
              this.$message.success('提交评价成功')
            }else{
              this.$message.error('你已经评价过这门课程了')
            }
        })
    }
  }
}
</script>