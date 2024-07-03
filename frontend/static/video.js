document.addEventListener('DOMContentLoaded', (event) => {
    const videoPlayer = document.getElementById('videoPlayer');
    const commentInput = document.getElementById('commentInput');
    const addCommentButton = document.getElementById('addCommentButton');
    const commentsList = document.getElementById('commentsList');
    const socket = io('http://' + document.domain + ':' + location.port);
    

    // Fetch initial comments
    fetch('/comments')
        .then(response => response.json())
        .then(comments => {
            comments.forEach(comment => {
                addComment(comment.text, comment.timestamp);
            });
        });

    addCommentButton.addEventListener('click', () => {
        const commentText = commentInput.value;
        const timestamp = new Date().toISOString();  // Capture current date and time
        console.log('Timestamp:', timestamp);  // Debugging line to check timestamp
        const comment = { text: commentText, timestamp: timestamp };
        socket.emit('addComment', comment);
        commentInput.value = '';
    });

    socket.on('newComment', (comment) => {
        addComment(comment.text, comment.timestamp);
    });

    function addComment(text, timestamp) {
        const commentElement = document.createElement('div');
        commentElement.className = 'list-group-item';
        commentElement.innerHTML = `
            <span>${text}</span>
            <span class="comment-timestamp comment-time">${new Date(timestamp).toLocaleString()}</span>
        `;
        commentsList.appendChild(commentElement);
    }
});
