<template>
    <div>
        <div class="grid grid-cols-8 h-96 mt-20">
            <div class="col-start-2 col-end-5 p-1">02</div>
            <div class="box col-start-5 rounded-full col-end-8 p-1">02</div>
        </div>

        <div class="grid grid-cols-8 h-96 mt-20">
            <div class="box col-start-2 col-end-5 p-1">02</div>
            <div class="col-start-5 col-end-8 p-1">02</div>
        </div>

        <div class="grid grid-cols-8 h-96 mt-20 mb-20">
            <div class="col-start-2 col-end-5 p-1">02</div>
            <div class="box col-start-5 col-end-8 p-1">02</div>
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

.box{
    background-color: #eebd7d;
    border-radius: 1rem;
}

.top{
    border-bottom: 3px solid black;
}

.logo{
    width: 4rem;
    height: 4rem;
}
</style>