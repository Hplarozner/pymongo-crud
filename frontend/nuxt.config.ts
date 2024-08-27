// nuxt.config.ts
import vuetify from 'vite-plugin-vuetify'

// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
  css: [
    'vuetify/lib/styles/main.sass',
   ],

  app: {
 pageTransition: {
   name: "page"
 },

 layoutTransition: {
   name: "rotate",
 },

 head: {
   title: "Pymongo",

   meta: [
     { name: "viewport", content: "width=device-width, initial-scale=1.25" },
   ],
 },
},

  build: {
    transpile: ['vuetify'],
  },

  vite: {
    define: {
      'process.env.DEBUG': false,
    },
     plugins: [
      vuetify()
    ]
  },

  compatibilityDate: "2024-08-27",
})