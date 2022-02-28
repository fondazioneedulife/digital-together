<template>
  <div class="flex w-full">
    <div class="flex flex-row w-full font-light">
      <div class="flex flex-col w-full">
        <div class="flex text-3xl font-bold content-start text-left py-4">
          {{ categoria.nome }}
        </div>
        <div class="flex w-full h-44">
          <img :src="categoria.immagine" alt="img" class="w-full" />
        </div>
        <div class="justify-between px-5 py-6 text-xl text-left">
          <span class="text-3xl font-bold">{{ corso.nome }}</span> <br />
          <p>
            data inizio: {{ corso.data_inizio }} / data fine:
            {{ corso.data_fine }}
          </p>
        </div>
        <hr />
        <h1 class="px-5 py-6 text-xl text-orange-400">caratteristiche:</h1>
        <div class="flex px-5 py-6">
          <p>{{ corso.descrizione }}</p>
        </div>
        <h1 class="px-5 py-2 text-xl text-orange-400">contatti:</h1>
        <div class="flex flex-col px-5 py-2">
          <p>cellulare: {{ palestra.telefono }}</p>
          <p>email: {{ palestra.email }}</p>
          <p>indirizzo: {{ palestra.indirizzo }}</p>
        </div>
        <ol-map
          v-if="this.lat && this.long"
          ref="map"
          :loadTilesWhileAnimating="true"
          :loadTilesWhileInteracting="true"
          style="height: 20rem; width: 60vw"
        >
          <ol-view
            ref="view"
            :center="center"
            :rotation="rotation"
            :zoom="zoom"
            :projection="projection"
          />

          <ol-fullscreen-control
            v-if="fullscreencontrol"
            tipLabel="full-screen"
          />

          <ol-tile-layer>
            <ol-source-osm />
          </ol-tile-layer>

          <ol-vector-layer>
            <ol-source-vector>
              <ol-feature>
                <ol-geom-multi-point
                  :coordinates="[[this.lat, this.long]]"
                ></ol-geom-multi-point>
                <ol-style>
                  <ol-style-icon :src="markerIcon" :scale="1"></ol-style-icon>
                </ol-style>
              </ol-feature>
            </ol-source-vector>
          </ol-vector-layer>
        </ol-map>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { ref, inject } from "vue";
import markerIcon from "@/assets/PointMap.svg";
export default {
  setup() {
    const center = ref([11, 45.44]);
    const projection = ref("EPSG:4326");
    const zoom = ref(11);
    const rotation = ref(0);
    const coordinates = ref([
      [0, 0],
    ]);

    const format = inject('ol-format');
    console.log(format);

    const geoJson = new format.GeoJSON();

    return {
      center,
      projection,
      zoom,
      rotation,
      geoJson,
      markerIcon,
      coordinates,
    };
  },
  data() {
    return {
      corso: {},
      categoria: {},
      palestra: {},
      errors: [],
      fullscreencontrol: true,
      lat: "",
      long: "",
    };
  },
  async mounted() {
    let id = this.$route.params.id;
    await axios
      .get("/api/v1/corsi/" + id + "/")
      .then((response) => {
        this.corso = response.data;
        this.categoria = response.data.idCategory;
        this.palestra = response.data.idGym;
        this.lat = this.palestra.lat;
        this.long = this.palestra.long;
        console.log(this.lat, this.long);
        this.mapsetup();
      })
      .catch((error) => {
        if (error.response) {
          for (const property in error.response.data) {
            this.errors.push(`${property}: ${error.response.data[property]}`);
          }
        } else if (error.message) {
          this.errors.push("Something went wrong. Please try again!");
        }
      });
  },
};
</script>
