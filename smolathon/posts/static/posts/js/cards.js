const cards = document.querySelectorAll('.card');
const icons = document.querySelectorAll('.circle');
const searchLink = document.getElementById('search-icon')
const searchInput = document.querySelector('.search__input')

searchLink.addEventListener('click', () => {
  searchInput.classList.toggle('none')
})

//cards.forEach(card => {
//  card.addEventListener('click', (e) => {
//
//    const sectionCards = document.querySelector('.section__cards');
//    const description = document.querySelector('.description');
//    const bg = document.querySelector('.header__bg');
//
//    sectionCards.classList.add('none');
//    description.classList.remove('none');
//    description.style.backgroundImage += 'url(' + `${e.target.src}` + ')';
//    bg.style.backgroundColor = 'transparent'
//    document.querySelectorAll('.nav__list-a').forEach((el) => {
//    el.style.color = 'white'
//    })
//
//    document.querySelector('.prev-descr').addEventListener('click', () => {
//      sectionCards.classList.remove('none');
//      description.classList.add('none');
//
//      bg.style.backgroundColor += 'var(--gray)'
//
//      document.querySelectorAll('.nav__list-a').forEach((el) => {
//        el.style.color = 'black'
//      })
//    })
//
//  })
//
//
//});

icons.forEach((e) => {
  e.addEventListener('click', () => {
    icons.forEach((e) => {
      e.querySelector('a').classList.remove('active')
    })
    e.querySelector('a').classList.add('active')
  })
})

