<template>
  <a-row>
    <a-col :span="8" :offset="8">
      <a-input-search
          v-model:value="city"
          placeholder="城市，默认北京"
          enter-button="搜索"
          size="small"
          @search="get_weather"
      />
    </a-col>
  </a-row>
  <a-row>
    <a-col :span="18" :offset="3">
      <a-table
          :columns="columns"
          :data-source="weather_list"
          :pagination="{ pageSize: 10 }"
          :scroll="{ y: 200 }"
      />
    </a-col>
  </a-row>


  <a-row>
    <a-col :span="12">
      <div class="chart" ref="chart01"></div>
    </a-col>
    <a-col :span="12">
      <div class="chart" ref="chart02"></div>
    </a-col>
  </a-row>
</template>

<script>
import axios from "axios"
import * as echarts from 'echarts';
import {ref} from 'vue';

export default {
  name: "ShowCenter",
  setup() {
    const value = ref();
    return {
      value,

    };
  },
  data() {
    return {
      city: '北京',
      weather_list: [],
      columns: [
        {
          title: '时间',
          dataIndex: 'hours',
          width: 150,
        },
        {
          title: '天气',
          dataIndex: 'wea',
          width: 150,
        },
        {
          title: '温度',
          dataIndex: 'tem',
          width: 150,
        },
        {
          title: '风力',
          dataIndex: 'win',
          width: 150,
        },
      ]
    }
  },
  methods: {
    get_weather() {
      axios.get("https://v0.yiketianqi.com/api", {
            params: {
              unescape: 1,
              version: 'v62',
              appid: '66565164',
              appsecret: 'h2bVd94W',
              city: this.city
            },
          },
      ).then((response) => {
        // console.log("response:::", response.data)
        this.weather_list = response.data.hours
        this.city = response.data.city
      })
    },
    chart01() {
      // console.log(this.$refs.chart01)
      var myChart = echarts.init(this.$refs.chart01)
      var option;
      option = {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            // Use axis to trigger tooltip
            type: 'shadow' // 'shadow' as default; can also be 'line' or 'shadow'
          }
        },
        legend: {},
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'value'
        },
        yAxis: {
          type: 'category',
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        series: [
          {
            name: 'Direct',
            type: 'bar',
            stack: 'total',
            label: {
              show: true
            },
            emphasis: {
              focus: 'series'
            },
            data: [320, 302, 301, 334, 390, 330, 320]
          },
          {
            name: 'Mail Ad',
            type: 'bar',
            stack: 'total',
            label: {
              show: true
            },
            emphasis: {
              focus: 'series'
            },
            data: [120, 132, 101, 134, 90, 230, 210]
          },
          {
            name: 'Affiliate Ad',
            type: 'bar',
            stack: 'total',
            label: {
              show: true
            },
            emphasis: {
              focus: 'series'
            },
            data: [220, 182, 191, 234, 290, 330, 310]
          },
          {
            name: 'Video Ad',
            type: 'bar',
            stack: 'total',
            label: {
              show: true
            },
            emphasis: {
              focus: 'series'
            },
            data: [150, 212, 201, 154, 190, 330, 410]
          },
          {
            name: 'Search Engine',
            type: 'bar',
            stack: 'total',
            label: {
              show: true
            },
            emphasis: {
              focus: 'series'
            },
            data: [820, 832, 901, 934, 1290, 1330, 1320]
          }
        ]
      };
      option && myChart.setOption(option);
    },
    chart02() {
      // console.log(this.$refs.chart01)
      var myChart = echarts.init(this.$refs.chart02)
      var option;
      option = {
        title: {
          text: 'Referer of a Website',
          subtext: 'Fake Data',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          orient: 'vertical',
          left: 'left'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: '50%',
            data: [
              {value: 1048, name: 'Search Engine'},
              {value: 735, name: 'Direct'},
              {value: 580, name: 'Email'},
              {value: 484, name: 'Union Ads'},
              {value: 300, name: 'Video Ads'}
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      };
      option && myChart.setOption(option);
    }
  },
  mounted() {
    this.get_weather()
    this.chart01()
    this.chart02()
  }
}
</script>

<style scoped>
table {
  width: 800px;
  border-collapse: collapse;
}

td, th {
  border: 1px solid black;
}

.chart {
  height: 500px;
}
</style>