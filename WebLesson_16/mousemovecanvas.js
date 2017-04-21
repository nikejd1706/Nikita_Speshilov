function mouse()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");

    window.addEventListener("mousemove", icon, false);
}

function icon(e) {
    canvas.clearRect(0, 0, 1000, 1000);
    var xPos = e.clientX;
    var yPos = e.clientY;
    var pic = new Image();
    pic.src = "https://vignette4.wikia.nocookie.net/nintendo/images/3/3e/MTO_Tennis_Ball.png/revision/latest?cb=20120504075543&format=original&path-prefix=en";
    canvas.drawImage(pic, xPos-100, yPos-100, 200, 200);
}

window.addEventListener("load", mouse, false);