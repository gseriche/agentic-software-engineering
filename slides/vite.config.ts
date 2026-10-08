import { defineConfig } from 'vite'

// Work around malformed CSS emitted by the current Slidev/UnoCSS combination
// when Lightning CSS minifies the production bundle.
export default defineConfig({
  build: {
    cssMinify: 'esbuild',
  },
})
