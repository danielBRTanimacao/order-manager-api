const languageSelect = document.getElementById("changeLanguage");

languageSelect.addEventListener("change", (event) => {
    const selectedLanguage = event.target.value;

    document.querySelectorAll("[data-lang-pt]").forEach((element) => {
        element.textContent = element.getAttribute(
            `data-lang-${selectedLanguage}`
        );
    });
});

function copy(text) {
    navigator.clipboard.writeText(text);
    const textSuccess = document.querySelector("div#hiddeText");
    textSuccess.classList.remove("hidden");
    textSuccess.classList.add("show");
    setTimeout(function () {
        setTimeout(function () {
            textSuccess.classList.remove("show");
            textSuccess.classList.add("hidden");
        }, 1000);
    }, 1000);
}
