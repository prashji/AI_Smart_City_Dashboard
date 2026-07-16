// ============================
// Live Clock
// ============================

function updateClock() {

    const now = new Date();

    const time = now.toLocaleTimeString();

    document.getElementById("clock").innerHTML = time;

}

setInterval(updateClock,1000);

updateClock();


// ============================
// Theme Change
// ============================

function changeTheme(){

let hour=new Date().getHours();

if(hour>=6 && hour<12){

document.body.style.background=
"linear-gradient(to right,#87CEEB,#E0F7FA)";

}

else if(hour>=12 && hour<17){

document.body.style.background=
"linear-gradient(to right,#4FC3F7,#0288D1)";

}

else if(hour>=17 && hour<20){

document.body.style.background=
"linear-gradient(to right,#FF9800,#E65100)";

}

else{

document.body.style.background=
"linear-gradient(to right,#0F172A,#020617)";

}

}

changeTheme();

setInterval(changeTheme,60000);


// ============================
// Fake Traffic Animation
// ============================

const trafficStatus=[

"🟢 Low Traffic",

"🟡 Medium Traffic",

"🔴 Heavy Traffic"

];

setInterval(()=>{

let random=Math.floor(Math.random()*trafficStatus.length);

document.getElementById("traffic").innerHTML=

trafficStatus[random];

},3000);


// ============================
// Fake AQI Meter
// ============================

setInterval(()=>{

let aqi=Math.floor(Math.random()*300);

let box=document.getElementById("aqi");

box.innerHTML="AQI : "+aqi;

if(aqi<100){

box.style.color="lime";

}

else if(aqi<200){

box.style.color="orange";

}

else{

box.style.color="red";

}

},2500);


// ============================
// Electricity Usage
// ============================

setInterval(()=>{

let unit=Math.floor(Math.random()*500);

document.getElementById("electricity").innerHTML=

"Usage : "+unit+" kWh";

},3000);


// ============================
// Parking Availability
// ============================

setInterval(()=>{

let free=Math.floor(Math.random()*100);

document.getElementById("parking").innerHTML=

"Available : "+free+" Slots";

},3000);


// ============================
// Weather Placeholder
// ============================

const weather=[

"☀ Sunny",

"☁ Cloudy",

"🌧 Rainy",

"⛈ Storm",

"🌤 Clear"

];

setInterval(()=>{

let random=Math.floor(Math.random()*weather.length);

document.getElementById("weather").innerHTML=

weather[random];

},3000);


// ============================
// AI Suggestion Placeholder
// ============================

const ai=[

"Use Public Transport",

"AQI is High. Wear Mask",

"Parking Available Nearby",

"Weather is Good for Travel",

"Save Electricity Today"

];

setInterval(()=>{

let random=Math.floor(Math.random()*ai.length);

document.getElementById("ai").innerHTML=

ai[random];

},4000);