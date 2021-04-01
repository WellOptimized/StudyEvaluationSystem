<template>  
<div>
    <p>你觉得是否进度如何</p>
  <el-radio-group v-model="radio1">
    <el-radio :label=3>较慢</el-radio>
    <el-radio :label=6>还行</el-radio>
    <el-radio :label=9>较快</el-radio>
  </el-radio-group>
      <p>你觉得是否进度如何</p>
  <el-radio-group v-model="radio2">
    <el-radio :label=3>较慢</el-radio>
    <el-radio :label=6>还行</el-radio>
    <el-radio :label=9>较快</el-radio>
  </el-radio-group>
      <p>你觉得是否进度如何</p>
  <el-radio-group v-model="radio3">
    <el-radio :label=3>较慢</el-radio>
    <el-radio :label=6>还行</el-radio>
    <el-radio :label=9>较快</el-radio>
  </el-radio-group>
        <p>你觉得是否进度如何</p>
  <el-radio-group v-model="radio4">
    <el-radio :label=3>较慢</el-radio>
    <el-radio :label=6>还行</el-radio>
    <el-radio :label=9>较快</el-radio>
  </el-radio-group>
        <p>你觉得是否进度如何</p>
  <el-radio-group v-model="radio5">
    <el-radio :label=3>较慢</el-radio>
    <el-radio :label=6>还行</el-radio>
    <el-radio :label=9>较快</el-radio>
  </el-radio-group>
    <br>
    <br>
  <el-button @click="commit()">提交评价</el-button>
</div>
</template>

<script>
  export default {
    data () {
      return {
        radio1: 6,
        radio2: 6,
        radio3: 6,
        radio4: 6,
        radio5: 6,
      };
    },
    created: function () {
    if(sessionStorage.getItem('userName')){
      this.$store.commit('setUser',sessionStorage.getItem('userName'))
    }else{
      this.$store.commit('setUser',null)
    }
    console.log('选择评价界面：'+this.$store.state.isLogin + this.$store.state.userName)
  },
    methods:{
      commit(){
          this.$http.post('http://127.0.0.1:8000/api/add_choicecomment',{
            course_name:'operatingsystem',
            teacher_name:'gao',
            author_name:this.$store.state.userName,
            content_1:this.radio1,
            content_2:this.radio2,
            content_3:this.radio3,
            content_4:this.radio4,
            content_5:this.radio5,

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