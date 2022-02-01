<template>
    <div class="flex-col">
        <div class="flex items-center justify-center px-3 py-4">
            <button class="shadow-xl font-light px-3 py-4 border rounded-lg hover:text-red-400 mr-4" @click="reload()">Tutti i Corsi</button>
            <div v-for="categoria in categorie" :key="categoria.id">
                <button class="shadow-xl font-light px-3 py-4 border rounded-lg hover:text-red-400 m-4" @click="orderList(categoria.nome)">
                    {{categoria.nome}}
                </button>
            </div>
        </div>
        <div class="flex items-center justify-center px-3 py-4" v-if="errors.length">
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
            categoria:{}
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
        reload(){
            location.reload();
        }
    },

}
</script>