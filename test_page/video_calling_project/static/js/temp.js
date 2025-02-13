var alertRedInput = "#8C1010";
var defaultInput = "rgba(10, 180, 180, 1)";


var texts = document.querySelectorAll(".change"); 
texts.forEach((text) => {
    text.addEventListener("mouseover", () => {
    console.log("works", text.style.color="white")
})
})

texts.forEach((text) => {
    text.addEventListener("mouseout", () => {
    console.log("works", text.style.color="#7FFFD4")
})
})



const form = document.querySelector(".signupSection")
console.log(form)

// we need to send the call to get the token for the user, once he filled the fields and submitted the form.
const fetch_token = async(event) => {
    
    // event.preventdefault will won't allow the default event to be happened, meaning in our eg submit event takes the
    // user to the new page if it is specified else, it refreshs the page. so that will won't be happened.
    event.preventDefault()
   
    const RoomName = event.target.room.value
    const username = event.target.username.value
    const response = await fetch(`get_token?channel=${RoomName}`)
    const data = await response.json()
    const token = data.token
    const uid = data.uid
    
    sessionStorage.setItem('token', token)
    sessionStorage.setItem('room', RoomName)
    sessionStorage.setItem('UID', uid)

    console.log(token, uid)
    console.log(window)

    // this bring the user to the room/ route and _self parameter
    // is for keeping the user to stick to single tab while taking him
    // to new route
    window.open('room/', "_self")
}

form.addEventListener('submit', fetch_token)


