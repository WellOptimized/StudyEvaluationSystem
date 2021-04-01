<template>
  <div class="login" clearfix>
    <div class="login-wrap">
      <el-row type="flex" justify="center">
        <el-form ref="loginForm" label-width="80px">
          <h3>登录</h3>
          <hr>
          <el-form-item prop="username" label="用户名">
            <el-input v-model="username" placeholder="请输入用户名" prefix-icon></el-input>
          </el-form-item>
          <el-form-item id="password" prop="password" label="密码">
            <el-input v-model="password" show-password placeholder="请输入密码"></el-input>
          </el-form-item>

          <el-form-item>
            <el-button type="primary"  @click="goToReigster()">注 册</el-button>
          </el-form-item>

          <el-form-item>
            <el-button type="primary"  @click="doLogin()">登 录</el-button>
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
        password: "",
    }
  },
  created :function (){
    if(sessionStorage.getItem('userName')){
      this.$store.commit('setUser',sessionStorage.getItem('userName'))
    }else{
      this.$store.commit('setUser',null)
    }
    console.log('登录界面：'+this.$store.state.isLogin + this.$store.state.userName)
  },
  methods: {
    doLogin() {
      if (!this.username) {
        this.$message.error("请输入用户名！");
        return;
      } else if (!this.password) {
        this.$message.error("请输入密码！");
        return;
      } else 
      {
        this.$http.post('http://127.0.0.1:8000/api/login_account',{ 
          username:this.username,
          password:this.password,  
        }).then(response => {
            console.log(response);
            if (response.data.error_num == 0) {
              this.$message.success(response.data.msg)

              if(response.data.info==3){
                this.$router.push({ path: "/courselist" })
              }
              else if(response.data.info==2){
                this.$router.push({ path: "/teachercourse" })
              }
              else if(response.data.info==1){
                this.$router.push({ path: "/studentcourse" })
              }

              sessionStorage.setItem('userName',this.username)
              this.$store.commit('setUser',this.username)

            } else {
              this.$message.error(response.data.msg)
            }
          });
      }
    },
    goToReigster(){
      this.$router.push({ path: "/Register" });
    }
  }
};
</script>
 
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.login {
  position: absolute;
  top:0px;
  right: 0px;
  width: 100%;
  height: 100%;
  /* background: url("../assets/login.jpg"); */
  background-size: cover;
  overflow: hidden;
}
.login-wrap {
  background-size: cover;
  width: 100%;
  height: 100%;
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