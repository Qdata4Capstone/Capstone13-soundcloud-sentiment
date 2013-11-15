$(document).on("click", "td", function(event){
    var targetClass = $(this).attr("class");
    $(this).css("background-color", "red");
    $("." + targetClass).css("background-color", "red");
});