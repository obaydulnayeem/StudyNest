document.addEventListener('DOMContentLoaded', function () {
    const togglefaqLinks = document.querySelectorAll('.togglefaq');

    togglefaqLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const answer = this.nextElementSibling;
            const icon = this.querySelector('i');

            // Toggle answer visibility
            if (answer.style.display === 'block') {
                answer.style.display = 'none';
                icon.classList.remove('fa-minus');
                icon.classList.add('fa-plus');
            } else {
                answer.style.display = 'block';
                icon.classList.remove('fa-plus');
                icon.classList.add('fa-minus');
            }
        });
    });
});
