<template>
  <div>
    <div>
        <LineChart
        :chart-data="data"
        :options="options"
        css-classes="chart-container"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue"
import { LineChart } from "vue-chart-3"
import {
  Chart,
  LineController,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement
} from "chart.js"

Chart.register(
  LineController,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement
)

const dataValues = ref([71.92, 100, 61.77, 74.54, 61.62, 69.31, 64.38,43.62,53.92,66.69])

const data = computed(() => ({
  labels: ["partecipante 1", "partecipante 2", "partecipante 3", "partecipante 4", "partecipante 5", "partecipante 6", "partecipante 7","partecipante 8","partecipante 9","partecipante 10"],
  datasets: [
    {
      label: "area 5",
      data: dataValues.value,
      backgroundColor: "#769ade",
      borderColor: '#769ade',
      borderWidth:2
      
    }
  ], 
  
}))

const options = ref({
  plugins: {
    lineTension: 1,
    responsive: true,
    title: {
      text: "Line"
    }
  }
})
</script>   