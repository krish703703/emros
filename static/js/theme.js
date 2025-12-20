// Theme Toggle Logic
(function () {
  const btn = document.getElementById("themeToggle");

  // Function to apply theme
  function setTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
    if (btn) {
      btn.setAttribute("aria-pressed", theme === "dark");
    }
  }

  // 1. Check for saved preference immediately
  const savedTheme = localStorage.getItem("theme");
  const systemDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

  if (savedTheme === "dark" || (!savedTheme && systemDark)) {
    setTheme("dark");
  } else {
    // Ensure button state is correct if light mode is active
    if (btn) btn.setAttribute("aria-pressed", "false");
  }

  // 2. Toggle on click
  if (btn) {
    btn.addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme");
      setTheme(current === "dark" ? "light" : "dark");
    });
  }
})();

// Mobile Menu Logic
(function () {
  const toggle = document.getElementById("menuToggle");
  const nav = document.getElementById("primaryNav");

  if (!toggle || !nav) return;

  toggle.addEventListener("click", () => {
    nav.classList.toggle("open");
  });
})();