// Welcoming message

var alerted = localStorage.getItem('alerted') || '';
if (alerted != 'yes') {
 alert("If you are using a smartphone, for a better experience, rotate your phone :)");
 localStorage.setItem('alerted','yes');
}

// No right click in website
// document.addEventListener('contextmenu', event => event.preventDefault());
