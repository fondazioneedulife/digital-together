<template>
  <div class="flex flex-col mx-10 py-4">
    <div class="flex justify-start p-auto">
      <Breadcrumb />
    </div>
    <div class="flex items-start w-full">
      <Detail class='w-screen'/>
    </div>
    <!-- <Map/> -->
  </div>
</template>
<script>
import Detail from "@/components/Detail.vue";
import Breadcrumb from "@/components/layout/Breadcrumb.vue";

//import Map from '@/components/Map.vue'
export default {
  components: {
    Detail,
    Breadcrumb,
    //Map
  },
};
</script>
