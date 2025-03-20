const dynamicImage = document.getElementById("dynamic-image")
const dynamicImageSecond = document.getElementById("dynamic-image-second")

const conn1 = SocketConnection(getTEnvObjectData("emulator").namespace)
const conn2 = SocketConnection(getTEnvObjectData("emulator_second").namespace)

conn1.socket.on("image", image => {
    dynamicImage.src = image
})

conn2.socket.on("image", image => {
    dynamicImageSecond.src = image
})
