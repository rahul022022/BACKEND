document.addEventListener('DOMContentLoaded', function () {
    const addBtn = document.getElementById('add-doctor-btn');
    const modal = document.getElementById('doctor-form-modal');
    const closeBtn = document.getElementById('close-modal');
    const form = document.getElementById('ajax-doctor-form');
    const list = document.getElementById('doctor-list');

    if (!addBtn || !modal || !form || !list) return;

    addBtn.addEventListener('click', function () {
        modal.classList.remove('hidden');
    });

    closeBtn.addEventListener('click', function () {
        modal.classList.add('hidden');
    });

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        const url = '/api/doctors/add/';
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'X-Requested-With': 'XMLHttpRequest',
            },
            body: new FormData(form)
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                const li = document.createElement('li');
                const link = document.createElement('a');
                link.href = '/doctors/' + data.id + '/';
                link.textContent = data.name;
                li.appendChild(link);
                list.appendChild(li);
                modal.classList.add('hidden');
                form.reset();
            } else {
                alert('Error saving doctor');
            }
        })
        .catch(err => {
            console.error(err);
            alert('Error saving doctor');
        });
    });
});
