<template>
    <div class="mb-24">
        <div class="flex flex-col mt-10 a md:grid md:grid-cols-8 md:h-96 md:mt-20 items-center">
            <div class="justify-items-center w-96 md:block md:col-start-2 md:col-end-5 p-1 md:right"><img src='@/assets/Landing_1.svg'></div>
            <div class="justify-items-center text-center md:col-start-5 rounded-full md:col-end-8 p-5 md:text-left">
                <p class='font-medium text-4xl mb-20'>INSERIRE SLOGAN<br> FIGO E<br> ACCATTIVANTE</p>
                <button class='btn text-white p-2 rounded'>Scopri di più</button>
            </div>
        </div>

        <div class="flex flex-col b mt-10 md:grid md:grid-cols-8 md:h-96 md:mt-20 items-center">
            <div class="justify-items-center text-center md:col-start-2 md:col-end-5 p-5 md:text-right">
                <p class='font-medium text-3xl mb-10'>OpenData</p>
                <p class='mb-20'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Faucibus sagittis tortor facilisis pretium egestas. Venenatis ut et vestibulum mi eget aliquam nibh tortor sit. Tellus cursus sed vel habitant morbi neque adipiscing urna, ultrices. Augue fames id.</p>
                <button class='btn text-white p-2 rounded'>Dati originali</button>
            </div>
            <div class="justify-items-center w-96 md:col-start-5 md:col-end-8 p-1"><img src='@/assets/Landing_2.svg'></div>
        </div>

        <div class="flex flex-col mt-10 c md:grid md:grid-cols-8 md:h-96 md:mt-20 md:mb-20 items-center">
            <div class="justify-items-center w-96 md:block md:col-start-2 md:col-end-5 p-1"><img src='@/assets/Landing_3.svg'></div>
            <div class="justify-items-center text-center md:col-start-5 md:col-end-8 p-5 md:text-left">
                <p class='font-medium text-3xl mb-10'>Mettiti alla prova</p>
                <p class='mb-20'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Faucibus sagittis tortor facilisis pretium egestas. Venenatis ut et vestibulum mi eget aliquam nibh tortor sit. Tellus cursus sed vel habitant morbi neque adipiscing urna, ultrices. Augue fames id.</p>
                <span class='flex flex-row'>
                    <button class='btnwhite p-2 rounded mr-5'>Originale</button>
                    <button class='btn text-white p-2 rounded'>Vai al test</button>
                </span>
            </div>
        </div>

        <div class="flex flex-col mt-10 b md:grid md:grid-cols-8 md:h-96 md:mt-20 items-center">
            <div class="justify-items-center text-center md:col-start-2 md:col-end-5 p-5 md:text-right">
                <p class='font-medium text-3xl mb-10'>Scopri i corsi</p>
                <p class='mb-20'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Faucibus sagittis tortor facilisis pretium egestas. Venenatis ut et vestibulum mi eget aliquam nibh tortor sit. Tellus cursus sed vel habitant morbi neque adipiscing urna, ultrices. Augue fames id.</p>
                <button class='btn text-white p-2 rounded'>Scopri di più</button>
            </div>
            <div class="justify-items-center w-72 md:col-start-5 md:col-end-8 md:mapimg p-1"><img src='@/assets/Landing_4.svg'></div>
        </div>

    </div>
</template>
<script>
export default {
    data() {
        return{
            
        }
    },
}
</script>
<style>
body::-webkit-scrollbar {
  display: none;
}

.top{
    border-bottom: 3px solid black;
}

.logo{
    width: 4rem;
    height: 4rem;
}

.btn{
    background-color: #FF7901;
}

.btnwhite{
    background-color: white;
    border: 0.10rem solid #FF7901;
    color: black;
}
@media screen and (min-width: 768px) {
    .a{
        background-image:url('../assets/Ellipse8.svg');
        background-position: center; 
        background-repeat: no-repeat;
        background-size: 380px 380px;
    }

    .b{
        background-image:url('../assets/sinistra.svg');
        background-position: left; 
        background-repeat: no-repeat;
        background-size: 380px 380px;
    }

    .c{
        background-image:url('../assets/destra.svg');
        background-position: right; 
        background-repeat: no-repeat;
        background-size: 380px 380px;
    }
}
.a .b .c{
    display: none
}

.mapimg{
    width: 400px;
}
</style>