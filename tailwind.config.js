module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        primary: '#E5E5E5',
        secondary: '#E9E9EB',
        tertiary: {
          100: '#e6e6f2',
          200: '#4A4AFF',
          300: '#CDFFCD',
          400: '#6DD11E',
          500: '#E9E9EB',
          600: '#626670',
          700: '#12161E',
          800: '#626670',
          900: '#2164E8',
        },
        hab: {
          100: '#CDFFCD',
          200: '#6D5BD0',
          300: '#E54F6D',
          400: '#BCBEC2',
        }
      },
      gridTemplateColumns: {
        '24': 'repeat(24, minmax(0, 1fr))',
      },
      inset: (theme, { negative }) => ({
        auto: 'auto',
        ...theme('spacing'),
        ...negative(theme('spacing')),
        '1/2': '50%',
        '1/3': '33.333333%',
        '2/3': '66.666667%',
        '1/4': '25%',
        '2/4': '50%',
        '3/4': '75%',
        '1/10': '10%',
        '15/100': '15%',
        '2/10': '20%',
        '3/10':'30%',
        '1/20': '5%',
        '3/5': '60%',
        full: '100%',
        '-1/2': '-50%',
        '-1/3': '-33.333333%',
        '-2/3': '-66.666667%',
        '-1/4': '-25%',
        '-2/4': '-50%',
        '-3/4': '-75%',
        '-full': '-100%',
      }),
      height: (theme) => ({
        auto: 'auto',
        ...theme('spacing'),
        '1/2': '50%',
        '1/3': '33.333333%',
        '2/3': '66.666667%',
        '1/4': '25%',
        '2/4': '50%',
        '3/4': '75%',
        '1/5': '20%',
        '2/5': '40%',
        '3/5': '60%',
        '4/5': '80%',
        '1/6': '16.666667%',
        '2/6': '33.333333%',
        '3/6': '50%',
        '4/6': '66.666667%',
        '5/6': '83.333333%',
        '1/10': '10%',
        '1/60': '1.6666667%',
        full: '100%',
        screen: '100vh',
      }),
      width: (theme) => ({
        auto: 'auto',
        ...theme('spacing'),
        '1/2': '50%',
        '1/3': '33.333333%',
        '2/3': '66.666667%',
        '1/4': '25%',
        '2/4': '50%',
        '3/4': '75%',
        '1/5': '20%',
        '2/5': '40%',
        '3/5': '60%',
        '4/5': '80%',
        '1/6': '16.666667%',
        '2/6': '33.333333%',
        '3/6': '50%',
        '4/6': '66.666667%',
        '5/6': '83.333333%',
        '1/24': '4.1666667%',
        '1/12': '8.333333%',
        '2/12': '16.666667%',
        '3/12': '25%',
        '4/12': '33.333333%',
        '5/12': '41.666667%',
        '6/12': '50%',
        '7/12': '58.333333%',
        '8/12': '66.666667%',
        '9/12': '75%',
        '10/12': '83.333333%',
        '11/12': '91.666667%',
        '5/24': '20.833333%',
        '90/100': '90%',
        '95/100': '95%',
        '3/24': '12.5%',
        full: '100%',
        screen: '100vw',
        min: 'min-content',
        max: 'max-content',
      }),
      height: (theme) => ({
        auto: 'auto',
        ...theme('spacing'),
        '1/2': '50%',
        '1/3': '33.333333%',
        '2/3': '66.666667%',
        '1/4': '25%',
        '2/4': '50%',
        '3/4': '75%',
        '1/5': '20%',
        '2/5': '40%',
        '3/5': '60%',
        '4/5': '80%',
        '1/6': '16.666667%',
        '2/6': '33.333333%',
        '3/6': '50%',
        '4/6': '66.666667%',
        '5/6': '83.333333%',
        '11/12': '91.666667%',
        full: '100%',
        screen: '100vh',
      }),
      borderOpacity: (theme) => theme('opacity'),
      borderRadius: {
        none: '0px',
        sm: '0.125rem',
        DEFAULT: '0.25rem',
        md: '0.375rem',
        lg: '0.5rem',
        mg: '0.625rem',
        xl: '0.75rem',
        '2xl': '1rem',
        '3xl': '1.5rem',
        full: '9999px',
      },
      fontFamily: {
        body: ['Lato',],
        hab: ['Work Sans',],
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
