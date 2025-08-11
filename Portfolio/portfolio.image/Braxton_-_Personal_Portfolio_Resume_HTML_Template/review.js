document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevents form from submitting the traditional way

    // Get the username and password values
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Check if the username and password match (this can be expanded later for real authentication)
    if (username === "pediatrician" && password === "safePassword123") {
        alert("Login Successful!");
        window.location.href = "dashboard.html"; // Redirect to a dashboard or home page
    } else {
        // Display error message if credentials don't match
        document.getElementById("error-message").style.display = "block";
        document.getElementById("error-message").innerText = "Invalid username or password!";
    }
});
