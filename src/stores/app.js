import { defineStore } from "pinia";
import { computed, reactive } from "vue";
import AppService from "@/services/app";

export const useAppStore = defineStore("app",
    () => {
      const state = reactive({
        loading: false,
        error: null,
        theme: "light",
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
          months: []
        }
      });

      const isDark = computed(() => state.theme === 'dark');
      const themeColor = computed(() => state.theme);
      const isLoading = computed(() => state.loading);
      const committed = computed(() => state.datas.globalIndicators.committed);
      const settled = computed(() => state.datas.globalIndicators.settled);
      const balance = computed(() => state.datas.globalIndicators.balance);
      const months = computed(() => state.datas.months);

      const mainDataframe = computed(() => state.datas.mainChart.dataframe);
      
      const mainChart = computed(() => {
        return {
          title: { text: "" },
          tooltip: { trigger: "axis" },
          legend: { 
            data: ["Empenhado", "Liquidado"], 
            left: "1%",
          },
          grid: { left: "2%", right: "23.5%", bottom: "3%", containLabel: true },
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
              center: ["89%", "50%"],
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

      const setTheme = (theme) => {
        state.theme = theme;
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

      const converterReal = (value) => {
        return new Intl.NumberFormat('pt-BR', {
          style: 'currency',
          currency: 'BRL'
        }).format(value);
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
          mainChart,
          mainDataframe,
          allNaturesChart,
          allNaturesDataframe,
          setTheme,
          getCharts,
      };
    }
)
