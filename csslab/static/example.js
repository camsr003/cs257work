function changeColor() {
  the_heading = document.getElementById("nextpageText");
  if (the_heading.style.color == "red")
    the_heading.style.color = "purple";
  else
    the_heading.style.color = "red";
  console.log("I just changed the color to: " + the_heading.style.color)  
}
