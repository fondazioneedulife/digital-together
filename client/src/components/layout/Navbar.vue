<template>
<div class="grid grid-cols-7 border-b border-orange-400 md:h-24 h-auto items-center justify-items-center justify-content-center">
    <div class="col-start-1 col-end-4 ml-5 md:col-start-2 md:col-end-3"><a href='/'>
        <img class="block md:w-32 md:h-24 w-auto h-28" :src="logo"/></a>
    </div>
    <div class="hidden md:col-start-3 md:col-end-7 md:contents whitespace-nowrap">
        <div
            v-for="link in navLinks"
            :key="link.code"
            :class="{
                    'border-b border-orange-400': link.code == currentRouteName,
                    '': link.code !== currentRouteNam
            }"
            @click="goToLink(link)"
            class="cursor-pointer text-xl font-light "
            >
            {{ link.label }}
        </div>
    </div>

    <div class='block md:hidden col-start-7 col-end-7'>
        <button @click="open"><img class='w-10 h-10 mr-6' :src="menu"/></button>
    </div>
    <div :class="show ? 'block': 'hidden' " class="bg-orange-200 md:hidden w-full col-start-1 col-end-9 flex flex-col items-left p-1">
        <div class='p-5 bg-white w-auto h-auto rounded-lg m-2 cursor-pointer'
            v-for="link in navLinks"
            :key="link.code"
            @click="goToLink(link)">
            {{ link.label }}
        </div>
    </div>
    
</div>
</template>
<script>
import image from '@/assets/Logo.svg';
import menu from '@/assets/Menuicon.svg';
export default {
    data() {
        return{
            show : false,
            navLinks: [
                // {
                // label: "Home",
                // code: "home"
                // },
                {
                label: "Corsi",
                code: "course_list"
                },
                {
                label: "About us",
                code: "about"
                },
                {
                label: "Opendata",
                code: "opendata"
                },
                {
                label: "FAQ",
                code: "faq"
                }
            ],
            logo: image,
            menu: menu,
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
        this.show = !this.show
        },
        open: function() {
            this.show = !this.show
        }
    }
}
</script>