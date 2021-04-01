<template>
<div class="MyAchievement">
    <div class="MyAchievement-echart">
            <div class="echart-title">这门课的评分</div>
            <div class="echart-content">
                <div id="myChart" :style="{width: '1500px', height: '460px'}"></div>
            </div>
    </div>
</div>
</template>

<script>
export default {
    created: function () {
        if(sessionStorage.getItem('userName')){
            this.$store.commit('setUser',sessionStorage.getItem('userName'))
        }else{
            this.$store.commit('setUser',null)
        }
        console.log('登录状态：'+this.$store.state.isLogin + this.$store.state.userName)

        if(sessionStorage.getItem('grades')){
            this.$store.commit('setGrades',sessionStorage.getItem('grades'))
        }else{
            this.$store.commit('setGrades',null)
        }
        console.log('分数'+this.$store.state.grades)
    },
    data() {
        return {
        }
    },
    mounted(){
        this.drawLine();
    },
    methods: {
        drawLine(){
            var myChart = this.$echarts.init(document.getElementById('myChart'));//获取容器元素
            var option = {
                tooltip : {
                    trigger: 'axis'
                },
                grid: {
                    left: '6%',
                    right: '6%',
                    bottom: '6%',
                    containLabel: true
                },
                legend: {
                    data:['分数'],
                    left: '6%',
                    top: 'top',
                    itemWidth: 15,//图例图标的宽
                    itemHeight: 15,//图例图标的高
                    textStyle: {
                        color: '#3a6186',
                        fontSize:20,
                    }
                },
                toolbox: {
                    show : true,
                    feature : {
                        magicType : {show: true, type: [ 'bar']},
                    },
                    right: '6%',
                },
                calculable : true,
                xAxis : [
                    {
                        type : 'category',
                        data : ['1','2','3','4','5'],
                        splitLine: {show: false},//去除网格分割线
                        axisTick: {//刻度
                            show: false//不显示刻度线
                        },
                        axisLine: {//坐标线
                            lineStyle: {
                                type: 'solid',
                                color: '#e7e7e7',//轴线的颜色
                                width:'2'//坐标线的宽度
                            }
                        },
                        axisLabel: {
                            textStyle: {
                                color: '#3a6186',//坐标值的具体的颜色
                            }
                        },
                        splitLine: {
                            show: false//去掉分割线
                        },
                    }
                ],
                yAxis : [
                    {
                        type : 'value',
                        axisLine: {//线
                            show: false
                        },
                        axisTick: {//刻度
                            show: false
                        },
                    }
                ],
                series : [
                    {
                        name:'分数',
                        type:'bar',
                        barWidth: 20,
                        data:[this.$store.state.grades[0],this.$store.state.grades[2],this.$store.state.grades[4],this.$store.state.grades[6],this.$store.state.grades[8]],
                        itemStyle: {
                            normal: {
                                color: '#00abf7',//设置柱子颜色
                                label: {
                                    show: true,//柱子上显示值
                                    position: 'top',//值在柱子上方显示
                                    textStyle: {
                                        color: '#00abf7',//值的颜色
                                        fontSize:16,
                                    }
                                }
                            }
                        },
                    },
                ]
            };
            //防止越界，重绘canvas
            window.onresize = myChart.resize;
            myChart.setOption(option);//设置option
        }
    }
}
</script>