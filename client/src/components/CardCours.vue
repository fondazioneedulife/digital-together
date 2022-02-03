<template>
            <div class="grid grid-cols-1 xl:max-w-6xl max-w-4xl">
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
</template>
<script>
export default {
    props:{
        corso:Object
    },
    data(){
        return{
        }
    },
    methods:{
        GoToCorsiView(corso){
            this.$router.push('/corsi/'+ corso.id)
        }
    }
}
</script>