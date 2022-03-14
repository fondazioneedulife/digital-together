<template>
<div>
    <!--mappa-->
    <div class="fixed right-5 bottom-5 m-5">
      <div
        v-if="openMap == true"
        class="
          flex
          fixed
          right-0
          bottom-24
          px-3
          py-2
          rounded-md
          bg-orange-400
          my-2
          mr-16
          ml-10
        "
      >
        <Map></Map>
      </div>
      <button
        @click="isOpen(!openMap)"
        class="bg-orange-300 rounded-full flex border-transparent p-1"
        :class="{
          'hover:bg-orange-400': openMap == false,
        }"
      >
        <img src="@/assets/Pin.svg" alt="map" class="w-10"/>
      </button>
    </div>
    <div class="mb-24" @click="isOpen(false)">
    
    
    <!--elementi-->
    <div class="flex flex-col mt-10 a md:grid md:grid-cols-8 md:h-96 md:mt-20 items-center">
        <div class="justify-items-center w-96 mb-4 md:w-96 md:col-start-2 md:col-end-4 p-1"><img src='@/assets/Landing_1.svg'></div>
        <div class="justify-items-center text-left md:col-start-5 rounded-full md:col-end-8 p-5 md:text-left">
            <h1 class='font-medium text-4xl md:text-6xl mb-20'>LE SCUOLE E I CORSI CHE CERCHI A PORTATA DI MANO</h1>
            <router-link to='/corsi' class='btn text-white p-2 rounded'>Scopri di più</router-link>
        </div>
    </div>

    <div class="flex flex-col-reverse md:flex-col b mt-10 md:grid md:grid-cols-8 md:h-96 md:mt-20 items-center">
        <div class="justify-items-center text-left md:col-start-2 md:col-end-5 p-5 md:text-left">
            <p class='font-medium text-3xl mb-10'>OpenData</p>
            <p class='mb-20 font-light text-lg'>Tutti i nostri dati derivano da una ricerca dell’Unione Europea sulle capacità digitali dei cittadini europei. Successivamente la ricerca è stata localizzata alle zone di Verona, per permetterci di offrirti i nostri servizi adattati al tuo comune.</p>
            <router-link to='/opendata' class='btn text-white p-2 rounded'>Dati originali</router-link>
        </div>
        <div class="justify-items-center w-72 md:w-96 md:col-start-6 md:col-end-8 p-1"><img src='@/assets/Landing_2.svg'></div>
    </div>

    <div class="flex flex-col mt-10 c md:grid md:grid-cols-8 md:h-96 md:mt-20 md:mb-20 items-center">
        <div class="justify-items-center w-96 md:block md:col-start-2 md:col-end-4 p-1"><img src='@/assets/Landing_3.svg'></div>
        <div class="justify-items-center text-left md:col-start-5 md:col-end-8 p-5 md:text-left">
            <p class='font-medium text-3xl mb-10'>Mettiti alla prova</p>
            <p class='mb-20 font-light text-lg'>Il nostro test è stato semplificato selezionando le domande più importanti, dandoti uno strumento per misurare le tue capacità digitali. Il test originale è stato creato dall’Unione Europea e se sei interessat* ad aiutare la causa abbiamo anche riportato il test intero.</p>
            <span class='flex flex-row justify-start'>
                <button class='btn text-white p-2 rounded'><a target='_blank' href='https://mydigiskills.eu/it/test/index2?code=AD-3a5f6f07'>Vai al test</a></button>
            </span>
        </div>
    </div>

    <div class="flex flex-col-reverse md:flex-col mt-10 b md:grid md:grid-cols-8 md:h-96 md:mt-20 items-center">
        <div class="justify-items-center text-left md:col-start-2 md:col-end-5 p-5 md:text-left">
            <p class='font-medium text-3xl mb-10'>Scopri i corsi</p>
            <p class='mb-20 font-light text-lg'>Abbiamo catalogato tutti i corsi digitali presenti nell’area di Verona, in modo da poterti fornire uno strumento di ricerca veloce che fornisse tutte le informazioni necessarie a portata di mano.</p>
            <router-link to='/corsi' class='btn text-white p-2 rounded'>Scopri di più</router-link>
        </div>
        <div class="justify-items-center w-72 md:col-start-6 md:col-end-8 md:mapimg p-1"><img src='@/assets/Landing_4.svg'></div>
    </div>

    </div>
</div>
</template>
<script>
import Map from "@/components/Map.vue";
export default {
    components: {
        Map,
    },
    data() {
        return{
            openMap: false,
        }
    },
    methods: {
    isOpen(status) {
      if (status != this.openMap) {
        this.openMap = status;
        console.log(this.openMap);
      }
    },
  },
}
</script>
<style>
body::-webkit-scrollbar {
  display: none;
}

.top{
    border-bottom: 3px solid black;
}

.logo{
    width: 4rem;
    height: 4rem;
}

.btn{
    background-color: #FF7901;
}

.btnwhite{
    background-color: white;
    border: 0.10rem solid #FF7901;
    color: black;
}
@media screen and (min-width: 768px) {
    .a{
        background-image:url('../assets/Ellipse8.svg');
        background-position: center; 
        background-repeat: no-repeat;
        background-size: 380px 380px;
    }

    .b{
        background-image:url('../assets/sinistra.svg');
        background-position: left; 
        background-repeat: no-repeat;
        background-size: 180px 600px;
    }

    .c{
        background-image:url('../assets/destra.svg');
        background-position: right; 
        background-repeat: no-repeat;
        background-size: 180px 600px;
    }
}
.a .b .c{
    display: none
}

.mapimg{
    width: 400px;
}
</style>