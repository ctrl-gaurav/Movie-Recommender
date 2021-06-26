const menuToggle = document.querySelector('.toggle')
const showcase = document.querySelector('.showcase')
const social = document.querySelector('.social')
const moviesToggle = document.querySelector('.movies')

const searchToggle = document.querySelector('.container')
const buttonToggle = document.querySelector('.search-button')

menuToggle. addEventListener('click', () => {
    menuToggle.classList.toggle('active')
    showcase.classList.toggle('active')
    social.classList.toggle('active')
    searchToggle.classList.toggle('active')
    moviesToggle.classList.toggle('active')
})

buttonToggle. addEventListener('click', () =>{
    searchToggle.classList.toggle('move-up')
})
