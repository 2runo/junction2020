var $video = $('#video');
var video = $video[0];
var $canvas = $('#canvas');
var canvas = $canvas[0];
var ctx = canvas.getContext('2d');
var cursor = $("#cursor")[0];

if (navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
      video.srcObject = stream;
    })
    .catch(err => {
      console.warn(err);
    });
}

function takePic() {
    // 사진 찍기
    console.log('take picture')
    // $canvas.css('width', $video.css('width'))
    // $canvas.css('height', $video.css('height'))
    ctx.drawImage(video, 0, 0);
    $canvas.css('display', 'block');
    $canvas.css('visibility', 'visible');
    $video.css('display', 'none');
    $video.css('visibility', 'hidden');
}

var timeoutIds = [];
$('body').on("vmousedown touchstart", () => {
    let id = setTimeout(() => {takePic()}, 1000);  // 1초 누르고 있으면 사진 찍기
    timeoutIds.push(id);
})

$('body').on("vmouseup touchend", () => {
    for (var i in timeoutIds) {
        clearTimeout(timeoutIds[i]);
    }
    timeoutIds = [];
})

