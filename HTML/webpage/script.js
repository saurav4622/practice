// Handle form submission
document.getElementById("registration-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission
    
    // Get form values
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    
    // Display confirmation message
    alert("Thank you, " + name + "! Your registration has been submitted.");
    
    // Clear form fields
    document.getElementById("name").value = "";
    document.getElementById("email").value = "";
  });
  