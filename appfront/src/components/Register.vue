<template>
  <div class="login clearfix">
    <div class="login-wrap">
      <el-row type="flex" justify="center">
        <el-form ref="loginForm"  label-width="120px">
          <h3>注册</h3>
          <hr>
          
          <el-form-item prop="username" label="用户名">
            <el-input v-model="username" placeholder="请输入用户名"></el-input>
          </el-form-item>
          <el-form-item prop="email" label="邮箱">
            <el-input v-model="email" placeholder="请输入邮箱"></el-input>
          </el-form-item>
          <el-form-item prop="password" label="设置密码">
            <el-input v-model="password" show-password placeholder="请输入密码"></el-input>
          </el-form-item>
          <router-link to="/">返回登录界面</router-link>
          <el-form-item>
            <el-button type="primary" icon @click="doRegister()">注册账号</el-button>
          </el-form-item>

          
        </el-form>
      </el-row>
    </div>
  </div>
</template>
 
<script>
export default {
  name: "login",
  data() {
    return {     
        username: "",
        email: "",
        password: "",    
    }
  },
  created() {
  },
  methods: {
    doRegister() {
        if (!this.username) {
            this.$message.error("请输入用户名！");
            return;
        } else if (!this.email) {
            this.$message.error("请输入邮箱！");
            return;
        } 
        // else if (this.email != null) {
        //     var reg = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
        //     if (!reg.test(this.email)) {
        //     this.$message.error("请输入有效的邮箱！");
        //     } else if (!this.password) {
        //     this.$message.error("请输入密码！");
        //     return;
        //     } 
            else {
        // this.$http.get('http://127.0.0.1:8000/api/add_book?book_name=' + this.input)
                this.$http.post('http://127.0.0.1:8000/api/register_account',{
                   
                    username:this.username,
                    email:this.email,
                    password:this.email,
                    
                }).then( response => {
                    var res = response.data
                    if (res.error_num == 0) {
                        // this.$router.push({ path: "/Home" });
                        this.$message.success('注册帐号成功，用户名为:'+this.username)
                    } else {
                        this.$message.error('注册帐号失败，用户名为:'+this.username)
                        console.log(res.data)
                    }
                })
            }
        } 
    }
  
};
</script>
 
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.login {
  width: 100%;
  height: 740px;
  /* background: url("../assets/images/bg1.png") no-repeat; */
  background-size: cover;
  overflow: hidden;
}
.login-wrap {
  /* background: url("../assets/images/login_bg.png") no-repeat; */
  background-size: cover;
  width: 1000px;
  height: 2000px;
  margin: 215px auto;
  overflow: hidden;
  padding-top: 10px;
  line-height: 20px;
}
 
h3 {
  color: #0babeab8;
  font-size: 24px;
}
hr {
  background-color: #444;
  margin: 20px auto;
}
 
.el-button {
  width: 80%;
  margin-left: -50px;
}
</style>