<template>
    <div class="flex bg-white border justify-between items-center px-10 py-0">
        <div class="items-center rounded p-5 ">
            <img class="w-38 h-20" :src="logo"/>
        </div>
        <div
                v-for="link in navLinks"
                :key="link.code"
                :class="{
                    'border-b border-red-400': link.code == currentRouteName,
                    '': link.code !== currentRouteName
                }"
                @click="goToLink(link)"
                class="cursor-pointer font-light items-center text-center content-around text-xl mr-12"
                >
                {{ link.label }}
        </div>
    </div>
</template>
<script>
import image from '@/assets/Logo.svg'
export default {
    data() {
        return{
            navLinks: [
                {
                label: "Home",
                code: "home"
                },
                {
                label: "Corsi",
                code: "course_list"
                },
                {
                label: "About us",
                code: "about"
                },
                {
                label: "Contatti",
                code: "contact"
                },
                {
                label: "FAQ",
                code: "faq"
                }
            ],
            logo: image,
        }
    },
    computed: {
        currentRouteName() {
            if (!this.$route.matched[0]){
                return 
            }
            return this.$route.matched[0].name;
        }
    },
    methods: {
        goToLink(link) {
        this.$router.push({
            name: link.code
        });
        }
    }
}
</script>