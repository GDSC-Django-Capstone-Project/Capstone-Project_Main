  function redirectToStudentLoginPage() {
    window.location.href = "student_login.html";
  }

  function redirectToStudentPage() {
    window.location.href = "student.html";
  }

  function redirectToAdminPage() {
    var adminPassword = prompt("Enter Admin Password");
    if (adminPassword === "12345") {
      window.location.href = "admin.html";
    } else {
      alert("Incorrect Admin Password");
    }
  }
  const passwordInput = document.getElementById("pass");
  const confirmPasswordInput = document.getElementById("cpass");
  const errorSpan = document.getElementById("password-error");

  confirmPasswordInput.addEventListener("input", () => {
    if (passwordInput.value !== confirmPasswordInput.value) {
      errorSpan.textContent = "Passwords do not match";
    } else {
      errorSpan.textContent = "";
    }
  });

  
