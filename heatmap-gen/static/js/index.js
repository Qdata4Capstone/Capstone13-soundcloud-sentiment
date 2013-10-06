function drawWaveForm(){
    var waveform = new Waveform({
        container: $('#test')[0],
        data: [0.3, 0.5, 1],
        innerColor: function(x, y){
            if (scores[x.toFixed(6)] !== undefined) {
                if(scores[x.toFixed(6)] == "really_positive"){
                    console.log("rp hit");
                    return '#00FF00';
                }
                else if (scores[x.toFixed(6)] == "semi_positive"){
                    console.log("sp hit");
                    return '#FFFF00';
                }
                else{
                    console.log("else hit");
                    return '#FFFFFF';
                }
            }else {
                console.log("no comment hit");
                return '#FFFFFF';
            }
        }
    });
}

$(document).ready(function(){
    $('#trigger').on('click', function(){
        drawWaveForm();
    });
});
