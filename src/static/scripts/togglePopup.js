let popupIsOppened = false

let TogglePopup = () => {
    popupIsOppened = !popupIsOppened

    if (popupIsOppened) {
        document.getElementById("popup").classList.remove("hidden")
    } else {
        document.getElementById("popup").classList.add("hidden")
    }
}