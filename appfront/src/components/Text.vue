<template>
<div id="app">
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