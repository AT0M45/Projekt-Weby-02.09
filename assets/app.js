const lessonSelect = document.getElementById('lessons');
if (lessonSelect) new TomSelect('#lessons', { plugins: ['remove_button'], placeholder: 'vyberte...' });

function showMessage(formId, messageId) {
  const form = document.getElementById(formId);
  if (!form) return;
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    if (!form.checkValidity()) { form.reportValidity(); return; }
    document.getElementById(messageId).classList.remove('d-none');
    form.reset();
  });
}
showMessage('registrationForm', 'registrationMessage');
showMessage('contactForm', 'contactMessage');
