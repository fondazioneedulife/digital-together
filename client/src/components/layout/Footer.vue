<template>
    <footer class="bg-white p-5 grid grid-cols-1 md:grid-cols-12">
    <div class="flex md:col-span-1"></div>
      <div class="flex md:col-span-2 justify-center md:items-left text-center md:text-left">
        <span class="text-gray-400">
          <span><router-link to="/"><img class="w-24 h-24" src='@/assets/Logo.svg'></router-link></span>
          <div class='flex flex-row'>
          <span class='w-6 h-6 mx-2'><a  class='w-6 h-6' href='https://www.instagram.com/37100lab.comunediverona/' target='_blank'><img src="@/assets/Instagram.svg" class="bg-white rounded-lg w-auto h-6"/></a></span>
          <span class='w-6 h-6 mx-2'><a  class='w-6 h-6' href='https://www.facebook.com/37100Lab.ComuneVerona/' target='_blank'><img src="@/assets/Facebook.svg" class="bg-white rounded-lg w-auto h-6"/></a></span>
          <span class='w-6 h-6 mx-2 '><a  class='w-6 h-6' href='https://www.linkedin.com/company/37100lab-comune-di-verona/' target='_blank'><img src="@/assets/Linkedin.svg" class="bg-white rounded-lg w-auto h-6"/></a></span>
          </div>
        </span>
      </div>
      <div class="flex md:col-span-2 justify-center md:items-start text-center md:text-left">
        <span class="md:w-0.5 md:h-full md:bg-orange-500 md:mr-5" />
        <div class="flex flex-col pt-5 text-orange-400">
          <!--<p class="text-orange-200 mb-3">Pagine</p>-->
          <span> <router-link to="/corsi">Corsi</router-link> </span>
          <span> <router-link to="/about">About Us</router-link> </span>
          <span> <router-link to="/contatti">Contatti</router-link> </span>
          <span> <router-link to="/faq">FAQ</router-link> </span>
        </div>
      </div>
      <div class="flex md:col-span-2 justify-center text-center md:text-left">
        <span class="md:w-0.5 md:h-full md:bg-orange-500 md:mr-5" />
        <div class="flex flex-col pt-5 text-orange-400">
        <!--<p class="text-orange-200 mb-3">Contatti</p>-->
          <span>351 524 3518</span>
          <span>37100lab@comune.verona.it</span>
          <span>vie Marchi, 12, 37135 Verona VR</span>
        
        </div>
      </div>
      
      <div class="mt-5 md:col-span-12 text-center text-orange-400 pt-2">
        Created by  Digital Together ®
      </div>
  </footer>
</template>