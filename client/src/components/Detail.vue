<template>
  <div class='flex mx-10'>
    <div class="flex-col font-light">
      <div class="flex text-3xl font-bold text-left px-5 py-6 m-auto">
        {{ categoria.nome }}
      </div>
      <div class="flex w-full h-44">
        <img :src="categoria.immagine" alt="img" class="w-full" />
      </div>
      <div class="flex-col justify-between px-5 py-6 m-auto text-xl text-left">
        <span class="text-3xl font-bold">{{ corso.nome }}</span> <br />
        {{ corso.descrizione }}
      </div>
      <hr />
      <h1 class="px-5 py-6 text-xl text-red-400">caratteristiche:</h1>
      <div class="flex justify-around px-5 py-6">
        <p>data inizio: {{ corso.data_inizio }}</p>
        <p>data fine: {{ corso.data_fine }}</p>
      </div>
      <h1 class="px-5 py-6 text-xl text-red-400">contatti:</h1>
      <div class="flex text-center justify-around px-5 py-6">
        <p>cellulare: {{ palestra.telefono }}</p>
        <p>email: {{ palestra.email }}</p>
        <p>indirizzo: {{ palestra.indirizzo }}</p>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      corso: {},
      categoria: {},
      palestra: {},
      error: [],
    };
  },
  async mounted() {
    let id = this.$route.params.id;
    await axios
      .get("/api/v1/corsi/" + id + "/")
      .then((response) => {
        this.corso = response.data;
        this.categoria = response.data.idCategory;
        this.palestra = response.data.idGym;
      })
      .catch((error) => {
        if (error.response) {
          for (const property in error.response.data) {
            this.errors.push(`${property}: ${error.response.data[property]}`);
          }
        } else if (error.message) {
          this.errors.push("Something went wrong. Please try again!");
        }
      });
  },
};
</script>
