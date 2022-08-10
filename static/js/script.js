window.onload = function(self) {
    if (window.innerWidth > 767) {
        document.getElementById('autobox').style.maxWidth = window.innerWidth - 200 +'px';
    }
}

window.onresize = function(self) {
    if (window.innerWidth > 767) {
        document.getElementById('autobox').style.maxWidth = window.innerWidth - 200 +'px';
    }

}
