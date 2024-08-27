
// plugins/vuetify.js
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as labs from "vuetify/labs/components";
import * as directives from 'vuetify/directives'
import 'vuetify/dist/vuetify.min.css';
import 'vuetify/styles'
export default defineNuxtPlugin(nuxtApp => {
  const vuetify = createVuetify({
    ssr: true,
    components: {
      ...components,
      ...labs
    },
     directives,

    theme: {
        defaultTheme: 'dark',

        themes: {
          light: {
            colors: {
              primary: "#0D47A1"
            }
          },
          dark: {
            dark: true,
            colors: {
              primary: "#1565C0"
            }
          }
        }
      }
  })

  nuxtApp.vueApp.use(vuetify)
})