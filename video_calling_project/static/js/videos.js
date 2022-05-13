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
  
  
  
  sessionStorage.setItem('dept', 'bscit')
  sessionStorage.setItem('exam', 'computer')
  
  const dept = sessionStorage.getItem('dept')
  const exam = sessionStorage.getItem('exam')
  
  console.log(dept)
  console.log(exam)
  
  bucket_name = exam + dept;
  
  
  console.log(sessionStorage.getItem('video_file'))
  sessionStorage.setItem('video_file', 'https://dq56bnzycx68u.cloudfront.net/computer_bscit/18Bit048.mp4')
  
  // submit event.
  const video_puller = async() => {
  
   
	
	
  }
  // this is for adding the videos automatically.
  const v = document.getElementById("player");
  console.log(v)
  
  var source = document.createElement('source');
  source.setAttribute('src', sessionStorage.getItem('video_file'));
  source.setAttribute('type', 'video/mp4');
  
  v.appendChild(source);
  
  console.log(v)
  