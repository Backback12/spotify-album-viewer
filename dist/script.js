/*
var timeDelay = 0;
var _delay = setInterval(delayCheck, 500);

$('.backk').on('mousemove', sendOut);
//$('.background').mousemove(sendOut)

function delayCheck() {
    if (timeDelay >= 3) {
        //$('.menu').fadeOut();
        console.log('hide');
        console.log(timeDelay);
        $('.menu').removeClass('show');
        timeDelay = 1;
    }
    timeDelay = timeDelay + 1;
}

function showAllEvent() {
    //$('.menu').fadeIn();
    $('.menu').addClass('show');
    console.log('show!')
    timeDelay = 1;
    clearInterval(_delay);
    _delay = setInterval(delayCheck, 500);
}

function sendOut() {
    console.log("worked");
}
*/

var timedelay = 1;
var _delay = setInterval(delayCheck, 500);

//$('.backk').on('mousemove', poww);
//$('.backk').onmousemove = poww;

function delayCheck() {
  if (timedelay == 3) {
    //$('.background').addClass('hidden');
    
    //$('.background').fadeOut();
    
    timedelay = 0;
    
  }
  timedelay = timedelay + 1;
  //console.log(timedelay);
}

function showAllEvent() {
  //$('.background').removeClass('hidden');
  $('.background').fadeIn();
  timedelay = 1;
  clearInterval(_delay);
  _delay = setInterval(delayCheck, 500);
  //console.log(show);
}

function poww() {
    console.log("pow")
}