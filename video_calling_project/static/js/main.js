// Until now, we are statically creating a token and channels for ourselves, but in the 
// production env we need to give a freedom for the users to generate their own token
// and channel for that we will use the agora token generator in python to do the token
// generate dynamically in agora.
//
// we need to include the functionality of generate link and also sharing the link via gmail. So this will be flexible for the users to work on.`


// we are using the backend to store the username and we are retreving it, because 
// we are storing where users details in their own session, other users, don't have 
// an access to other user session. that's why we are storing the information in 
// database.
const APP_ID = '9585a50464ce4126b4a932dbce5225c0'

// from the session storage we are getting the values which is been stored in the previous page
// when the user actually logged in.
const TOKEN = sessionStorage.getItem('token')
const CHANNEL = sessionStorage.getItem('room')
let UID = sessionStorage.getItem('UID')

// we are accessing our name, but this won't be shown to other users. so we will create
// the database and store the name, so we can able to get them, even when other users are joining.
let NAME = sessionStorage.getItem('name')


const client = AgoraRTC.createClient({mode:'rtc', codec:'vp8'})

let localTracks = []
let remoteUsers = {}

// this function is only called for the users, who are creating the channel.
let joinAndDisplayLocalStream = async () => {
    // we are setting the value for that particular html text
    document.getElementById('room-name').innerText = CHANNEL

    // we are looking for the two events, one is users login and users hanging up the 
    // call
    client.on('user-published', handleUserJoined)
    client.on('user-left', handleUserLeft)

    // if it is success, we are joining the user in the call
    try{
        // async gives the promise resolved in the await, so we usually use the 
        // try and catch block for the resolved and rejected promises.
        // await always accepts the promises.
        UID = await client.join(APP_ID, CHANNEL, TOKEN, UID)
    }
    // if there is any error, we are routing the users, back to the main page.
    // using django, we should show some error message here, if the users does'nt 
    // provied a channel name. because we are just refreshing the page.
    catch(error){
        console.error(error)
        window.open('/', '_self')
    }
    
    // accessing the microphone and camera of the users by their permission
    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

    // we are creating the user, by their name, uid, channel, so we can able to
    // retrieve their username, when other users are logging in, it will give us
    // a user's information which is stored.
    let member = await createMember()

    console.log(member, "member1")

    console.log(localTracks[0], "localtrack0")

    console.log(localTracks[1], "localtrack1")

    // After creating a player for a client whoever joins the channel, we will add it to the DOM
    // Below code make sure to add each video Player to the stream we created before
    let player = `<div  class="video-container" id="user-container-${UID}">
                     <div class="video-player" id="user-${UID}"></div>
                     <div class="username-wrapper" style = color:"white"> <span class="user-name">${member.name} </span></div>
                  </div>`
    document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)
    
    // playing the video of the users
    localTracks[1].play(`user-${UID}`)
    // publishing the video of the users to other users in the channel
    await client.publish([localTracks[0], localTracks[1]])
}

// this function will be invoked, when the second and preceeding users are join
// this will return a other users video and audio streams who are in current channel
// so it can be shown in their screen.
let handleUserJoined = async (user, mediaType) => {
    remoteUsers[user.uid] = user
    await client.subscribe(user, mediaType)

    if (mediaType === 'video'){
        let player = document.getElementById(`user-container-${user.uid}`)
        if (player != null){
            player.remove()
        }

        // this will give the members detail, who are already there in the 
        // channel
        let member = await getMember(user)
        console.log("member", member.name)

        player = `<div  class="video-container" id="user-container-${user.uid}">
            <div class="video-player" id="user-${user.uid}"></div>
            <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
        </div>`

        document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)
        user.videoTrack.play(`user-${user.uid}`)
    }

    if (mediaType === 'audio'){
        user.audioTrack.play()
    }
}

// this is will be invovked when users clicks the leave button
let handleUserLeft = async (user) => {
    delete remoteUsers[user.uid]
    document.getElementById(`user-container-${user.uid}`).remove()
}

// we also take care of removing the streams from our array, we created .
let leaveAndRemoveLocalStream = async () => {
    for (let i=0; localTracks.length > i; i++){
        localTracks[i].stop()
        localTracks[i].close()
    }

    await client.leave()
    // this will delete the users details in the backend. so we need not to consume the 
    // space 
    //This is somewhat of an issue because if user leaves without actaull pressing leave button, it will not trigger
    deleteMember()
    window.open('/', '_self')
}

// We are trying turn off the video of the users, if they click the button this method 
// will be invovked
let toggleCamera = async (e) => {
    console.log('TOGGLE CAMERA TRIGGERED')
    if(localTracks[1].muted){
        await localTracks[1].setMuted(false)
        e.target.style.backgroundColor = '#fff'
    }else{
        await localTracks[1].setMuted(true)
        e.target.style.backgroundColor = 'rgb(255, 80, 80, 1)'
    }
}

// Same like a video, we also need to have a event listener that will be look for an
// event of users clicking the button of toggling mic 
let toggleMic = async (e) => {
    console.log('TOGGLE MIC TRIGGERED')
    if(localTracks[0].muted){
        await localTracks[0].setMuted(false)
        e.target.style.backgroundColor = '#fff'
    }else{
        await localTracks[0].setMuted(true)
        e.target.style.backgroundColor = 'rgb(255, 80, 80, 1)'
    }
}

// we are storing the users information in the database. we are posting the information
// to the backend, so it can able to store these users information in the backend.
let createMember = async () => {
    let response = await fetch('/create_member/', {
        method:'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'name':NAME, 'room_name':CHANNEL, 'UID':UID})
    })
    let member = await response.json()
    return member
}

// we are trying to get the members details, who are already in the channel.
let getMember = async (user) => {
    let response = await fetch(`/get_member/?UID=${user.uid}&room_name=${CHANNEL}`)
    let member = await response.json()
    return member
}

// we are trying to send the users information, who are left the call.
let deleteMember = async () => {
    let response = await fetch('/delete_member/', {
        method:'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'name':NAME, 'room_name':CHANNEL, 'UID':UID})
    })
    let member = await response.json()
}

// we are also deleting the members, who are just closing the window, instead of 
// pressing the call end button. so this will take care of that.
// beforeunload event will take care of that
window.addEventListener("beforeunload",deleteMember);

joinAndDisplayLocalStream()


// event listeners, that will be listening for the users to click the any of the three
// buttons camera off and on, leave on and off
document.getElementById('leave-btn').addEventListener('click', leaveAndRemoveLocalStream)
document.getElementById('camera-btn').addEventListener('click', toggleCamera)
document.getElementById('mic-btn').addEventListener('click', toggleMic)

