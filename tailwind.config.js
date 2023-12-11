/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/base.html',
        './templates/footer.html',
        './templates/header.html',
        './home/templates/index.html',
        './home/templates/contact.html',
        './templates/404.html',
        './templates/500.html',
        './templates/hero.html',
        './users/templates/signup.html',
        './templates/account_header.html',
        './account/templates/account_home.html',
        './users/templates/login.html',
        './users/templates/logout.html',
        './writing/templates/create_writing.html',
    ],
    theme: {
        extend: {
            colors: {
                'horange': '#F6BD58',
            },
        },
        fontFamily: {
            title: ['Boogaloo', 'sans-serif'],
            body: ['Ubuntu', 'sans-serif'],
            kids: ['Ubuntu Mono', 'monospace'],
        },
    },
    plugins: [],
};

