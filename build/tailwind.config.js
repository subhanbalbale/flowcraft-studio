module.exports = {
  content: ["./*.html"],
  theme: {
    extend: {
      // Names are deliberately outside Tailwind's default palette so the pages
      // still on the old theme keep their blue-*/pink-* utilities.
      colors: {
        ground: "#0350c4", // page ground
        navy: "#112967",   // ink on flame, deep panels
        azure: "#6091d8",  // texture only, never text
        mint: "#ddf5ec",   // primary text on ground, card surface
        aqua: "#c7e5ea",   // secondary text on ground
        flame: "#fa7d13",  // CTA fill only
        paper: "#f8f3f3",  // inset panels
        ink: "#1c1c1c",
      },
      fontFamily: {
        display: ["Archivo", "Archivo Fallback", "Arial", "sans-serif"],
        serif: ["Instrument Serif", "Georgia", "Times New Roman", "serif"],
      },
    },
  },
  plugins: [],
};
