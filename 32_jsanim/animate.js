var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "#0000FF";

var requestID;

var clear = (e) => {
   // e.preventDefault();
    ctx.clearRect(0, 0, c.width, c.height);
};

var dvdLogoSetup =  function() {
    window.cancelAnimationFrame(requestID);

    var rectWidth = 60;
    var rectHeight = 40;

    // var rectX = 200;
    // var rectY = 200;
    var rectX = Math.random()*(c.width-rectWidth);
    var rectY = Math.random()*(c.height- rectHeight);

    var xVel = 2
    var yVel = 2

    var logo = new Image();
    logo.src = "logo_dvd.jpg";


    var dvdLogo =  function() {
        ctx.clearRect(0, 0, c.width, c.height);
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
        //ctx.fill();
     if(rectX > c.width-rectWidth){
            xVel = -xVel;
        }
     if(rectY > c.height-rectHeight){
            yVel = -yVel;
     }
     if(rectX<=0){
        xVel = -xVel;
      }
      if(rectY<=0){
          yVel = -yVel;
       }
        rectX = rectX + xVel;
        rectY = rectY + yVel;
        requestID = window.requestAnimationFrame(dvdLogo);
       };
      dvdLogo();
    };

var radius = 0;
var growing  = true;


let drawCirc = function() {
    ctx.beginPath();
    ctx.arc(c.width/2, c.height/2, radius, 0, Math.PI*2);
    ctx.fill();
    ctx.closePath();
  }

var drawDot = () => {
    clear();
    if(radius==c.width/2){
        growing = false;
    }
    else if(radius==0){
        growing = true;
    }

    if (growing){
        radius++;
    }else{
        radius--;
     }
     
    drawCirc();

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
}


var stopIt = () => {
    console.log("stopIt invoked...");
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
}

dotButton.addEventListener("click",drawDot);
dvdButton.addEventListener("click", dvdLogoSetup);
stopButton.addEventListener("click", stopIt);