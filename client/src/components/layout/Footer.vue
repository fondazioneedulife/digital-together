<template>
    <footer class="bg-gray-800 p-5 grid grid-cols-1  md:grid-cols-12">
      <div class="md:col-span-2 pb-2 md:mb-0 m-8">
        <p class="text-gray-200">Contatti</p>
        <ul class="pt-5 text-gray-400">
          <li>351 524 3518</li>
          <li>37100lab@comune.verona.it</li>
          <li>vie Marchi, 12, 37135 Verona VR</li>
        </ul>
      </div>
      <div class="md:col-span-2 pb-2 m-8 ml-32 md:mb-0">
          <p class="text-gray-200">Pagine</p>
        <ul class="pt-5 text-gray-400">
          <li> <router-link to="/">Home</router-link> </li>
          <li> <router-link to="/corsi">Corsi</router-link> </li>
          <li> <router-link to="/about">About Us</router-link> </li>
          <li> <router-link to="/faq">FAQ</router-link> </li>
        </ul>
      </div>
      <div class="md:col-span-4 pb-2 m-8 ml-32 md:mb-0">
        <ul class="pt-5 text-gray-400">
          <li><img class="w-24 h-24" src='@/assets/Logo.svg'></li>
          <li><img src="https://img.icons8.com/ios/50/000000/instagram-new--v3.png" class="bg-white rounded-lg w-6 h-6"/></li>
        </ul>
      </div>
      <div class="mt-5 md:col-span-12 text-center text-gray-400 pt-2">
        Created by  Digital Together ®
      </div>
  </footer>
</template>