// main.js
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const processingAnimation = document.getElementById('processing-animation');
    const resultsContainer = document.getElementById('results');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        // Show processing animation
        form.style.display = 'none';
        processingAnimation.style.display = 'block';

        // Create FormData object and append video file
        const formData = new FormData(form);
        const xhr = new XMLHttpRequest();
        xhr.open('POST', form.action, true);

        // Handle response
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                const results = JSON.parse(xhr.responseText);
                // Hide processing animation and show results
                processingAnimation.style.display = 'none';
                resultsContainer.style.display = 'block';
                resultsContainer.innerHTML = JSON.stringify(results, null, 2);
            }
        };

        // Send FormData
        xhr.send(formData);
    });
});
