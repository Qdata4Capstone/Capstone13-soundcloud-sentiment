function drawWaveForm(){
    var waveform = new Waveform({
        container: $('#test')[0],
        data: [1, 0.2, 0.5]
    });
}

$(document).ready(function(){
    $('#trigger').on('click', function(){
        drawWaveForm();
    });
});
