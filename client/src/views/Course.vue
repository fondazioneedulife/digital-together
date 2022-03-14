<template>
  <div class="flex-col">
    <div class="flex flex-row items-center justify-center px-6">
      <div class="relative inline-block text-left shadow-xl" @click="toggle()">
        <button
          type="button"
          class="inline-flex h-16 items-center w-full rounded-md border border-orange-300 shadow-sm px-4 py-2 bg-orange-500 text-lg font-light text-white hover:bg-orange-400 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-orange-100 focus:ring-orange-500"
          id="menu-button"
          aria-expanded="true"
          aria-haspopup="true"
        >
          {{ listed }}
          <!-- Heroicon name: solid/chevron-down -->
          <svg
            class="-mr-1 ml-2 h-5 w-5"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
          >
            <path
              fill-rule="evenodd"
              d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
              clip-rule="evenodd"
            />
          </svg>
        </button>
        <!-- '''''' -->
        <div
          v-if="isOpen"
          class="origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none"
          role="menu"
          aria-orientation="vertical"
          aria-labelledby="menu-button"
          tabindex="-1"
        >
          <div role="none" @click="orderList()">
            <!-- Active: "bg-gray-100 text-gray-900", Not Active: "text-gray-700" -->

            <p
              v-for="categoria in categorie"
              :key="categoria.id"
              @click="selected(categoria)"
              class="text-gray-700 block px-4 py-2 text-sm hover:bg-gray-200 cursor-pointer"
              role="menuitem"
              tabindex="-1"
              id="menu-item-0"
            >
              {{ categoria.nome }}
            </p>
          </div>
        </div>
      </div>
      <div class="m-3 w-2/4 shadow-xl rounded-lg border border-orange-300">
        <div
          class="px-2 flex items-center border-1 bg-white shadow-sm rounded-full"
        >
          <input
            class="rounded-l-sm w-full h-16 py-2 px-6 text-gray-700 rounded-lg leading-tight focus:outline-none"
            id="search"
            type="text"
            placeholder="Search"
            v-model="query"
          />
          <div class="p-2">
            <button
              class="hidden md:bg-orange-500 md:text-white md:rounded-full md:p-2 md:hover:bg-red-400 md:focus:outline-none md:w-12 md:h-12 md:flex md:items-center md:justify-center"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>
      <div
        class="relative inline-block text-left shadow-xl"
        @click="openFilter()"
      >
        <button
          type="button"
          class="inline-flex h-16 items-center w-full rounded-md border border-orange-300 shadow-sm px-4 py-2 bg-orange-500 text-lg font-light text-white hover:bg-orange-400 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-orange-100 focus:ring-orange-500"
          id="menu-button"
          aria-expanded="true"
          aria-haspopup="true"
        >
          Filtri
          <img
            class="hidden md:mr-1 md:ml-2 md:h-5 md:w-5"
            src="@/assets/imbutofilter.svg"
          />
        </button>
        <div
          :class="filterOpen ? 'block' : 'hidden'"
          class="origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none"
          role="menu"
          aria-orientation="vertical"
          aria-labelledby="menu-button"
          tabindex="-1"
        >
          <div class="flex flex-col p-2 border border-orange-300">
            <!--collegare checkbox alla durata del corso-->
            <p class="flex flex-row">Durata corso</p>
            <span
              class="flex flex-row items-center"
              v-for="(corso, index) in corsi"
              :key="index"
              ><input
                @click="setHour(corso.durata)"
                type="checkbox"
                class="mr-1"
              />
              <p>{{ corso.durata }} ore</p></span
            >
          </div>
        </div>
      </div>
    </div>
    <div v-if="!isLoading"></div>
    <div v-else class="flex items-center justify-center p-10">
      <span
        class="text-orange-400 font-bold text-center text-xl flex flex-col items-center"
      >
        <Spinner class=''></Spinner>
      </span>
    </div>
    <div
      class="flex items-center justify-center px-3 py-2"
      v-if="errors.length"
    >
      <p
        class="text-orange-400 font-light"
        v-for="error in errors"
        v-bind:key="error"
      >
        *attenzione: {{ error }}*
      </p>
    </div>
    <div class="flex items-center justify-center">
      <div
        class="flex flex-col w-screen h-auto my-4 p-4"
        v-if="filteredCorso.length"
      >
        <!-- v-for="corso in corsi"
          :key="corso.id" -->
        <CardCours
          v-for="(corso, index) in filteredCorso"
          :key="index"
          v-bind="corso"
          :corso="corso"
        />
      </div>
      <div
        v-else
        class="flex justify-center w-screen h-auto my-4 p-4 font-bold p-5 text-gray-400"
      >
        Nessuna corso corrisponde alla tua ricerca :(
      </div>
      <!-- <div v-else>
        <p>content not found</p>
      </div> -->
    </div>
  </div>
</template>
<script>
import axios from "axios";
import CardCours from "@/components/CardCours";
import Spinner from "@/components/Spinner.vue";
export default {
  components: {
    CardCours,
    Spinner,
  },
  data() {
    return {
      categorie: [],
      query: "",
      errors: [],
      isOpen: false,
      filterOpen: false,
      listed: "categoria",
      corsi: [],
      isLoading: true,
      // duration:['40 ore','100 ore', '400 ore', 'annuale', 'biennale'],
      time: "",
    };
  },
  async mounted() {
    this.isLoading = true;
    await axios
      .get("/api/v1/categorie/")
      .then((response) => {
        this.categorie = response.data;
        this.isLoading = false;
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
    this.isLoading = true;
    await axios
      .get("/api/v1/corsi/")
      .then((response) => {
        this.corsi = response.data;
        this.isLoading = false;
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
  computed: {
    filteredCorso() {
      return this.corsi.filter((corsi) => {
        if (this.query == "") {
          this.listed = "categoria";
          return true;
        }
        if (corsi.nome.toLowerCase().startsWith(this.query.toLowerCase())) {
          return true;
        }
        if (corsi.idCategory.nome.toLowerCase() == this.listed.toLowerCase()) {
          return true;
        }
        if (corsi.durata == this.time) {
          return true;
        }
        return false;
      });
    },
  },
  methods: {
    orderList() {
      this.query = this.listed;
    },
    toggle() {
      if (this.isOpen == false) {
        this.isOpen = true;
      } else if (this.isOpen == true) {
        this.isOpen = false;
      }
    },
    openFilter: function () {
      this.filterOpen = !this.filterOpen;
    },
    selected(categoria) {
      this.listed = categoria.nome;
      return this.listed;
    },
    setHour(value) {
      this.time = value;
      this.query = this.time;
      console.log(this.corsi, this.time);
      // const result = this.corsi.sort((a, b) => a.durata - b.durata)
      // console.log(result)
    },
  },
  // computed:{
  //     filtered() {
  //         return this.listed.filter(corso => {
  //             if (this.listed == "cerca") {
  //             return true;
  //             }
  //             if (this.listed.toLowerCase() == corso.idCategory.nome.toLowerCase()){
  //             return true;
  //             }
  //             return false;
  //         });
  //     }
  // }
};
</script>
