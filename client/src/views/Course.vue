<template>
    <div class="flex-col">
        <div class="flex flex-row items-center justify-center  px-6">
            <div class="relative inline-block text-left shadow-xl" @click="Toggle()">
                <button type="button" class="inline-flex h-16 items-center  w-full
                        rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-lg font-light
                        text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 
                        focus:ring-offset-gray-100 focus:ring-indigo-500" id="menu-button" aria-expanded="true" aria-haspopup="true">
                {{ categorie == true ? categorie : " cerca" }}
                <!-- Heroicon name: solid/chevron-down -->
                    <svg class="-mr-1 ml-2 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                        <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                </button>
                <!-- '''''' -->
                <div v-if="isOpen" class="origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none" role="menu" aria-orientation="vertical" aria-labelledby="menu-button" tabindex="-1">
                    <div class=" " role="none">
                    <!-- Active: "bg-gray-100 text-gray-900", Not Active: "text-gray-700" -->
                        <p v-for="categoria in categorie" :key="categoria.id" class="text-gray-700 block px-4 py-2 text-sm hover:bg-gray-200 cursor-pointer " role="menuitem" tabindex="-1" id="menu-item-0">{{categoria.nome}}</p>
                    </div>
                </div>
            </div>
            <div class="m-3 w-2/4 shadow-xl rounded-lg border">
                <div class="px-2 flex items-center border-1 bg-white shadow-sm rounded-full">
                    <input class="rounded-l-sm w-full py-2 px-6 text-gray-700  rounded-lg leading-tight focus:outline-none" id="search"
                    type="text" placeholder="Search">
                    <div class="p-2">
                        <button
                            class="bg-red-300 text-white rounded-full p-2 hover:bg-red-400 focus:outline-none w-12 h-12 flex items-center justify-center">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                            </svg>
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div class="flex items-center justify-center px-3 py-2" v-if="errors.length">
            <p class="text-red-400 font-light" v-for="error in errors" v-bind:key="error">**attenzione: {{ error }}**</p>
        </div>
        <div class="flex items-center justify-center">
            <CardCours/>
        </div>
    </div>
</template>
<script>
import  axios  from "axios";
import CardCours from '@/components/CardCours'
export default {
    components:{
        CardCours
    },
    data() {
        return{
            categorie:[],
            query:'',
            errors:[],
            isOpen:false
        }
    },
    async mounted(){
         await axios
            .get('/api/v1/categorie/')
            .then(response => {
                    this.categorie = response.data
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else if (error.message) {
                        this.errors.push('Something went wrong. Please try again!')
                    }
                })
    },
    methods:{
        async orderList(categoria){
            if(categoria != this.query){
                this.query = categoria;
            }
            //let uri = window.location.search.substring(1)
            //let params = new URLSearchParams(uri)
            await axios
                .post('/api/v1/corsi/search/',{'query':this.query})
                .then(response => {
                    this.categoria = response.data[0]
                    console.log(this.categoria)
                })
                .catch(error => {
                    console.log(error)
                })
        },
        Toggle(){
            if (this.isOpen == false){
                this.isOpen = true;
            } else if(this.isOpen == true){
                this.isOpen = false;
                }
        }
    },
    // computed:{
    //     filteredDdt() {
    //         return this.ddtAll.filter(ddt => {
    //             if (this.query == "") {
    //             return true;
    //             }
    //             if (this.query.toLowerCase() == ddt.numeroDdt.toLowerCase()){
    //             return true;
    //             }
    //             return false;
    //             // return cliente.nomeCliente.toLowerCase().includes(this.query.toLowerCase())
    //         });
    //     }  
    // }  

}
</script>