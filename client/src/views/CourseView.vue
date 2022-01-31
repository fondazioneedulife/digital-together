<template>
    <div class="flex-col m-auto ml-12 px-3 py-4">
        <div class="flex justify-start p-auto">
            <Breadcrumb/>
        </div>
        <div>
            <Detail/>
        </div>
        <!-- <Map/> -->
    </div>
</template>
<script>
import Detail from '@/components/Detail.vue'
import Breadcrumb from '@/components/layout/Breadcrumb.vue'
//import Map from '@/components/Map.vue'
export default {
    components:{
        Detail,
        Breadcrumb,
        //Map
    }
}
</script>