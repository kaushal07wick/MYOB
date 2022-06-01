
  var changebg = function() {
  if (myscore % 20 == 0) {
    level++;
    document.getElementById("level").innerHTML = "Level: " + level;
    $("#level").fadeIn(1500, function(){$("#level").hide()})
    backgroundindex++;
    if (backgroundindex > 6) {
      backgroundindex == Math.floor((Math.random()*6)+1)};
    document.getElementById("background").src="/bg"+backgroundindex+".jpg";
  };
}
