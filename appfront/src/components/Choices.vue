<template>  
<div>
  <h1 id="1">课程评学</h1>
  <br/> 
  <br/> 


    <p align="center">1.您觉得自己能否跟上课程的进度</p>
  <el-radio-group v-model="radio1">
    <el-radio :label=3>跟不上</el-radio>
    <el-radio :label=6>还可以</el-radio>
    <el-radio :label=9>可以跟上，并且很轻松</el-radio>
  </el-radio-group>
  <br /> 
  <br/> 


    <p align="center">2.老师所讲授的知识让你感到疑惑吗</p>
  <el-radio-group v-model="radio2">
    <el-radio :label=3>很疑惑</el-radio>
    <el-radio :label=6>有点疑惑</el-radio>
    <el-radio :label=9>没有疑惑，老师讲的简介易懂</el-radio>
  </el-radio-group>
  <br /> 
  <br/> 

    <p align="center">3.您对于这门课是否有了更加深入的认识与理解</p>
  <el-radio-group v-model="radio3">
    <el-radio :label=3>没有，只停留在皮毛</el-radio>
    <el-radio :label=6>还可以</el-radio>
    <el-radio :label=9>有了全新的认识</el-radio>
  </el-radio-group>
  <br /> 
  <br/> 

    <p align="center">4.您觉得这门课对于你的专业技能是否有提升</p>
  <el-radio-group v-model="radio4">
    <el-radio :label=3>两者没什么关联</el-radio>
    <el-radio :label=6>还行</el-radio>
    <el-radio :label=9>帮助很大</el-radio>
  </el-radio-group>
  <br /> 
  <br/> 

    <p align="center">5.作业和工程的完成对您来说有难度吗</p>
  <el-radio-group v-model="radio5">
    <el-radio :label=3>很大的难度</el-radio>
    <el-radio :label=6>一般</el-radio>
    <el-radio :label=9>没难度</el-radio>
  </el-radio-group>
  <br /> 
  <br/> 
  <br /> 
  <br/> 

  <el-button @click="commit()">提交评价</el-button>
</div>
</template>

<script>
var course_name
var teacher_name
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
          this.$http.post('http://127.0.0.1:8000/api/add_choicecomment',{
            course_name:course_name,
            teacher_name:teacher_name,
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