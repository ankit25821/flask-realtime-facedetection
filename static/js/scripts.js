var socket;
var localstream;
const FPS = 6;
var photo = document.querySelector('#photo');
var video = document.querySelector('#videoInput');
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');

video.width = 400;
video.height = 300;

function startStream() {
    socket = io(window.location.origin);

    socket.on('connect', function () {
        console.log("Connected...!", socket.connected)
    });

    if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(function (stream) {
                video.srcObject = stream;
                localstream = stream;
                video.play();
            })
            .catch((err0r) => console.log(err0r));
    }


    setInterval(() => {
        width = video.width;
        height = video.height;
        context.drawImage(video, 0, 0, width, height);
        var data = canvas.toDataURL('image/jpeg', 0.5);
        context.clearRect(0, 0, width, height);
        socket.emit('image', data);
    }, 1000 / FPS);

    socket.on('response_back', function (data) {
        photo.setAttribute('src', data.image_data);

    });
}

function stopStream() {
    socket.disconnect()
    video.pause();
    video.src = "";
    photo.src = '';
    localstream.getTracks()[0].stop();
}