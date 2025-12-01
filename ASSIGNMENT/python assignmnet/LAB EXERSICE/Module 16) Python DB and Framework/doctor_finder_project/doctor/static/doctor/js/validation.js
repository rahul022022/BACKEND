function validateRegistrationForm() {
    const form = document.getElementById('registration-form');
    if (!form) return true;

    const password = form.querySelector('input[name="password"]');
    const confirmPassword = form.querySelector('input[name="confirm_password"]');
    const email = form.querySelector('input[name="email"]');

    if (password && confirmPassword && password.value !== confirmPassword.value) {
        alert('Passwords do not match');
        return false;
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email && !emailPattern.test(email.value)) {
        alert('Please enter a valid email');
        return false;
    }

    return true;
}
