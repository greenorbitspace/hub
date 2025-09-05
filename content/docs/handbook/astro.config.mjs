import { defineConfig } from "astro/config";
import tailwind from "@astrojs/tailwind";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://handbook.greenorbit.space", // base URL of the subsite
  integrations: [tailwind(), sitemap()],
  build: {
    outDir: "dist", // can change per subsite
  },
});