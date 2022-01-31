<template>
    <div class="flex-col">
        <div class="flex items-center justify-center px-3 py-4">
            <button class="shadow-xl font-light px-3 py-4 border rounded-lg hover:text-red-400 mr-4">All</button>
            <div v-for="categoria in categorie" :key="categoria.id">
                <button class="shadow-xl font-light px-3 py-4 border rounded-lg hover:text-red-400 m-4" @click="orderList()">
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
            errors:[]
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
        orderList(){

        }
    }

}
</script>