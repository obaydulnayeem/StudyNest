document.addEventListener("DOMContentLoaded", function() {
    var input = document.getElementById('search');
    var placeholder = input.getAttribute('data-placeholder');
    var index = 0;

    // Typing effect for placeholder text
    function type() {
        if (index < placeholder.length) {
            input.placeholder += placeholder.charAt(index);
            index++;
            setTimeout(type, 100);
        }
    }

    // Start typing effect after a short delay
    setTimeout(type, 500);

    // Add event listeners to trigger the expanded class
    input.addEventListener('focus', function() {
        input.classList.add('expanded');
    });

    input.addEventListener('blur', function() {
        if (input.value === '') { // Shrink only if the input is empty
            input.classList.remove('expanded');
        }
    });
});
