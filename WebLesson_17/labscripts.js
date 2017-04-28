function drag() {
    mantis = document.getElementById("tennisball");
    leftbox = document.getElementById("leftBox");

    mantis.addEventListener("dragstart", startDrag, false);
    mantis.addEventListener("dragend", endDrag, false);

    leftbox.addEventListener("dragenter", dragEnter, false);
    leftbox.addEventListener("dragleave", dragLeave, false);
    leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
    leftbox.addEventListener("drop", drop, false);
}

function startDrag(e) {
    var pic = '<img id = "tennisball" src = "https://vignette4.wikia.nocookie.net/nintendo/images/3/3e/MTO_Tennis_Ball.png/revision/latest?cb=20120504075543&path-prefix=en">';
    e.dataTransfer.setData('Picture', pic);
}

function dragEnter(e) {
    e.preventDefault();
    leftbox.style.background = "#80637c";
    leftbox.style.border = "3px solid green";
}

function dragLeave(e) {
    e.preventDefault();
    leftbox.style.background = "white";
    leftbox.style.border = "3px solid purple";
}
function drop(e) {
    e.preventDefault();
    leftBox.innerHTML = e.dataTransfer.getData('Picture');
}

function endDrag(e) {
    pic = e.target
    pic.style.visibility = "hidden";
}

window.addEventListener("load", drag, false);
