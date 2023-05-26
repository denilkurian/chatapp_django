
   // Function to toggle dark mode
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





