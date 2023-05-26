const id = JSON.parse(document.getElementById('json-username').textContent);
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);

const socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + id
    + '/'
);

socket.onopen = function(e){
    console.log("CONNECTION ESTABLISHED");
}

socket.onclose = function(e){
    console.log("CONNECTION LOST");
}

socket.onerror = function(e){
    console.log("ERROR OCCURRED");
}



socket.onmessage = function(e){
    const data = JSON.parse(e.data);
    if(data.username === message_username){
        document.querySelector('#chat-body').innerHTML += `<tr>
                                                                <td></td>
                                                                <td>
                                                                    <p class="bg-primary p-2 mt-2 mr-5 shadow-sm text-white float-right rounded">${data.message}</p>
                                                                </td>
                                                                <td>
                                                                    <p class="text-right"><small class="p-1 shadow-sm">${formatTimestamp(data.timestamp)}</small>&nbsp; <i class="bi bi-clock-fill"></i></p>
                                                                </td>
                                                            </tr>`;
    } else {
        document.querySelector('#chat-body').innerHTML += `<tr>
                                                                <td>
                                                                    <p class="btn btn-secondary btn-rounded">${data.message}</p>
                                                                </td>
                                                                <td></td>
                                                                <td>
                                                                    <p class="text-left"><small class="p-1 shadow-sm">${formatTimestamp(data.timestamp)}</small>&nbsp; <i class="bi bi-clock-fill"></i></p>
                                                                </td>
                                                            </tr>`;
    }
};

// Format the timestamp in the desired format
function formatTimestamp(timestamp) {
    const date = new Date(timestamp);
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    return `${hours}:${minutes}`;
}

document.querySelector('#chat-message-submit').onclick = function(e){
    const message_input = document.querySelector('#message_input');
    const message = message_input.value;
    const timestamp = new Date().toISOString(); // Get the current timestamp

    socket.send(JSON.stringify({
        'message': message,
        'username': message_username,
        'timestamp': timestamp, // Include the timestamp in the data
    }));

    message_input.value = '';
};



document.addEventListener('DOMContentLoaded', function() {
  var scrollDiv = document.querySelector('.message-table-scroll');

  // Scroll to bottom function
  function scrollToBottom() {
    scrollDiv.scrollTop = scrollDiv.scrollHeight;
  }

  // Scroll to bottom on initial load
  setTimeout(function() {
    requestAnimationFrame(scrollToBottom);
  }, 0);

  // Scroll to bottom on page resize
  window.addEventListener('resize', function() {
    setTimeout(function() {
      requestAnimationFrame(scrollToBottom);
    }, 0);
  });

  // Scroll to bottom when new content is added
  var observer = new MutationObserver(function() {
    setTimeout(function() {
      requestAnimationFrame(scrollToBottom);
    }, 0);
  });

  observer.observe(scrollDiv, { childList: true });
});





           function toggleDarkMode() {
            var element = document.body;
            element.classList.toggle("dark-mode");

            // Store the dark mode preference in local storage
            var isDarkModeEnabled = element.classList.contains("dark-mode");
            localStorage.setItem("darkModeEnabled", isDarkModeEnabled);
        }

        // Check if dark mode preference is stored in local storage
        var isDarkModeEnabled = localStorage.getItem("darkModeEnabled");
        if (isDarkModeEnabled === "true") {
            document.body.classList.add("dark-mode");
        }




