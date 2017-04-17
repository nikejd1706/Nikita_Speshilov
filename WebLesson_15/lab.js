function shapes()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    canvas.beginPath();
    canvas.moveTo(300, 200);
    canvas.lineTo(400, 250);
    canvas.lineTo(300, 300);
    canvas.lineTo(380, 400);
    canvas.lineTo(230, 330);
    canvas.lineTo(215, 475);
    canvas.lineTo(160, 330);
    canvas.lineTo(130, 400);
    canvas.stroke();
    canvas.closePath();
}
window.addEventListener("load", shapes, false);
