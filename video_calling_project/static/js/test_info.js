let step = 'step1';

const step1 = document.getElementById('step1');
const step2 = document.getElementById('step2');
const step3 = document.getElementById('step3');
const step4 = document.getElementById('step4');

function next() {
  if (step === 'step1') {
    step = 'step2';
    step1.classList.remove("is-active");
    step1.classList.add("is-complete");
    step2.classList.add("is-active");

  } else if (step === 'step2') {
    step = 'step3';
    step2.classList.remove("is-active");
    step2.classList.add("is-complete");
    step3.classList.add("is-active");

  } else if (step === 'step3') {
    step = 'step4d';
    step3.classList.remove("is-active");
    step3.classList.add("is-complete");
    step4.classList.add("is-active");

  } else if (step === 'step4d') {
    step = 'complete';
    step4.classList.remove("is-active");
    step4.classList.add("is-complete");

  } else if (step === 'complete') {
    step = 'step1';
    step4.classList.remove("is-complete");
    step3.classList.remove("is-complete");
    step2.classList.remove("is-complete");
    step1.classList.remove("is-complete");
    step1.classList.add("is-active");
  }
}
const attempts = document.querySelector('.attempts')

window.addEventListener("load", ()=>{
  const button = document.querySelector('button');
  console.log(button, "button")
  const startValues = sessionStorage.getItem('startDate');
  const endValues = sessionStorage.getItem('endDate');
  const valid = sessionStorage.getItem('valid');
  const start = document.querySelector('.start');
  const end = document.querySelector('.end');
  attempts.innerHTML = `Number of Attempts: ${localStorage.getItem("count")}`;

  start.innerHTML = `Start Date: ${startValues.slice(5, startValues.length)}`;
  end.innerHTML = `End Date: ${endValues.slice(3, endValues.length)}`;

  if(valid==="false"){
    console.log("s")
    button.setAttribute('disabled', '');

  }
  
});


const handleSubmit = ( ) => {
  let attemptCount = 0 ;
  if (localStorage.getItem("count")){
    attemptCount = localStorage.getItem("count");
    attemptCount = Number(attemptCount)
    attemptCount += Number(1);
    localStorage.setItem("count", attemptCount);
    attempts.innerHTML = `Number of Attempts: ${attemptCount}`
    window.open("/test/take", "_self");
  }
  else{
    localStorage.setItem("count", 1);
    attempts.innerHTML = `Number of Attempts: ${1}`
    window.open("/test/take", "_self");
  }
  
  
}
