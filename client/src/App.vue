<template>
  <div class="flex-col w-full">
    <Navbar/>
    <router-view/>
  </div>
</template>
<script>
import Navbar from '@/components/layout/Navbar.vue'
export default {
  components: {
    Navbar
  }
}
</script>
