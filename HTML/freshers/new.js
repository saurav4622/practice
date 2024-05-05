
window.onscroll = function() {
    scrollFunction();
  };
  
  function scrollFunction() {
    if (document.body.scrollTop > 500 || document.documentElement.scrollTop > 500) {
      document.getElementById("heading").style.opacity = "0";
      document.getElementById("heading").style.transform = "scale(0.9)";
    } else if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
      document.getElementById("heading").style.fontSize = "30px";
      document.getElementById("heading").style.padding = "0";
      document.getElementById("heading").style.opacity = "1";
      document.getElementById("heading").style.transform = "scale(1)";
    } else {
      document.getElementById("heading").style.fontSize = "80px";
      document.getElementById("heading").style.padding = "";
      document.getElementById("heading").style.opacity = "1";
      document.getElementById("heading").style.transform = "scale(1)";
    }
  }
  