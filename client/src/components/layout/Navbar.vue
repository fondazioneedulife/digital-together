<template>
    <div class="flex px-6 py-8  bg-white m-auto border-b border-black">
        <div class="">
            <img class="w-38 h-20" :src="logo"/>
        </div>
        <div class="flex justify-center items-center mx-auto">
            <div
                v-for="link in navLinks"
                :key="link.code"
                @click="goToLink(link)"
                class="cursor-pointer items-center content-around text-xl font-light text-center px-3 py-1"
                >
                {{ link.label }}
            </div>
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
                code: "Home"
                },
                {
                label: "Corsi",
                code: "Courses"
                },
                {
                label: "About us",
                code: "About"
                },
                {
                label: "Contatti",
                code: "Contact"
                },
                {
                label: "FAQ",
                code: "Faq"
                }
            ],
            logo: image,
        }
    },
    computed: {
        currentRouteName() {
            return this.$route.matched[0].path;
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