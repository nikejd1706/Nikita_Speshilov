function drag() {
    mantis = document.getElementById("mantisShrimp");
    leftbox = document.getElementById("leftBox");

    mantis.addEventListener("dragstart", startDrag, false);

    leftbox.addEventListener("dragenter", function(e){e.preventDefault()}, false);
    leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
    leftbox.addEventListener("drop", drop, false);
}

function startDrag(e){
    var pic = '<img id = "mantisShrimp" src = "https://upload.wikimedia.org/wikipedia/commons/3/39/OdontodactylusScyllarus2.jpg">';
    e.dataTransfer.setData('Picture', pic);
}

function drop(e){
    e.preventDefault();
    leftBox.innerHTML = e.dataTransfer.getData('Picture');
}

window.addEventListener("load", drag, false);
