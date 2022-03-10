<template>
    <div>
        <section class="py-8 2xl:py-12 bg-white">
        <div class="container px-4 mx-auto">
            <div class="mb-8 text-center">
            <span class="text-lg font-bold text-red-500">Hey! Have any questions?</span>
            <h2 class="mb-12 mt-6 text-7xl font-bold font-heading">FAQ&apos;s</h2>
            </div>
            <div class="max-w-4xl mx-auto">
            <ul>
                <li class="mb-4 px-4 lg:px-12 py-8 bg-orange-50 rounded-2xl shadow-xl" v-for="(question, index) in questions" :key="index">
                <button class="flex w-full text-left" @click="OpenDrop(question)">
                    <div class="w-auto mr-8">
                    <span class="flex items-center justify-center w-12 h-12 text-lg font-bold bg-orange-200 rounded-full">{{index+1}}</span>
                    </div>
                    <div class="w-full mt-3">
                    <div class="flex items-center justify-between">
                        <h3 class="text-xl font-bold">{{question.ask}}</h3>
                        <span class="ml-4">
                        <svg v-if="question.isOpen == true" class="w-4 h-4 ring-orange-500" width="18" height="10" viewbox="0 0 18 10" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M1.18267 9.00018C0.910673 9.26818 0.473672 9.26818 0.203672 9.00018C-0.0663284 8.73218 -0.0673279 8.29918 0.203672 8.03118L8.11167 0.201183C8.38167 -0.0668173 8.81867 -0.0668173 9.09067 0.201183L16.9987 8.03118C17.2687 8.29918 17.2687 8.73218 16.9987 9.00018C16.7277 9.26818 16.2897 9.26818 16.0197 9.00018L8.60067 1.85918L1.18267 9.00018Z" fill="#1F40FF"></path>
                        </svg>
                        <svg v-else class="w-4 h-4" width="18" height="10" viewbox="0 0 18 10" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M16.0185 0.999999C16.2905 0.732 16.7275 0.732 16.9975 0.999999C17.2675 1.268 17.2685 1.701 16.9975 1.969L9.0895 9.799C8.8195 10.067 8.3825 10.067 8.1105 9.799L0.2025 1.969C-0.0675004 1.701 -0.0675004 1.268 0.2025 1C0.4735 0.732 0.9115 0.732 1.1815 1L8.6005 8.141L16.0185 0.999999Z" fill="#1F40FF"></path>
                        </svg>
                        </span>
                    </div>
                    <div v-if='question.isOpen' class="mt-6 ">
                        <p class="font-light mb-5 text-xl">{{question.answare}}</p>
                    </div>
                    </div>
                </button>
                </li>
            </ul>
            </div>
        </div>
        </section>
    </div>
</template>
<script>
//import BotBanner from '@/components/BotBanner.vue'
export default {
    name: 'Faq',
    components:{ //BotBanner 
    },
    data(){
        return{
            questions: [
                {
                    ask: "quali corsi ci sono?",
                    answare: "i corsi presenti sono molti, vai nella sezione corsi e utilizza i filtri per trovare il corso giusto per te!",
                    isOpen: false
                },
                {
                    ask: "quali tipo di corsi sono presenti?",
                    answare: "quando ti rivolgi a questa piattaforma puoi trovare qualsiasi tipo di corso inerente alle competenze digitali. ;)",
                    isOpen: false
                },
                {
                    ask: "posso visualizzare la palestra digitale su una mappa?",
                    answare: "si, in questo modo puoi vedere esattamente dove si svolge il corso e raggiungerlo rapidamente.",
                    isOpen: false
                }
            ]
        }
    },
    methods:{
        OpenDrop(question){
            if (question.isOpen == false){  
                question.isOpen = true;
            } else if(question.isOpen == true){
                question.isOpen = false;
            }
        }
    }
}
</script>