// Sends the service-request form to Web3Forms, which emails it to javier@pcninja.pro.
// Required fields are enforced by the browser (required attributes) before this runs.
(function () {
  var form = document.getElementById('request-form');
  if (!form) return;
  var status = document.getElementById('form-status');
  var button = form.querySelector('button[type="submit"]');
  var t = form.dataset;

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.checkValidity()) { form.reportValidity(); return; }
    button.disabled = true;
    button.textContent = t.sending;
    status.hidden = true;

    fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: { 'Accept': 'application/json' },
      body: new FormData(form)
    })
      .then(function (r) { return r.json(); })
      .then(function (res) {
        if (!res.success) throw new Error(res.message || 'failed');
        form.reset();
        status.className = 'form-status ok';
        status.textContent = t.sent;
      })
      .catch(function () {
        status.className = 'form-status err';
        status.textContent = t.failed;
      })
      .finally(function () {
        status.hidden = false;
        button.disabled = false;
        button.textContent = t.send;
        status.scrollIntoView({ block: 'nearest' });
      });
  });
})();
