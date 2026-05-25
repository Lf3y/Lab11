const form = document.getElementById("contact-form");
const successMessage = document.getElementById("success-message");
const errorMessage = document.getElementById("error-message");

/**
 * Проверяет корректность заполнения формы.
 * @returns {boolean}
 */
const isFormValid = () => {
  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const message = document.getElementById("message").value.trim();
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  return Boolean(name && emailPattern.test(email) && message);
};

/**
 * Скрывает все сообщения формы.
 */
const hideMessages = () => {
  successMessage.classList.add("hidden");
  errorMessage.classList.add("hidden");
};

form.addEventListener("submit", (event) => {
  event.preventDefault();
  hideMessages();

  if (isFormValid()) {
    successMessage.classList.remove("hidden");
    form.reset();
    return;
  }

  errorMessage.classList.remove("hidden");
});
