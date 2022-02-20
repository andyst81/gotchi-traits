module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    theme: {
      extend: {
        lineHeight: {
          3: '1.2rem',
          4: '1.6rem',
          5: '2.0rem',
          6: '2.4rem',
          7: '2.8rem',
          8: '3.2rem',
          9: '3.6rem',
          10: '4.0rem',
        },
        fontSize: {
          xs: ['1.2rem', { lineHeight: '1.6rem' }],
          sm: ['1.4rem', { lineHeight: '2.0rem' }],
          base: ['1.6rem', { lineHeight: '2.4rem' }],
          lg: ['1.8rem', { lineHeight: '2.8rem' }],
          xl: ['2.0rem', { lineHeight: '2.8rem' }],
          '2xl': ['2.4rem', { lineHeight: '3.2rem' }],
          '3xl': ['3.0rem', { lineHeight: '3.6rem' }],
          '4xl': ['3.6rem', { lineHeight: '4.0rem' }],
          '5xl': ['4.8rem', { lineHeight: '1' }]
        },
      },
    },
  },
  plugins: [],
}