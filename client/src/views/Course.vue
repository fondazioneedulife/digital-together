<template>
    <div>
        <!-- <div class="flex items-center justify-center mt-10">
            <div v-for="(filt, index) in filter" :key="index"  class="relative inline-block text-center m-10">
                <div>
                    <button @click="OpenDrop()" type="button" class="inline-flex justify-center w-full rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-100 focus:ring-indigo-500" id="menu-button" aria-expanded="true" aria-haspopup="true">
                    {{filt.name}}
                    
                    <svg class="-mr-1 ml-2 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                        <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                    </button>
                </div>
                <div v-if='isOpen' class="origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="menu-button" tabindex="-1">
                    <div v-for="(c, index) in filt.choose" :key="index" class="py-1" role="none">
                        <button href="#" class="text-gray-700 block px-4 py-2 text-sm" role="menuitem" tabindex="-1" id="menu-item-0">{{c}}</button>
                    </div>
                </div>
            </div>
        </div> -->
        <div class="flex justify-center px-3 py-4 ">
            <div class="font-light border border-red-200  rounded text-black mr-3">
                <select class="m-2 p-3 mr-3 " for="">
                    <option  class="font-light" value="">Tipologia corso</option>
                </select>
                <input type="text" placeholder="cerca qui un corso" class="border ml-2 rounded-lg p-3">
                <button class="m-2 rounded px-3 py-4 bg-red-200 text-red-400">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                    </svg>
                </button>
            </div>
            <button class="flex border border-red-400 px-2 py-2 rounded font-light text-white bg-red-200">
                <p class="m-2 ">Filtri </p>
                <svg xmlns="http://www.w3.org/2000/svg" class="m-2  h-6 w-6 " fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />
                </svg>
            </button>
        </div>
        <CardCours/>
    </div>
</template>
<script>
import CardCours from '@/components/CardCours'
export default {
    components:{
        CardCours
    },
    data() {
        return{
            filter:[
                {
                    name:'Tipologia corso',
                    choose:[
                        'Corso scolastico',
                        'Corso di potenziamento'
                    ]
                },
                {
                    name:'Durata corso',
                    choose:[
                        '< 40 ore',
                        '< 100 ore',
                        '< 400 ore',
                        'Corso Annuale',
                        'Corso Biennale', 
                    ]
                },
                {
                    name:'Aree formative',
                    choose:[
                        'CAD e Grafica',
                        'Social media',
                        'Informatica',
                        'Web e e-commerce',
                        'Stampa 3d',
                    ]
                }
            ],
            isOpen: false
        }
    },
    methods:{
        OpenDrop(){
            if (this.isOpen == false){
                this.isOpen = true;
            } else if(this.isOpen == true){
                this.isOpen = false;
            }
        },
    }

}
</script>