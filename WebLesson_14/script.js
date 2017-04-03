function validate() {
    var x = document.forms.input.username.value;
    var a = document.forms.input.password.value;
    var atPos = x.indexOf("@");
    var dotPos = x.lastIndexOf(".");
    var pass = a.length;


    //we need... username@webAddress.extension
    //if, the following...
        //@ is not in the string
        //@ is in the wrong place
        //there is no .com, .gov, or any otg
        //final dot is in the wrong place
    if(atPos < 1 || dotPos < atPos+2 || dotPos + 2 > x.length)
        alert("This is not a valid email address!")

    else
        alert("Success!");
}
