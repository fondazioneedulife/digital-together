<template>
<div>
    <ol-map ref="map" :loadTilesWhileAnimating="true" :loadTilesWhileInteracting="true" style="height:500px">
    <ol-view ref="view" :center="center" :rotation="rotation" :zoom="zoom" :projection="projection" />
    <ol-tile-layer>
        <ol-source-osm />
    </ol-tile-layer>
    <ol-vector-layer>
        <ol-source-vector>
            <ol-feature>
                <ol-geom-multi-point :coordinates="coordinates"></ol-geom-multi-point>
                <ol-style>
                    <ol-style-icon :src="markerIcon" :scale="1"></ol-style-icon>
                </ol-style>
            </ol-feature>
        </ol-source-vector>
    </ol-vector-layer>
</ol-map>
</div>
</template>

<script>
import { ref, inject } from 'vue'

import markerIcon from '@/assets/place.svg'
export default {
    setup() {
        const center = ref([11, 45.45])
        const projection = ref('EPSG:4326')
        const zoom = ref(12)
        const rotation = ref(0)
        const coordinates = ref([[10.999020713202624, 45.43096190830851], [10.98563922484148, 45.40336630316935], [11.018044869025559, 45.52346858176481]])

        const format = inject('ol-format');

        const geoJson = new format.GeoJSON();
     

        return {
            center,
            projection,
            zoom,
            rotation,
            geoJson,
            markerIcon,
            coordinates
        }
    },
}
</script>