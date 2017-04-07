function shapes()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    canvas.beginPath();
    canvas.moveTo(50, 50);
    canvas.lineTo(75, 75);
    canvas.lineTo(75, 50);
    canvas.stroke(50, );


}

window.addEventListener("load", shapes, false);
