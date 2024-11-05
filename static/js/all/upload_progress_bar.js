document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('QuestionForm');
    const progressBar = document.getElementById('progressBar');
    const progressContainer = document.getElementById('progressContainer');

    form.addEventListener('submit', function (e) {
        e.preventDefault(); // Prevent default form submission

        // Show the progress container
        progressContainer.style.display = 'block';

        // Mock progress increment (replace with actual file upload logic)
        let progress = 0;
        const interval = setInterval(function () {
            if (progress >= 100) {
                clearInterval(interval);
                form.submit(); // After 100%, submit the form
            } else {
                progress += 1;
                progressBar.style.width = progress + '%';
                progressBar.setAttribute('aria-valuenow', progress);
                progressBar.innerHTML = progress + '%';
            }
        }, 50); // Adjust the time to control the speed of progress
    });
});
