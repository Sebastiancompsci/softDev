// retrieve node in DOM via ID
let c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2Dobject
let ctx =c.getContext("2d");

//init global state var
let mode = "rect";

        
let toggleMode = function(e){
        console.log("toggling...");
        if (mode == "rect") {
            mode = "circ";
            btoggler.innerHTML = "Circle";
        } else {
            mode = "rect";
            btoggler.innerHTML = "Rectangle";
            }
        }

let drawRect = function(e){
    let mouseX = e.offsetX;
    let mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillStyle=("#ff0000");
    ctx.fillRect(mouseX,mouseY,100,100);
    }

let drawCircle = function(e){
    let mouseX = e.offsetX;
    let mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillStyle=("#ff0000");
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 50, 0, Math.PI*2);
    ctx.fill();
    }

let draw = function(e){
    if (mode == "rect"){
    drawRect(e);
    } else {
        drawCircle(e);
      }
    }

let wipeCanvas = function() {
    ctx.clearRect(0, 0, 600, 600);
    }

c.addEventListener("click", draw);
let btoggler = document.getElementById("buttonToggle");
btoggler.addEventListener("click", toggleMode);
let clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);
    
    
    
    
