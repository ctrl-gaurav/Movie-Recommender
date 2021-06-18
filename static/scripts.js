const menuToggle = document.querySelector('.toggle')
const showcase = document.querySelector('.showcase')
const social = document.querySelector('.social')

menuToggle. addEventListener('click', () => {
    menuToggle.classList.toggle('active')
    showcase.classList.toggle('active')
    social.classList.toggle('active')
})