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
          <!-- <router-link to="/">返回登录界面</router-link> -->
          <!-- <router-link to="/register">注册账号</router-link> -->
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
      
  },
  methods: {
    doLogin() {
      // if (!this.username) {
      //   this.$message.error("请输入用户名！");
      //   return;
      // } else if (!this.password) {
      //   this.$message.error("请输入密码！");
      //   return;
      // } else 
      {
            this.$http.post('http://127.0.0.1:8000/api/login_account',{
            
                username:this.username,
                password:this.password,
            
        }).then(response => {
            console.log(response);
            if (response.data.error_num == 0) {
              this.$message.success('登录账号成功，用户名为:'+this.username)
              this.$router.push({ path: "/courselist" });

            } else {
              // alert("您输入的用户名或密码错误！");
              this.$message.error(response.data.msg+' : '+this.username)
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