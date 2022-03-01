<template>
  <div class="px-0 md:mx-24 mx-3 flex flex-col mt-10 mb-10">
    <section class="text-black body-font max-w-screen-lg md:mx-auto mx-2 p-1">
      <h1 class="font-bold my-8 text-3xl md:text-6xl">Open Data</h1>
      <div class="lg:w-full md:w-2/2 w-6/6 font-light text-lg">
        Il nostro sito è stato creato basandoci su dei dati raccolti a livello
        europeo, riguardante le abilità digitali dei cittadini.<br
          class="hidden lg:inline-block"
        />
        Con abilità digitali si intende la capacità di districarsi autonomamente
        attraverso la tecnologia.<br class="hidden lg:inline-block" />
        Il test è stato soggetto a persone volontarie, in maniera casuale, ed è
        suddiviso in 5 aree:<br class="hidden lg:inline-block" />
        <ol>
          <li><span>1) </span> Alfabetizzazione su informazione e dati</li>
          <li><span>2) </span>Comunicazione e collaborazione</li>
          <li><span>3) </span>Creazione di contenuti digitali</li>
          <li><span>4) </span>Sicurezza</li>
          <li><span>5) </span>Problem solving</li>
        </ol>
        I dati sono rappresentati in diagrammi per semplificarne la comprensione
      </div>
    </section>
    <section class="text-black mt-12">
      <div class="container mx-auto flex px-5 py-6 md:flex-row flex-col-reverse items-center" >
        <div class="lg:w-full md:w-1/4 w-full">
          <Graphic class="object-cover object-center rounded w-auto h-full" />
        </div>
        <div class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-center md:text-left mb-16 md:mb-0 items-center text-center">
          <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-black">
            Alfabetizzazione su
            <br class="hidden lg:inline-block" />informazione e dati
          </h1>
        </div>
      </div>
    </section>
    <section class="text-gray-700 body-font">
      <div class="container mx-auto flex px-5 py-6 md:flex-row flex-col items-center">
        <div class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-center md:text-left mb-16 md:mb-0 items-center text-center">
          <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-black">
            Comunicazione <br class="hidden lg:inline-block" />e collaborazione
          </h1>
        </div>
        <div class="lg:w-full md:w-1/4 w-full">
          <Graphic2 class="object-cover object-center rounded" />
        </div>
      </div>
    </section>
    <section class="text-gray-700 body-font">
      <div class="container mx-auto flex px-5 py-6 md:flex-row flex-col-reverse items-center">
        <div class="lg:w-full md:w-1/4 w-full">
          <Graphic3 class="object-cover object-center rounded" />
        </div>
        <div class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-center md:text-left mb-16 md:mb-0 items-center text-center" >
          <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900" >
            Creazione di <br class="hidden lg:inline-block" />contenuti digitali
          </h1>
        </div>
      </div>
    </section>
    <section class="text-gray-700 body-font">
      <div class="container mx-auto flex px-5 py-6 md:flex-row flex-col items-center">
        <div class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-center md:text-left mb-16 md:mb-0 items-center text-center">
          <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">
            Sicurezza
            <br class="hidden lg:inline-block" />
          </h1>
        </div>
        <div class="lg:w-full md:w-1/4 w-full">
          <Graphic4 class="object-cover object-center rounded" />
        </div>
      </div>
    </section>
    <section class="text-gray-700 body-font">
      <div class="container mx-auto flex px-5 py-6 md:flex-row flex-col-reverse items-center">
        <div class="lg:w-full md:w-1/4 w-full">
          <Graphic5 class="object-cover object-center rounded" />
        </div>
        <div class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-center md:text-left mb-16 md:mb-0 items-center text-center">
          <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">
            Problem <br class="hidden lg:inline-block" />solving
          </h1>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import Graphic from "@/components/chart/Graphic.vue";
import Graphic2 from "@/components/chart/Graphic2.vue";
import Graphic3 from "@/components/chart/Graphic3.vue";
import Graphic4 from "@/components/chart/Graphic4.vue";
import Graphic5 from "@/components/chart/Graphic5.vue";
export default {
  components: {
    Graphic,
    Graphic2,
    Graphic3,
    Graphic4,
    Graphic5,
  },
};
</script>
<style>
span{
  font-weight: bold;
}

</style>
