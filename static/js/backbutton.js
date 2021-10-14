document.addEventListener("DOMContentLoaded", function(){
    let backButton = document.getElementsByClassName("back-button")[0];
    backButton.addEventListener("click", goBack);
})

function goBack() {
    window.history.back();
};