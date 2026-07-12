/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        paper: "#FBFAF6",
        ink: "#1A1D1B",
        muted: "#6B6F6A",
        line: "#E3E1D6",
        stamp: {
          DEFAULT: "#0B6E4F",
          dark: "#08543C",
          light: "#E8F3EE",
        },
        seal: {
          DEFAULT: "#B0893D",
          light: "#F6EEDD",
        },
        risk: {
          DEFAULT: "#B3462C",
          light: "#FBEBE6",
        },
      },
      fontFamily: {
        display: ["var(--font-display)", "serif"],
        body: ["var(--font-body)", "sans-serif"],
        mono: ["var(--font-mono)", "monospace"],
      },
    },
  },
  plugins: [],
};
