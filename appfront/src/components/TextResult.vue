<template>
<div id="myecharts-wordcloud" :style="{width: '1500px', height: '460px'}"></div>
</template>


<script>
var res

export default {
    created: function () {
        if(sessionStorage.getItem('userName')){
        this.$store.commit('setUser',sessionStorage.getItem('userName'))
        }else{
        this.$store.commit('setUser',null)
        }
        console.log('文本评价结果：'+this.$store.state.isLogin + this.$store.state.userName)

        if(sessionStorage.getItem('text')){
            this.$store.commit('setText',sessionStorage.getItem('text'))
        }else{
            this.$store.commit('setText',null)
        }    

        res=JSON.parse(this.$store.state.text)
    },
    data() {
        return {
        }
    },
    mounted(){
        this.drawLine();
    },
    methods: {
        drawLine() {          
            let myChart = this.$echarts.init(       document.getElementById("myecharts-wordcloud")     );          
            let option = {       
                title: {    
                    text: "评价",         
                    textStyle: {    color: "#148D75",  },         
                    top: 14,         
                    left: 26,       
                },       
                series: [{
                    type: "wordCloud",           
                    size: ["80%", "80%"],           
                    rotationRange: [0, 0],              
                    textPadding: 0,           
                    autoSize: { enable: true, minSize: 14, },           
                    left: "center",                            
                    top: "center",           
                    right: null,           
                    bottom: null,           
                    textStyle: {             
                        normal: {               
                            color: function() {return "#056E71" },             
                            },           
                    },           
                    data: [res


                    
                    ]
                },],
            }
            myChart.setOption(option, true);   
        }
    }
}

</script>