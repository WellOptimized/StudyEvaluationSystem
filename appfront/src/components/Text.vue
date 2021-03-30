<template>
<div id="app">
  <p>请输入文本评价</p>
  <el-input
    type="textarea"
    :autosize="{ minRows: 3, maxRows: 5}"
    placeholder="请输入内容"
    v-model="textarea3">
  </el-input>

  <el-button @click="commit">提交评价</el-button>
</div>
</template>

<script>
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
  },
  methods:{
    commit(){
        this.$http.post('http://127.0.0.1:8000/api/add_textcomment',{
            course_name:'operatingsystem',
            teacher_name:'1',
            author_name:this.$store.state.userName,
            content:this.textarea3,
        }).then(response=>{
            this.$message.success('提交文本评价成功')
        })
    }
  }
}
</script>