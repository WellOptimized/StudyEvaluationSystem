<template>
  <div id="app">
      <wordcloud
      :data="defaultWords"
      nameKey="name"
      valueKey="value"
      :color="myColors"
      :showTooltip="true"
      :wordClick="wordClickHandler">
      </wordcloud>
  </div>
</template>

<script>

import wordcloud from 'vue-wordcloud'

export default {
  name: 'app',
  components: {
    wordcloud
  },

created: function () {
    if(sessionStorage.getItem('userName')){
    this.$store.commit('setUser',sessionStorage.getItem('userName'))
    }else{
    this.$store.commit('setUser',null)
    }
    console.log('文本评价结果：'+this.$store.state.isLogin + this.$store.state.userName)


},
methods: {
    wordClickHandler(name, value, vm) {
    console.log('wordClickHandler', name, value, vm);
    }
},
data() {
return {
    myColors: ['#1f77b4', '#629fc9', '#94bedb', '#c9e0ef'],
    defaultWords: [{
        "name": this.$route.params._1,
        "value": 20
    },
    {
        "name": this.$route.params._2,
        "value": 20
    },
    {
        "name": this.$route.params._3,
        "value": 10
    },
    ]
}
}
}
</script>