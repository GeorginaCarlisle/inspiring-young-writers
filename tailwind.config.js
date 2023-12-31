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
        './writing/templates/my_work.html',
        './writing/templates/edit_writing.html',
        './writing/templates/view_writing.html',
        './library/templates/library.html',
        './library/templates/library_title.html',
        './library/templates/read.html',
        './templates/password_reset/password_reset.html',
        './templates/password_reset/password_reset_sent.html',
        './templates/password_reset/password_reset_complete.html',
        './templates/password_reset/password_reset_form.html',
        './templates/parent_info.html',
        './library/templates/give_feedback.html',
        './writing/templates/view_my_feedback.html',
        './library/templates/read_feedback.html',
        './library/templates/edit_feedback.html',
        './account/templates/account_contact.html',
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

