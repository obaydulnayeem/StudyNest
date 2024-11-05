// SHARE LINK
// Replace this with your function to retrieve the base URL of your application
function getBaseURL() {
    // Implement the logic to get the base URL of your application
    // This might involve Django's template tags or other methods to obtain the base URL
    return 'http://127.0.0.1:8000/'; // Replace with your actual base URL
}

function generateShareLink(resourceId) {
    var baseUrl = getBaseURL();
    var shareableLink = baseUrl + 'study/share/' + resourceId;

    var tempInput = document.createElement('input');
    tempInput.value = shareableLink;
    document.body.appendChild(tempInput);

    tempInput.select();
    tempInput.setSelectionRange(0, 99999);
    document.execCommand('copy');

    document.body.removeChild(tempInput);

    // Provide a visual cue or message
    var tooltip = document.createElement('div');
    tooltip.textContent = 'Link copied!';
    tooltip.style.position = 'fixed';
    tooltip.style.bottom = '500px';
    tooltip.style.right = '10px';
    tooltip.style.padding = '10px';
    tooltip.style.backgroundColor = '#65a147';
    tooltip.style.color = 'white';
    tooltip.style.borderRadius = '5px';
    tooltip.style.opacity = '0';
    tooltip.style.transition = 'opacity 0.5s';

    document.body.appendChild(tooltip);

    // Show the tooltip
    tooltip.style.opacity = '1';

    // Hide the tooltip after a delay
    setTimeout(function() {
        tooltip.style.opacity = '0';
    }, 3000);  // Adjust the delay (in milliseconds) as needed

    // Optionally, you can also keep the alert message
    alert('Copy the link?');
}
