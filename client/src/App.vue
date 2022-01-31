<template>
  <div class="flex-col w-full">
    <Navbar/>
    <router-view/>
    <Footer/>
  </div>
</template>
<script>
import Navbar from '@/components/layout/Navbar.vue'
import Footer from '@/components/layout/Footer.vue'
export default {
  components: {
    Navbar, Footer
  }
}
</script>
