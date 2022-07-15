
const clientList = document.querySelectorAll('.list__contain')
let value

function newClientWin(){
    const newClientBtn = document.querySelector(".newclientbtn")
    const closeClientBtn = document.querySelector(".closeclientbtn")
    const newClientForm = document.querySelector(".new_client_form")
    const newClientTextIn = document.querySelector(".form_input1")
    const addClientBtn = document.querySelector(".add__btn")
    const menuItem = document.querySelectorAll('.menu__item')

    closeClientBtn.addEventListener('click', () => {
        newClientBtn.style.display = 'block'
        closeClientBtn.style.display = 'none'
        newClientForm.style.display = 'none' 
    })

    newClientTextIn.addEventListener('input', e =>{
        value = e.target.value
        if (value) {
            addClientBtn.style.display = 'block'
        }
        else {
            addClientBtn.style.display = 'none'
        }
    })


    newClientBtn.addEventListener('click', () => {
        newClientBtn.style.display = 'none'
        closeClientBtn.style.display = 'block'
        newClientForm.style.display = 'flex'    
    })

    addClientBtn.addEventListener('click', () => {
        const newClientItem = document.createElement('div')
        newClientItem.classList.add('client__item')
        newClientItem.textContent=value
        clientList[0].append(newClientItem)
        newClientForm.style.display = 'none'
    })

    for(let i in menuItem){
    menuItem[i].addEventListener('mouseover', () =>{
        menuItem[i].style.color = '#BAB444'});
    menuItem[i].addEventListener('mouseout', () =>{
        menuItem[i].style.color = 'white'})

    }

    
    
    
}


newClientWin()

