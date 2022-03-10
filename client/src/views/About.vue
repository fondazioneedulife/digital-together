<template>
  <div class="px-0 mx-auto flex flex-col mt-10 mb-10 c">
    <div class="max-w-screen-lg mx-auto p-1">
      <h1 class="font-bold m-8 text-3xl md:text-6xl">
        Ciò che riguarda
        <span class="text-4xl md:text-7xl text-red-400">NOI</span>
      </h1>
      <div class="gap-8 grid-flow-row">
        <div class="col-span-12">
          <div class="grid m-8 font-light text-lg">
            Siamo semplicemente delle persone con un’idea: rendere accessibile
            la formazione alle persone, permettendo a chiunque di cercare i
            corsi o le scuole più adatte a loro. <br />
            Normalmente se si ha bisogno di cercare un corso per sé o un
            parente, oppure semplicemente la scuola migliore per vostro figlio,
            si dovrebbe necessariamente girare su un’infinità di pagine sperando
            di ricordarsi tutti i nomi, oppure ritrovandosi con tantissime
            pagine aperte sul proprio browser, dovendo continuamente scambiare
            tra una e l’altra.
            <br />
            Tuttavia ci siamo noi, con il nostro sito, che ti permette di
            ricercare tutto sulla stessa pagina rendendo così ogni cosa più
            accessibile.
          </div>
        </div>
      </div>
    </div>
    <div class="w-full md:w-1/2">
		<div
			class="leading-loose max-w-xl m-4 p-7 bg-secondary-light dark:bg-secondary-dark rounded-xl shadow-xl text-left"
		>
			<p
				class="font-general-medium text-primary-dark dark:text-primary-light text-2xl mb-8"
			>
				Contact Form
			</p>
			<div  class="font-general-regular space-y-7">
				<div>
					<label
						class="block text-lg text-primary-dark dark:text-primary-light mb-2"
						for="name"
						>Full Name</label
					>
					<input
						class="w-full px-5 py-2 border border-gray-300 dark:border-primary-dark border-opacity-50 text-primary-dark dark:text-secondary-light bg-ternary-light dark:bg-ternary-dark rounded-md shadow-sm text-md"
						id="name"
						name="name"
						type="text"
						required
						placeholder="Your Name"
						aria-label="Name"
					/>
				</div>
				<div>
					<label
						class="block text-lg text-primary-dark dark:text-primary-light mb-2"
						for="email"
						>Email</label
					>
					<input
						class="w-full px-5 py-2 border border-gray-300 dark:border-primary-dark border-opacity-50 text-primary-dark dark:text-secondary-light bg-ternary-light dark:bg-ternary-dark rounded-md shadow-sm text-md"
						id="email"
						name="email"
						type="text"
						required
						placeholder="Your Email"
						aria-label="Email"
					/>
				</div>
				<div>
					<label
						class="block text-lg text-primary-dark dark:text-primary-light mb-2"
						for="subject"
						>Subject</label
					>
					<input
						class="w-full px-5 py-2 border border-gray-300 dark:border-primary-dark border-opacity-50 text-primary-dark dark:text-secondary-light bg-ternary-light dark:bg-ternary-dark rounded-md shadow-sm text-md"
						id="subject"
						name="subject"
						type="text"
						required
						placeholder="Subject"
						aria-label="Subject"
					/>
				</div>

				<div>
					<label
						class="block text-lg text-primary-dark dark:text-primary-light mb-2"
						for="message"
						>Message</label
					>
					<textarea
						class="w-full px-5 py-2 border border-gray-300 dark:border-primary-dark border-opacity-50 text-primary-dark dark:text-secondary-light bg-ternary-light dark:bg-ternary-dark rounded-md shadow-sm text-md"
						id="message"
						name="message"
						cols="14"
						rows="6"
						aria-label="Message"
						required
					></textarea>
				</div>
				<!-- <div class="bg-green-100 border-t-4 border-green-500 rounded-b text-green-900 px-4 py-3 shadow-md" role="alert" v-if="confirmed">
						<div class="flex">
							<div class="py-1"><svg class="fill-current h-6 w-6 text-green-500 mr-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 17.07zm12.73-1.41A8 8 0 1 0 4.34 4.34a8 8 0 0 0 11.32 11.32zM9 11V9h2v6H9v-4zm0-6h2v2H9V5z"/></svg></div>
							<div>
							<p class="text-green-600 font-bold">{{confirmed}}</p>
							</div>
						</div>
					</div>
				<div class="bg-red-100 border-t-4 border-red-500 rounded-b text-red-900 px-4 py-3 shadow-md" role="alert" v-if="alert">
						<div class="flex">
							<div class="py-1"><svg class="fill-current h-6 w-6 text-red-500 mr-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M2.93 17.07A10 10 0 1 1 17.07 2.93 10 10 0 0 1 2.93 17.07zm12.73-1.41A8 8 0 1 0 4.34 4.34a8 8 0 0 0 11.32 11.32zM9 11V9h2v6H9v-4zm0-6h2v2H9V5z"/></svg></div>
							<div>
							<p class="text-red-600 font-bold">{{alert}}</p>
							</div>
						</div>
				</div> -->
				<div>
					<button
						title="Send Message"
						class="px-4 py-2.5 text-white tracking-wider bg-indigo-500 hover:bg-indigo-600 focus:ring-1 focus:ring-indigo-900 rounded-lg duration-500"
						type="submit"
						aria-label="Send Message"
						ref="form"	
					>
          Send message
          </button>
				</div>
			</div>
		</div>
	</div>
  </div>
</template>
