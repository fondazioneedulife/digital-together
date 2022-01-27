<template>
        <div class="flex-col items-center justify-center w-screen h-screen p-10 m-5">
            <div class="grid grid-cols-1 xl:max-w-6xl max-w-4xl " v-for="corso in corsi" :key="corso.id">
                <div class="flex bg-red-100 rounded-lg px-4 py-6 m-2 shadow-2xl">
                    <div class="flex flex-col items-start ml-4 w-full">
                        <div class="flex justify-between items-center w-full ">
                            <h4 class="text-xl font-light uppercase">{{corso.nome}}</h4>
                            <h4 class="text-white bg-red-200 border border-red-400 p-2 rounded font-light">{{corso.idCategory.nome}}</h4>
                        </div>
                        <p class="text-sm font-light">data inizio: <strong>{{corso.data_inizio}}</strong>.</p>
                        <p class="text-sm font-light">docente: <strong>{{corso.docente}}</strong>.</p>
                        <p class="text-sm font-light">dove: <strong>{{corso.idGym.indirizzo}}</strong>.</p>
                        <p class="text-sm font-light">info sul corso: <br> {{corso.descrizione}}.</p>
                        <button type='button' @click="GoToCorsiView(corso)" class="p-2 leading-none rounded font-medium mt-3 bg-red-300 text-xs uppercase" >visualizza</button>
                    </div>
                </div>
            </div>
        </div>
</template>
<script>
import axios from 'axios'
export default {
    data(){
        return{
            corsi:[],
            error:[]
        }
    },
    async mounted(){
         await axios
                .get('/api/v1/corsi/')
                .then(response => {
                    this.corsi = response.data
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
        GoToCorsiView(corso){
            this.$router.push('/corsi/'+ corso.id)
        }
    }
}
</script>