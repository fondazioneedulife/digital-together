<template>
    <div class="flex bg-white border justify-between items-center px-10 py-0">
        <div class="items-center rounded p-5 ">
            <img class="w-38 h-20" :src="logo"/>
        </div>
        <div
                v-for="link in navLinks"
                :key="link.code"

                @click="goToLink(link)"
                class="cursor-pointer items-center text-center content-around text-xl font-light"
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