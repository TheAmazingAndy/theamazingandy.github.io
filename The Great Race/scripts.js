
function startRace() {
	let newImage = "greenlight.png";
	document.getElementById("imageToChange").src = newImage;
	animateRacer("player1", true);
	animateRacer("player2", true);
}

function animateRacer(playerId, reset) {
  var elem = document.getElementById(playerId);
  var pos = parseInt(elem.style.left, 10);
  if (isNaN(pos) || reset) {
    pos = 0;
  }
  

  if (pos < 1350) {
    pos += randStep(3);
    elem.style.left = pos + 'px';
    setTimeout('animateRacer("' + playerId + '")', randStep(5));
  }
  
}
	

function randStep(max) {
  var min = 1;
  return Math.floor(Math.random() * (max - min)) + min;
}