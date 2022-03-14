<template>
  <div>
    <ol-map
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

      <ol-fullscreen-control v-if="fullscreencontrol" tipLabel="full-screen"/>

      <ol-tile-layer>
        <ol-source-osm />
      </ol-tile-layer>

      <span v-for="gym in palestra" v-bind:key="gym.idGym">
      <ol-vector-layer>
        <ol-source-vector>
          <ol-feature>
            <ol-geom-multi-point
              :coordinates="[[gym.lat, gym.long]]"
            ></ol-geom-multi-point>
            <ol-style>
              <ol-style-icon :src="markerIcon" :scale="1"></ol-style-icon>
            </ol-style>
          </ol-feature>
        </ol-source-vector>
      </ol-vector-layer>
      </span>
    </ol-map>
  </div>
</template>

<script>
import { ref, inject } from "vue";

import markerIcon from "@/assets/PointMap.svg";
import axios from "axios";
export default {
  setup() {
    const center = ref([11, 45.44]);
    const projection = ref("EPSG:4326");
    const zoom = ref(11);
    const rotation = ref(0);
    const coordinates = ref([
      [0,0],      
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
          fullscreencontrol: true,
          lat: "",
          long: "",
          palestra: {},
          errors: [],
      }
  },
  async mounted() {
    await axios
      .get("/api/v1/palestre/")
      .then((response) => {
        this.palestra = response.data;
        console.log(this.palestra);
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