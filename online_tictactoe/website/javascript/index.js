document.addEventListener('DOMContentLoaded', function() {
    const switchThemeBtn = document.querySelector('.switch-theme-btn');
    const switchLanguageBtn = document.querySelector('.switch-language-btn');
    const body = document.body;
    const switchThemeBtnText = switchThemeBtn.querySelector('.menu-text');
    const switchLanguageBtnImg = switchLanguageBtn.querySelector('.language-flag');

    // Check the current theme
    const isDarkMode = body.classList.contains('dark-mode');

    // Set initial button text based on current theme
    switchThemeBtnText.textContent = isDarkMode ? "Switch to Light" : "Switch to Dark";

    // Switch theme on button click
    switchThemeBtn.addEventListener('click', function() {
        // Toggle dark mode
        body.classList.toggle('dark-mode');

        // Change button text based on the theme
        if (body.classList.contains('dark-mode')) {
            switchThemeBtnText.textContent = "Switch to Light";
        } else {
            switchThemeBtnText.textContent = "Switch to Dark";
        }
    });

    // Switch language/flag on button click
    switchLanguageBtn.addEventListener('click', function() {
        // Only change the flag, not the theme
        if (switchLanguageBtnImg.src.includes('united.svg')) {
            switchLanguageBtnImg.src = "../../../Assets/svgs/flags/france.svg";
            switchLanguageBtnImg.alt = "French flag icon";
        } else {
            switchLanguageBtnImg.src = "../../../Assets/svgs/flags/united.svg";
            switchLanguageBtnImg.alt = "United Kingdom flag icon";
        }
    });
});
