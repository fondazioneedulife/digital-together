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

const dataValues = ref([79.83, 100, 60.96, 72.57, 71.17, 76.96, 64.04,63.87,66.70, 78.39])

const data = computed(() => ({
  labels: ["partecipante 1", "partecipante 2", "partecipante 3", "partecipante 4", "partecipante 5", "partecipante 6", "partecipante 7","partecipante 8","partecipante 9","partecipante 10"],
  datasets: [
    {
      label: "area 2",
      data: dataValues.value,
      backgroundColor: "#fcba03",
      borderColor: '#fcba03',
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