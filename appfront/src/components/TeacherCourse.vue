<template>
  <div class="courselist">
    <el-row display="margin-top:10px">
        <el-input v-model="input_course_name" placeholder="请输入课程名" style="display:inline-table; width: 30%; float:left"></el-input>
        <el-input v-model="input_teacher_name" placeholder="请输入授课教师姓名" style="display:inline-table; width: 30%; float:left"></el-input>
        
        <el-button type="primary" @click="addCourse()" style="float:left; margin: 2px;">新增</el-button>

        <el-button type="primary" @click="dialogVisibleForModifyAccount = true" >修改帐号密码</el-button>
        <el-dialog title="修改帐号密码" :visible.sync="dialogVisibleForModifyAccount">
          <el-form :model="form">
            <el-form-item label="帐号名称" :label-width="formLabelWidth">
              <el-input v-model="form.username" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="修改后密码" :label-width="formLabelWidth">
              <el-input v-model="form.password" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogVisibleForModifyAccount = false">取 消</el-button>
            <el-button type="primary" @click="handleCloseForModifyAccount();dialogVisibleForModifyAccount=false;">确 定</el-button>
          </div>
        </el-dialog>

        <el-button type="primary" @click="dialogVisibleForDeleteEvaluation = true">删除评论</el-button>
        <el-dialog title="删除评论" :visible.sync="dialogVisibleForDeleteEvaluation">
          <el-form :model="form">
            <el-form-item label="帐号名称" :label-width="formLabelWidth">
              <el-input v-model="form.username" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="课程名称" :label-width="formLabelWidth">
              <el-input v-model="form.coursename" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="教师姓名" :label-width="formLabelWidth">
              <el-input v-model="form.teachername" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogVisibleForDeleteEvaluation = false">取 消</el-button>
            <el-button type="primary" @click="handleCloseForDeleteEvaluation();dialogVisibleForDeleteEvaluation=false;">确 定</el-button>
          </div>
        </el-dialog>

        <el-button type="primary" @click="dialogVisibleForDeleteAccount = true">删除帐号</el-button>
        <el-dialog title="删除帐号" :visible.sync="dialogVisibleForDeleteAccount">
          <el-form :model="form">
            <el-form-item label="帐号名称" :label-width="formLabelWidth">
              <el-input v-model="form.username" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogVisibleForDeleteAccount = false">取 消</el-button>
            <el-button type="primary" @click="handleCloseForDeleteAccount();dialogVisibleForDeleteAccount=false;">确 定</el-button>
          </div>
        </el-dialog>

    </el-row>
    
    <el-row>
        <el-table :data="course_list" style="width: 100%" border>
          <el-table-column prop="course_name" label="课程名" min-width="30">
            <template slot-scope="scope"> {{ scope.row.fields.course_name }} </template>
          </el-table-column>
          <el-table-column prop="teacher_name" label="授课教师" min-width="30">
            <template slot-scope="scope"> {{ scope.row.fields.teacher_name }} </template>
          </el-table-column>
          <el-table-column prop="evaluate_button" label="评学入口" min-width="50">
            <template slot-scope="scope">
              <el-button @click.native="jumpToDetail('/courselist/' + scope.row.fields.course_name+'/choices')">定量评学</el-button>
            
              <el-button @click.native="jumpToDetail('/courselist/' + scope.row.fields.course_name+'/text')">定性评学</el-button>

            </template>
          </el-table-column>
          <el-table-column prop="delete_button" label="管理课程" min-width="100">
            <template slot-scope="scope">
            <!-- <el-button @click.native="modifyCourse(scope.row.fields.course_name,scope.row.fields.teacher_name)">修改课程信息</el-button> -->
            
            <el-button type="primary" @click="dialogVisibleForModifyCourse = true" >修改课程信息</el-button>
            <el-dialog title="修改课程信息" :visible.sync="dialogVisibleForModifyCourse">
              <el-form :model="form">
                <el-form-item label="课程名称" :label-width="formLabelWidth">
                  <el-input v-model="form.coursename" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="教师姓名" :label-width="formLabelWidth">
                  <el-input v-model="form.teachername" autocomplete="off"></el-input>
                </el-form-item>
              </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button @click="dialogVisibleForModifyCourse = false">取 消</el-button>
                <el-button type="primary" @click="handleCloseForModifyCourse(scope.row.fields.course_name,scope.row.fields.teacher_name);dialogVisibleForModifyCourse=false;">确 定</el-button>
              </div>
            </el-dialog>
            
            <el-button type="primary" @click.native="deleteConfirm(scope.row.fields.course_name,scope.row.fields.teacher_name)">删除课程</el-button>
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
      dialogVisibleForDeleteAccount: false,
      form: {
          username: '',
          coursename:'',
          teachername:'',
          password:'',
      },
      formLabelWidth: '120px',

      dialogVisibleForDeleteEvaluation :false,
      dialogVisibleForModifyCourse:false,
      dialogVisibleForModifyAccount:false,

    }
  },
  created: function () {
    this.showCourses()
  },
  methods: {
    handleCloseForDeleteAccount() {
      console.log(this.form.username)           //从数据库中删除该帐号 以及 该账号所留下的所有评论    
      this.$http.post('http://127.0.0.1:8000/api/delete_account',{
          user_name:this.form.username,        
      }).then( response => {
          var res = response.data
          if (res.error_num == 0) {
            this.showCourses()
            this.$message.success(res['msg'])
          } else {
            this.$message.error(res['msg'])
          }
      })
      this.form.username=''
      this.form.coursename=''
      this.form.teachername=''
      this.form.password=''
    },
    handleCloseForDeleteEvaluation() {
      console.log(this.form.username)
      console.log(this.form.coursename)
      console.log(this.form.teachername)
      this.$http.post('http://127.0.0.1:8000/api/delete_evaluation',{
        user_name:this.form.username,    
        course_name:this.form.coursename,
        teacher_name:this.form.teachername,
      }).then( response => {
          var res = response.data
          if (res.error_num == 0) {
            this.showCourses()
            this.$message.success(res['msg'])
          } else {
            this.$message.error(res['msg'])
          }
      })
      this.form.username=''
      this.form.coursename=''
      this.form.teachername=''
      this.form.password=''

    },
    handleCloseForModifyCourse(a,b) {
      this.$http.post('http://127.0.0.1:8000/api/modify_course',{
        course_name:a,
        teacher_name:b,
        aim_course_name:this.form.coursename,
        aim_teacher_name:this.form.teachername,
      }).then( response => {
          var res = response.data
          if (res.error_num == 0) {
            this.showCourses()
            this.$message.success(res['msg'])
          } else {
            this.$message.error(res['msg'])
          }
      })
      this.form.username=''
      this.form.coursename=''
      this.form.teachername=''
      this.form.password=''

    },
    handleCloseForModifyAccount(){
      this.$http.post('http://127.0.0.1:8000/api/modify_account',{
      user_name:this.form.username,
      password:this.form.password,
      }).then( response => {
          var res = response.data
          if (res.error_num == 0) {
            this.showCourses()
            this.$message.success(res['msg'])
          } else {
            this.$message.error(res['msg'])
          }
      })
      this.form.username=''
      this.form.coursename=''
      this.form.teachername=''
      this.form.password=''
    },
    handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
    },
    addCourse () {
      this.$http.post('http://127.0.0.1:8000/api/add_course',{
        
          course_name:this.input_course_name,
          teacher_name:this.input_teacher_name,
        
      }).then( response => {
          var res = response.data
          if (res.error_num == 0) {
            this.showCourses()
            this.$message.success('成功添加课程')
            this.input_course_name=''
            this.input_teacher_name=''
          } else {
            this.$message.error(res['msg'])
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
            this.$message.error(res['msg'])
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
            this.$message.success('删除课程成功')
            this.showCourses()
          } else {
            this.$message.error(res['msg'])
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

            let grades=res.result
            
            sessionStorage.setItem('grades',JSON.stringify(grades))
            this.$store.commit('setGrades',grades)

            sessionStorage.setItem('course',JSON.stringify(course_name))
            this.$store.commit('setCourse',course_name)
            

            this.$router.push({name:'ChoicesResult'})

          } else {
            this.$message.error(res['msg'])
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
            
            let text=res.result

            sessionStorage.setItem('text',JSON.stringify(text))
            this.$store.commit('setText',text)

            sessionStorage.setItem('course',JSON.stringify(course_name))
            this.$store.commit('setCourse',course_name)
            
            this.$router.push({name:'TextResult'})

          } else {
            this.$message.error(res['msg'])
          }
        })
    },
    modifyCourse(course_name,teacher_name){
      
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