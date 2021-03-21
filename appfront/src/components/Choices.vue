<template>  
<div>
    <p>你觉得是否进度如何</p>
  <el-radio-group v-model="radio">
    <el-radio :label="3">较慢</el-radio>
    <el-radio :label="6">还行</el-radio>
    <el-radio :label="9">较快</el-radio>
  </el-radio-group>
    <br>
    <br>
  <el-button @click="commit">提交评价</el-button>
</div>
</template>

<script>
  export default {
    data () {
      return {
        radio: 6
      };
    },
    methods:{
        commit(){
            this.$http.get('http://127.0.0.1:8000/api/show_courses',{

            }).then(response=>{
                this.$message.success('提交评价成功')
            })
        }
    }
  }
</script>