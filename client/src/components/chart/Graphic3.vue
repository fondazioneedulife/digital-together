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

const dataValues = ref([52, 93.75, 37.38, 54.25, 64.63, 45.81, 60.63, 43.75, 37.44, 56.25])

const data = computed(() => ({
  labels: ["partecipante 1", "partecipante 2", "partecipante 3", "partecipante 4", "partecipante 5", "partecipante 6", "partecipante 7","partecipante 8","partecipante 9","partecipante 10"],
  datasets: [
    {
      label: "area 3",
      data: dataValues.value,
      backgroundColor: "#03fc98",
      borderColor: '#03fc98',
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