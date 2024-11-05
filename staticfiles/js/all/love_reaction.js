// LOVE REACTION
function handleLoveClick(questionId) {
    // Send an AJAX request to increment the love count
    $.ajax({
        type: 'POST',
        url: '{% url "increment_love_count" %}',  // Replace with your backend URL
        data: {
            'question_id': questionId
        },
        success: function(response) {
            // Update the love count button text with the new value
            $('#loveBtn' + questionId).text(response.love_count);
        },
        error: function(xhr, status, error) {
            console.error(xhr.responseText);
        }
    });
}