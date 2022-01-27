<template>
    <div class="m-3 px-3 py-4">
        <Breadcrumb/>
        <Detail/>
        <Map/>
    </div>
</template>
<script>
import Detail from '@/components/Detail.vue'
import Breadcrumb from '@/components/layout/Breadcrumb.vue'
import Map from '../components/Map.vue'
export default {
    components:{
        Detail,
        Breadcrumb,
        Map
    }
}
</script>