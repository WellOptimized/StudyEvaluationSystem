<template>
  <div class="courselist">
    <el-row display="margin-top:10px">
        <el-input v-model="input_course_name" placeholder="请输入课程名" style="display:inline-table; width: 30%; float:left"></el-input>
        <el-input v-model="input_teacher_name" placeholder="请输入授课教师姓名" style="display:inline-table; width: 30%; float:left"></el-input>
        
        <el-button type="primary" @click="addCourse()" style="float:left; margin: 2px;">新增</el-button>
    </el-row>
    
    <el-row>
        <el-table :data="course_list" style="width: 100%" border>
          <!-- <el-table-column prop="id" label="编号" min-width="100">
            <template scope="scope"> {{ scope.row.pk }} </template>
          </el-table-column> -->
          <el-table-column prop="book_name" label="课程名" min-width="100">
            <template scope="scope"> {{ scope.row.fields.course_name }} </template>
          </el-table-column>
          <el-table-column prop="add_time" label="授课教师" min-width="100">
            <template scope="scope"> {{ scope.row.fields.teacher_name }} </template>
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
          } else {
            this.$message.error('新增课程失败，请重试')
            console.log(res.msg)
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
            this.$message.success('查询课程成功')
          
            
          } else {
            this.$message.error('查询课程失败')
            console.log(res.msg)
          }
        })
    }
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