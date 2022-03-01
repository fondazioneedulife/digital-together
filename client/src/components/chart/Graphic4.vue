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

const dataValues = ref([76, 100, 53.78, 66.83, 68.67, 72.28, 63.22, 48.06,42.56,77.78])

const data = computed(() => ({
  labels: ["partecipante 1", "partecipante 2", "partecipante 3", "partecipante 4", "partecipante 5", "partecipante 6", "partecipante 7","partecipante 8","partecipante 9","partecipante 10"],
  datasets: [
    {
      label: "area 4",
      data: dataValues.value,
      backgroundColor: "#cea3e6",
      borderColor: '#cea3e6',
      borderWidth:2
    }
  ]
}))

const options = ref({
  plugins: {
    title: {
      text: "Line"
    }
  }
})
</script>