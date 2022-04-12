const token = '0069585a50464ce4126b4a932dbce5225c0IABvlkTRhz8eFCDz7/UtBhm1aX7Xb/4mTDHXDjjvb+Izb0mwxnQAAAAAEABQyPoBlBRQYgEAAQCUFFBi'
const channel = "nw"
const app_id = "9585a50464ce4126b4a932dbce5225c0"


const client = AgoraRTC.createClient({ mode: 'rtc', codec: "vp8" });

// Here we will store the voice tracks and video tracks of the remote users
let localTracks = [];

// Here we will store names og the remote users
let remoteUsers = {};

// This function is called when the client joins the channel
(async() => {
    // this will make sure to add them in their specific channel, this will give their user id for each user
        UID = await client.join(
        app_id, 
        channel, 
        token,
        null
    )
    // this is appending a audio and video of the specific client 
    localTracks = await AgoraRTC.createMicrophoneandCameraTracks();
    
    // We are creating a dynamic div for each user to display their video and their name with their consponding uid
    let video_player = `<div class="video-container" id = "user-container-${UID}">
    <div class="video-player" id="user-${UID}"></div> 
    <div class="username-wrapper"><span class="user-name">Dennis Ivanov</span></div>
    </div>`

    // After creating a player for a client whoever joins the channel, we will add it to the DOM
    // Below code make sure to add each video Player to the stream we created before
    document.getElementById("video-streams").insertAdjacentHTML('beforeend', video_player);
    
    prompt("A")
    console.log("Ss")

    // We need to play the video and audio track   to display the video and audio of the user
 localTracks[1].play("user-" + UID);
    // For publishing a audio and video  track to whole channel  
    await client.publish(localTracks[0], localTracks[1]);
   
})();