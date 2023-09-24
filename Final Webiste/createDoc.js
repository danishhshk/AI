console.log('heoo')
let doc = document.getElementById('dropOpt')

doc.addEventListener('click', () => {
  let select = document.querySelector('.selector-cont')
  select.style.flexDirection = 'row'
  select.style.marginRight = '0px'
  document.querySelector('.btn').innerHTML = doc.innerHTML
  select.classList.remove('align')
})
