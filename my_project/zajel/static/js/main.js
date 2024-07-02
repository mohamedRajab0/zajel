function appear_settings() {
    var stiting = document.getElementByID("settings");
    if (stiting.style.display === "block") {
        stiting.style.display = "none";
    }
    else {
        stiting.style.display = "block";
    }
}