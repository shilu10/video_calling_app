// DOM Loaded
document.addEventListener("DOMContentLoaded", () => {
	const player = new Plyr("#player", {
	  title: "Spring",
	  controls: [
	  "play-large",
	  "play",
	  "progress",
	  "current-time",
	  "duration",
	  "mute",
	  "volume",
	  "settings",
	  "pip",
	  "airplay",
	  "fullscreen"] });
  
  
  
	document.querySelectorAll(".accordion").forEach(acc => {
	  acc.addEventListener("click", () => {
		acc.classList.toggle("is-active");
		let panel = acc.nextElementSibling;
		panel.style.maxHeight ?
		panel.style.maxHeight = null :
		panel.style.maxHeight = panel.scrollHeight + "px";
	  });
	});
  
	document.querySelector(".nav-toggle").addEventListener("click", e => {
	  e.currentTarget.classList.contains("is-active") ?
	  e.currentTarget.innerHTML = "Show navigation" :
	  e.currentTarget.innerHTML = "Hide navigation";
  
	  e.currentTarget.classList.toggle("is-active");
  
	  document.querySelector("#videoColumn").classList.toggle("is-full");
	  document.querySelector("#navColumn").classList.toggle("is-active");
	});
  
	document.querySelectorAll(".go-to").forEach(btn => {
	  btn.addEventListener("click", () => {
		player.currentTime = parseInt(btn.getAttribute("data-time"));
		player.play();
	  });
	});
  });
  
// Shilash Code.

// submit event.
var video_puller = async() => {

	const input_val = document.getElementById('input').value

	const dept = dropdown_values_for_first()
	const exam = dropdown_values_for_second()

	sessionStorage.setItem('video_file', `https://dq56bnzycx68u.cloudfront.net/${exam}_${dept}/${input_val}.mp4`)
  }


// for the alerts 
var alert_functionality = async () => {
	console.log(sessionStorage.getItem('video_file'))
	var response = await axios.get(sessionStorage.getItem('video_file'))
	const alert = document.getElementById('alert')
	if (response.status != 200){
		alert.style.opacity =  "1.0";
	}
	else{
		alert.style.opacity = "0";
	}

}
alert_functionality()


// this is for adding the videos automatically.
var video_player = document.getElementById("player");
var source = document.createElement('source');
source.setAttribute('src', sessionStorage.getItem('video_file'));
source.setAttribute('type', 'video/mp4');
video_player.appendChild(source);

// just for imitating the client data.
var dept = ["bscit", "bscct"]
var exam = ["computer", "math"]
// Adding the values to the option tag from the js.
var dropdown = document.getElementsByClassName("selectpicker")
var dropdown1 = document.getElementById("picker1")



dept.forEach((value) => {
	var option = document.createElement('option');
	var option_value = document.createTextNode(value);
	option.appendChild(option_value);
	dropdown[0].appendChild(option);
})

exam.forEach((value)=>{
	var option = document.createElement('option');
	var option_value = document.createTextNode(value);
	option.appendChild(option_value);
	dropdown1.appendChild(option);

})


function dropdown_values_for_first(){
	var select = document.getElementsByClassName("selectpicker")
	console.log(select)
	val = select[0].options['selectedIndex']
	return dept[val]
} 


function dropdown_values_for_second(){
	var select = document.getElementById("picker1")
	console.log(select)
	val = select.options['selectedIndex']
	return exam[val]
} 

