<template>
  <div class="w-full md:w-9/12 place-self-center">
    <div
      class="flex flex-col md:flex-row bg-orange-100 rounded-lg px-2 py-6 m-2 shadow-2xl items-center">
      <div class="flex w-full md:w-auto mb-4 md:mb-0 px-4 md:px-0 md:flex md:flex-col md:justify-center md:ml-4">
        <img
          :src="corso.idCategory.immagine"
          alt="img"
          class="w-full md:w-auto md:h-44 h-36 rounded-lg"
        />
      </div>
      <div class="flex flex-col items-start mx-4 w-full px-4 md:px-0">
        <div class="flex justify-between items-center w-full">
          <h4 class="text-xl font-light uppercase">{{ corso.nome }}</h4>
          <h4
            class="text-white bg-orange-500 border border-orange-400 p-2 rounded font-light"
          >
            {{ corso.idCategory.nome }}
          </h4>
        </div>
        <p class="text-sm font-light">
          data inizio: <strong>{{ corso.data_inizio }}</strong
          >.
        </p>
        <p class="text-sm font-light">
          docente: <strong>{{ corso.docente }}</strong
          >.
        </p>
        <p class="text-sm font-light">
          dove: <strong>{{ corso.idGym.indirizzo }}</strong
          >.
        </p>
        <p class="text-sm font-light">
          info sul corso: <br />
          {{ corso.descrizione }}.
        </p>
        <button
          type="button"
          @click="GoToCorsiView(corso)"
          class="p-2 leading-none rounded font-medium mt-3 bg-orange-500 text-xs uppercase text-white"
        >
          visualizza
        </button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    corso: Object,
  },
  data() {
    return {};
  },
  methods: {
    GoToCorsiView(corso) {
      this.$router.push("/corsi/" + corso.id);
    },
  },
};
</script>
