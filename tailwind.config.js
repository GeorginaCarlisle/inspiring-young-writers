/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/base.html', 
    './templates/footer.html', 
    './templates/header.html', 
    './home/templates/index.html'
  ],
  theme: {
    extend: {},
    fontFamily: {
      title: ['Boogaloo', 'sans-serif'],
      body: ['Ubuntu', 'sans-serif'],
      kids: ['Ubuntu Mono', 'monospace'],
    }
  },
  plugins: [],
}

