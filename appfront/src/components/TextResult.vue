<template>
<div>
    <h1 id="1">这门课的评分</h1>
    <div id="myecharts-wordcloud" :style="{width: '1500px', height: '460px'}"></div>
</div>
</template>


<script>
var res
var course_name
var after=[]
var final=[]
export default {
    created: function () {
        console.log('------------------------------------------------')

        if(sessionStorage.getItem('userName')){
        this.$store.commit('setUser',sessionStorage.getItem('userName'))
        }else{
        this.$store.commit('setUser',null)
        }
        console.log(this.$store.state.isLogin + this.$store.state.userName)

        if(sessionStorage.getItem('text')){
            this.$store.commit('setText',sessionStorage.getItem('text'))
        }else{
            this.$store.commit('setText',null)
        }    
        res=JSON.parse(this.$store.state.text)
        console.log(res)

        if(sessionStorage.getItem('course')){
            this.$store.commit('setCourse',sessionStorage.getItem('course'))
        }else{
            this.$store.commit('setCourse',null)
        }
        course_name=JSON.parse(this.$store.state.course)
        console.log(course_name)

        after=[]
        for(var key in res){
            var item=res[key];
            var tmp={};
            tmp["value"]=item;
            tmp["name"]=key;
            after.push(tmp);
        }
        console.log(after)

        console.log('------------------------------------------------')

    },
    data() {
        return {
        }
    },
    mounted(){
        document.getElementById("1").innerHTML=course_name;
        this.drawLine();
    },
    methods: {
        drawLine() {          
            let myChart = this.$echarts.init(document.getElementById("myecharts-wordcloud"));          
            let option = {       
                title: {    
                    // text: "评价",         
                    textStyle: {    color: "#148D75",  },         
                    top: 14,         
                    left: 26,       
                },       
                series: [{
                    type: "wordCloud",           
                    size: ["100%", "100%"],           
                    rotationRange: [0, 0],              
                    textPadding: 0,           
                    // autoSize: { enable: true, minSize: 20, }, 
                    sizeRange: [30, 60],          
                    left: "center",                            
                    top: "center",           
                    right: null,           
                    bottom: null,           
                    textStyle: {
                    normal: {
                        fontFamily: 'sans-serif',
                        fontWeight: 'normal'
                    },
                    emphasis: {
                        shadowBlur: 10,
                        shadowColor: '#333'
                    }
                    },       
                    data:after,
                },],
            }
            myChart.setOption(option, true);   
        }
    }
}

</script>