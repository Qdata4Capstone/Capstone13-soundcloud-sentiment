$(document).on("click", "td", function(event){
    $("td").removeClass("selected");
    var targetClass = $(this).attr("class");
    $("." + targetClass).addClass("selected");
});