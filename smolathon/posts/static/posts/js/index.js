gsap.registerPlugin(ScrollTrigger, ScrollSmoother)

//анимация поиска
const burgerBtn = document.getElementById('burgerBtn')
const burgerMenu = document.querySelector('.burger-menu')
const search = document.getElementById('search')
const searchInput = document.querySelector('.search__top-block')
const dark = document.querySelector('.header__dark')

search.addEventListener('click', () => {
    dark.classList.toggle('none');
    dark.addEventListener('click', (e) => {
        if (e.target !== searchInput){
            dark.classList.add('none')
        } 
    })
}) 

burgerBtn.addEventListener('click', () => {
    burgerMenu.classList.toggle('none');
    burgerBtn.classList.toggle('grey-burger');
    burgerMenu.classList.add('animated-burg');
}) 

//анимация заведений
const events = document.querySelector('.events');
const eventsMin  = document.querySelector('.events-min')

events.addEventListener('click', () => {
    eventsMin.classList.toggle('none');

    let styles = window.getComputedStyle(events).getPropertyValue('--bg-img');
    console.log(styles);

    if (styles == "url('/images/point-bottom.svg')"){
        let newBg = "url('/images/point-top.svg')";
        events.style.setProperty('--bg-img', newBg);
    } else {
        let newBg = "url('/images/point-bottom.svg')";
        events.style.setProperty('--bg-img', newBg);
    }
})


// анимация карточек
const card = document.querySelectorAll('.sights__card')

card.forEach((e) => {
    e.addEventListener('click', ActiveCard)
})

function ActiveCard () {
    card.forEach((em) => {
        em.classList.remove('active')
    })

    this.classList.add('active')
}

//анимация скрола
if (ScrollTrigger.isTouch !== 1){
    ScrollSmoother.create({
        wrapper: '.wrapper',
        content: '.content',
        effects: true
    })

    gsap.fromTo('.reasons__h', { opacity: 0}, {
        opacity: 1,
        scrollTrigger: {
            trigger: '.reasons__h',
            start: 80,
            end: 'center',
            scrub: true
        }
    })
}

// document.querySelector('.sights__btn-more').addEventListener('click', () => {
//     setTimeout(() => {
//         document.querySelector('body').classList.add('close')
//     }, 1000)
// })