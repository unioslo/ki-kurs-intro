// Canvas-compatible tabs with no-scroll behavior
document.addEventListener('DOMContentLoaded', function() {
    // Find all tab containers
    const tabContainers = document.querySelectorAll('.enhanceable_content.tabs');

    tabContainers.forEach(function(container) {
        const tabLinks = container.querySelectorAll('ul li a');
        const tabPanels = container.querySelectorAll(':scope > div[id]');

        // Hide all panels except the first one
        tabPanels.forEach(function(panel, index) {
            panel.style.display = index === 0 ? 'block' : 'none';
        });

        // Add active class to first tab
        if (tabLinks.length > 0) {
            tabLinks[0].classList.add('active-tab');
        }

        // Handle tab clicks
        tabLinks.forEach(function(link) {
            link.addEventListener('click', function(e) {
                e.preventDefault(); // Prevent scrolling

                // Get the target panel ID from the href
                const targetId = this.getAttribute('href').substring(1);
                const targetPanel = document.getElementById(targetId);

                if (targetPanel) {
                    // Hide all panels
                    tabPanels.forEach(function(panel) {
                        panel.style.display = 'none';
                    });

                    // Show target panel
                    targetPanel.style.display = 'block';

                    // Remove active class from all tabs
                    tabLinks.forEach(function(tabLink) {
                        tabLink.classList.remove('active-tab');
                    });

                    // Add active class to clicked tab
                    this.classList.add('active-tab');
                }
            });
        });
    });
});
