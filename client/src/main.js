import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import OpenLayersMap from 'vue3-openlayers'
import 'vue3-openlayers/dist/vue3-openlayers.css'


axios.defaults.baseURL = 'http://localhost:8000'

createApp(App).use(store).use(router, axios, OpenLayersMap).mount('#app')
