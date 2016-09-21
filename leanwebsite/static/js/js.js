(function(){
/**/

    var utils = {};

/* ressources */
var img = new Image();
var ctx = document.getElementById('cnv').getContext("2d");
var cnvWidth = ctx.canvas.width;
var cnvHeight = ctx.canvas.height;


/* game loop */
function gameLoop(){
    msg("canvas", 12, 103);
    msg("demo", 20);
}

function msg(m, x, y){
    if(y == undefined){
        if (x == undefined){ 
            x=10;
        }

        y=250;
    }

  ctx.save();
    var my_gradient=ctx.createLinearGradient(0,0,0,170);
    my_gradient.addColorStop(0,"black");
    my_gradient.addColorStop(1,"white");
    ctx.fillStyle=my_gradient;
    ctx.font = "80px Nunito";
    ctx.fillText(m, x, y);
  ctx.restore();
}

gameLoop();
})();
