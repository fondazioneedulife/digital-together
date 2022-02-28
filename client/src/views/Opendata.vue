<template>
    <div>
     <section class="text-gray-700 body-font">
      <div class="container mx-auto flex px-5 py-24 md:flex-col flex-col items-start">
        <div class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center">
          <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">Open Data
            <br class="hidden lg:inline-block">
          </h1>
        </div>
        <div class="lg:w-full md:w-2/2 w-6/6">
          Il nostro sito è stato creato basandoci su dei dati raccolti a livello europeo, riguardante le abilità digitali dei cittadini.<br class="hidden lg:inline-block">
          Con abilità digitali si intende la capacità di districarsi autonomamente attraverso la tecnologia.<br class="hidden lg:inline-block">
          Il test è stato soggetto a persone volontarie, in maniera casuale, ed è suddiviso in 5 aree:<br class="hidden lg:inline-block">
          <span class="font-bold">1)</span>  Alfabetizzazione su informazione e dati<br class="hidden lg:inline-block">
          <span class="font-bold">2)</span> Comunicazione e collaborazione<br class="hidden lg:inline-block">
          <span class="font-bold">3)</span> Creazione di contenuti digitali<br class="hidden lg:inline-block">
          <span class="font-bold">4)</span> Sicurezza<br class="hidden lg:inline-block">
          <span class="font-bold">5)</span> Problem solving<br class="hidden lg:inline-block">
          I dati sono rappresentati in diagrammi per semplificarne la comprensione
        </div>
      </div>
    </section>
      <section class="text-gray-700 body-font">
        <div class="container mx-auto flex px-5 py-24 md:flex-row flex-col items-center">
          <div class=" lg:w-full md:w-1/2 w-5/6">
            <Graphic class="object-cover object-center rounded"/>
          </div>
          <div class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center">
            <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">Alfabetizzazione su  
              <br class="hidden lg:inline-block">informazione e dati
            </h1>
          </div>
        </div>
      </section>
      <section class="text-gray-700 body-font">
        <div class="container mx-auto flex px-5 py-24 md:flex-row flex-col items-center">
          <div class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center">
            <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">Comunicazione 
              <br class="hidden lg:inline-block">e collaborazione
            </h1>
          </div>
          <div class="lg:w-full md:w-1/2 w-5/6">
            <Graphic2 class="object-cover object-center rounded"/>
          </div>
        </div>
      </section>
      <section class="text-gray-700 body-font">
        <div class="container mx-auto flex px-5 py-24 md:flex-row flex-col items-center">
          <div class=" lg:w-full md:w-1/2 w-5/6">
            <Graphic3 class="object-cover object-center rounded"/>
          </div>
          <div class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center">
            <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">Creazione di  
              <br class="hidden lg:inline-block">contenuti digitali
            </h1>
          </div>
        </div>
      </section>
      <section class="text-gray-700 body-font">
        <div class="container mx-auto flex px-5 py-24 md:flex-row flex-col items-center">
          <div class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center">
            <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">Sicurezza 
              <br class="hidden lg:inline-block">
            </h1>
          </div>
          <div class="lg:w-full md:w-1/2 w-5/6">
            <Graphic4 class="object-cover object-center rounded"/>
          </div>
        </div>
      </section>
      <section class="text-gray-700 body-font">
        <div class="container mx-auto flex px-5 py-24 md:flex-row flex-col items-center">
          <div class="lg:w-full md:w-1/2 w-5/6">
            <Graphic5 class="object-cover object-center rounded"/>
          </div>
          <div class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center">
            <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">Problem 
              <br class="hidden lg:inline-block">solving 
            </h1>
          </div>
        </div>
      </section>
    </div>
</template>
<script>
import Graphic from '@/components/chart/Graphic.vue'
import Graphic2 from '@/components/chart/Graphic2.vue'
import Graphic3 from '@/components/chart/Graphic3.vue'
import Graphic4 from '@/components/chart/Graphic4.vue'
import Graphic5 from '@/components/chart/Graphic5.vue'
export default {
  components: { 
    Graphic,
    Graphic2,
    Graphic3,
    Graphic4,
    Graphic5
  },
  
}
</script>