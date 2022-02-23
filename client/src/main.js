import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import VueAxios from 'vue-axios'
import OpenLayersMap from 'vue3-openlayers'
import 'vue3-openlayers/dist/vue3-openlayers.css'

axios.defaults.baseURL = 'http://localhost:8000'

const app = createApp(App);

app.use(router);
app.use(store);
app.use(OpenLayersMap);
app.use(VueAxios,axios);

app.mount("#app");
