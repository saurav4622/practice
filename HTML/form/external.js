 // When the user scrolls down 50px from the top of the document, resize the heading's font size
 window.onscroll = function() {scrollFunction()};
            
 function scrollFunction() {
   if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
     document.getElementById("heading").style.fontSize = "15px";
   } else {
     document.getElementById("heading").style.fontSize = "75px";
   }
 }