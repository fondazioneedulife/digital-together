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

const dataValues = ref([91.75, 100, 52.75, 72.42, 80.67, 83.42, 72.50, 69.50, 72.33, 88.92])

const data = computed(() => ({
  labels: ["partecipante 1", "partecipante 2", "partecipante 3", "partecipante 4", "partecipante 5", "partecipante 6", "partecipante 7","partecipante 8","partecipante 9","partecipante 10"],
  datasets: [
    {
      label: "area 1",
      data: dataValues.value,
      backgroundColor: "#dc322f",
      borderColor: '#dc322f',
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