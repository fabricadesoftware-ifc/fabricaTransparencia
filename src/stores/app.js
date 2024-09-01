import { defineStore } from "pinia";
import { computed, reactive } from "vue";
import { v4 as uuidv4 } from 'uuid';
import AppService from "@/services/app";

export const useAppStore = defineStore("app",
    () => {
      const state = reactive({
        loading: false,
        error: null,
        theme: "light",
        monthsInputFilter: [],
        datas: {
          globalIndicators: {
            committed: 0,
            settled: 0,
            balance: 0
          },
          mainChart: {
            line1: null,
            line2: null,
            pie: [
              { value: 0, name: "" },
              { value: 0, name: "" },
            ],
            dataframe: null,
          },
          allNaturesChart: {
            bar1: null,
            bar2: null,
            yAxis: null,
            dataframe: null,
          },
          byMonthChart: {
            "Natureza Despesa": {},
            "Empenhado": {},
            "Liquidado": {},
            "Filtro": [],
          },
          months: [],
        }
      });

      const isDark = computed(() => state.theme === 'dark');
      const themeColor = computed(() => state.theme);
      const isLoading = computed(() => state.loading);
      const committed = computed(() => state.datas.globalIndicators.committed);
      const settled = computed(() => state.datas.globalIndicators.settled);
      const balance = computed(() => state.datas.globalIndicators.balance);
      const months = computed(() => state.datas.months);
      const monthsInput = computed(() => state.monthsInputFilter)
      const mainDataframe = computed(() => state.datas.mainChart.dataframe);
      const monthsFilter = computed(() => state.datas.byMonthChart['Filtro']);
      
      const mainChart = computed(() => {
        return {
          title: { text: "" },
          tooltip: { trigger: "axis" },
          legend: { 
            data: ["Empenhado", "Liquidado"], 
            left: "1%",
          },
          grid: { left: "2%", right: "27%", bottom: "3%", containLabel: true },
          toolbox: { feature: { saveAsImage: {} } },
          xAxis: {
            type: "category",
            boundaryGap: false,
            axisLabel: { margin: 20 },
          },
          yAxis: { type: "value" },
          series: [
            {
              name: "Empenhado",
              type: "line",
              stack: "Empenhado",
              smooth: true,
              data: state.datas?.mainChart?.line1 || [],
            },
            {
              name: "Liquidado",
              type: "line",
              stack: "Liquidado",
              smooth: true,
              data: state.datas?.mainChart?.line2 || [],
            },
            {
              name: "Soma Total (R$)",
              type: "pie",
              radius: "60%",
              center: ["87%", "50%"],
              emphasis: {
                label: {
                  show: true,
                },
              },
              label: {
                show: false,
                formatter: "{d}%",
                fontSize: 15,
                fontWeight: "bold",
                position: "center",
                color: state.theme == 'dark' ? "#fff" : "#000",
              },
              data: state.datas?.mainChart?.pie || [],
            },
          ],
        };
      });

      const allNaturesDataframe = computed(() => state.datas.allNaturesChart.dataframe);
      const allNaturesChart = computed(() => {
        return {
          title: {
            text: '',
          },
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'shadow'
            },
          },
          legend: {
            data: ['Empenhado', 'Liquidado'],
            left: '0%',
            top: '1%',
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            top: '8%',
            containLabel: true
          },
          xAxis: {
            type: 'value',
            boundaryGap: [0, 0.01]
          },
          yAxis: {
            type: 'category',
            data: state.datas?.allNaturesChart?.yAxis || [],
          },
          series: [
            {
              name: 'Empenhado',
              type: 'bar',
              emphasis: {
                focus: 'series'
              },
              label: {
                position: 'right',
                show: true,
                formatter: (params) => converterReal(params.value)
              },
              data: state.datas?.allNaturesChart?.bar1 || [],
            },
            {
              name: 'Liquidado',
              type: 'bar',
              emphasis: {
                focus: 'series'
              },
              label: {
                position: 'right',
                show: true,
                formatter: (params) => converterReal(params.value)
              },
              data: state.datas?.allNaturesChart?.bar2 || [],
            }
          ],
        };
      });

      const byMonthChart = computed(() => {
        let data1 = []
        let data2 = []
        if(state.datas?.byMonthChart?.['Natureza Despesa']) {
          data1 = Object.keys(state.datas.byMonthChart['Natureza Despesa']).map(key => {
            return {
              value: state.datas.byMonthChart['Empenhado'][key],
              name: state.datas.byMonthChart['Natureza Despesa'][key]
            };
          })
          data2 = Object.keys(state.datas.byMonthChart['Natureza Despesa']).map(key => {
            return {
              value: state.datas.byMonthChart['Liquidado'][key],
              name: state.datas.byMonthChart['Natureza Despesa'][key]
            };
          })
        }

        console.log('data1', data1)
        console.log('data2', data2)

        return {
          legend: { left: '1%', right: '2%', itemGap: 24 },
          tooltip: { trigger: 'axis', showContent: false },
          series: [
            {
              type: 'pie',
              id: String(uuidv4()),
              radius: '50%',
              center: ['25%', '70%'],
              label: {
                formatter: (params) => `${params.percent}% | R$ ${params.value}`
              },
              encode: {
                itemName: 'Natureza Despesa',
                value: 'Empenhado',
                tooltip: 'Empenhado'
              },
              data: data1
            },
            {
              type: 'pie',
              id: String(uuidv4()),
              radius: '50%',
              center: ['75%', '70%'],
              label: {
                formatter: (params) => {
                  return `${params.percent}% | R$ ${params.value}`
                }
              },
              encode: {
                itemName: 'Natureza Despesa',
                value: 'Liquidado',
                tooltip: 'Liquidado'
              },
              data: data2
            }
          ]
        }
      })

      const setTheme = (param) => {
        state.theme = param;
      }

      const getCharts = async () => {
          state.loading = true;
          try {
            state.datas = await AppService.getCharts();
          } catch (error) {
            state.error = error;
          } finally {
            state.loading = false;
          }
      }

      const converterReal = (param) => {
        return new Intl.NumberFormat('pt-BR', {
          style: 'currency',
          currency: 'BRL'
        }).format(param);
      }

      const filteringMonths = (param) => {
        // state.datas.byMonthChart["Filtro"] = param;
        // monthsFilter.value = param;
        console.log('param', param)
      }

      return {
        state,
        themeColor,
        isDark,
        isLoading,
        committed,
        settled,
        balance,
        months,
        monthsInput,
        mainChart,
        mainDataframe,
        allNaturesChart,
        allNaturesDataframe,
        byMonthChart,
        monthsFilter,
        filteringMonths,
        setTheme,
        getCharts,
      };
    }
)
