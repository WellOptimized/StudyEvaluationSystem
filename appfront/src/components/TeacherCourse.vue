<template>
  <div class="courselist">
    <!-- <el-row display="margin-top:10px">
        <el-input v-model="input_course_name" placeholder="请输入课程名" style="display:inline-table; width: 30%; float:left"></el-input>
        <el-input v-model="input_teacher_name" placeholder="请输入授课教师姓名" style="display:inline-table; width: 30%; float:left"></el-input>
        
        <el-button type="primary" @click="addCourse()" style="float:left; margin: 2px;">新增</el-button>
    </el-row> -->
    
    <el-row>
        <el-table :data="course_list" style="width: 100%" border>
          <el-table-column prop="course_name" label="课程名" min-width="100">
            <template slot-scope="scope"> {{ scope.row.fields.course_name }} </template>
          </el-table-column>
          <el-table-column prop="teacher_name" label="授课教师" min-width="100">
            <template slot-scope="scope"> {{ scope.row.fields.teacher_name }} </template>
          </el-table-column>
          <!-- <el-table-column prop="evaluate_button" label="评学入口" min-width="100">
            <template slot-scope="scope">
              <el-button @click.native="jumpToDetail('/courselist/' + scope.row.fields.course_name+'/choices')">定量评学</el-button>
            
              <el-button @click.native="jumpToDetail('/courselist/' + scope.row.fields.course_name+'/text')">定性评学</el-button>

            </template>
          </el-table-column> -->
          <el-table-column prop="delete_button" label="管理课程" min-width="100">
            <template slot-scope="scope">
            <!-- <el-button @click.native="deleteConfirm(scope.row.fields.course_name,scope.row.fields.teacher_name)">删除课程</el-button> -->
            <el-button @click.native="showTextResult(scope.row.fields.course_name,scope.row.fields.teacher_name)">展示文本评价</el-button>
            <el-button @click.native="showChoiceResult(scope.row.fields.course_name,scope.row.fields.teacher_name)">展示选择评价</el-button>
            </template>
          </el-table-column>
        
        </el-table>
    </el-row>
  </div>

</template>
<script>
export default {
  name: 'courselist',
  data () {
    return {
      input_course_name: '',
      input_teacher_name:'',
      course_list: [],
    }
  },
  created: function () {
    if(sessionStorage.getItem('userName')){
      this.$store.commit('setUser',sessionStorage.getItem('userName'))
    }else{
      this.$store.commit('setUser',null)
    }
    console.log('课程列表界面：'+this.$store.state.isLogin + this.$store.state.userName)

    this.showCourses()
  },
  methods: {
    addCourse () {
      this.$http.post('http://127.0.0.1:8000/api/add_course',{
        
          course_name:this.input_course_name,
          teacher_name:this.input_teacher_name,
        
      }).then( response => {
          var res = response.data
          if (res.error_num == 0) {
            this.showCourses()
            this.$message.success(res.msg)
            this.input_course_name=''
            this.input_teacher_name=''
          } else {
            this.$message.error(res.msg)
          }
        })
    },
    showCourses () {
      this.$http.get('http://127.0.0.1:8000/api/show_courses')
        .then( response => {
          var res = response.data
          console.log(res)
          if (res.error_num == 0) {
            this.course_list = res['list']
          } else {
            this.$message.error(res.msg)
          }
        })
    },
    jumpToDetail(url){
      this.$router.push({ path: url });
    },
    deleteCourse(course_name,teacher_name){
      this.$http.post('http://127.0.0.1:8000/api/delete_course',{
          course_name:course_name,
          teacher_name:teacher_name,
      }).then( response => {
          var res = response.data
          if (res.error_num == 0) {
            this.$message.success(res.msg)
            this.showCourses()
          } else {
            this.$message.error(res.msg)
            console.log(res.msg)
          }
        })
    },
    deleteConfirm(course_name,teacher_name){
        this.$confirm('确定删除该课程?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.deleteCourse(course_name,teacher_name)
        })
    },
    showChoiceResult(course_name,teacher_name){
      this.$http.post('http://127.0.0.1:8000/api/get_choice_results',{
          course_name:course_name,
          teacher_name:teacher_name,
      }).then( response => {
          var res = response.data
          if (res.error_num == 0) { 
            var grades=res.result
            this.$router.push({name:'ChoicesResult',params:{a:grades[0],b:grades[1],c:grades[2],d:grades[3],e:grades[4]}})
          } else {
            this.$message.error(res.msg)
            console.log(res.msg)
          }
        })
    },
    showTextResult(course_name,teacher_name){
      this.$http.post('http://127.0.0.1:8000/api/get_text_results',{
          course_name:course_name,
          teacher_name:teacher_name,
      }).then( response => {
          var res = response.data
          if (res.error_num == 0) { 
            console.log(res.result)
            
            var grades={_1:"进度",_2:"难度",_3:"跟上"}
            this.$router.push({name:'TextResult',params:grades})
          } else {
            this.$message.error(res.msg)
            console.log(res.msg)
          }
        })
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }
  ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>