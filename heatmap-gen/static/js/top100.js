function findCluster(name){
    for(var i = 0; i < groups.length; i++){
        if(groups[i].indexOf(name) > -1){
            return i;
        }
    }
}

$(document).on("click", "td", function(event){
    $("td").removeClass("selected");
    var targetClass = $(this).attr("class");
    $("." + targetClass).addClass("selected");
});