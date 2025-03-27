const dynamicImage = document.getElementById("dynamic-image")
const dynamicImageSecond = document.getElementById("dynamic-image-second")

const socket1 = io(getTEnvObjectData("emulator").namespace)
const socket2 = io(getTEnvObjectData("emulator_second").namespace)

socket1.on("image", image => {
    dynamicImage.src = image
})

socket2.on("image", image => {
    dynamicImageSecond.src = image
})
