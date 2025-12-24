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

  // Default to Dark Mode if no preference is saved, or if it is explicitly 'dark'
  // Only set Light Mode if explicitly saved as 'light'
  if (savedTheme === "light") {
    setTheme("light");
  } else {
    setTheme("dark");
  }

  // 2. Toggle on click
  if (btn) {
    btn.addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme");
      // If current is 'light', switch to 'dark', otherwise 'light'
      const newTheme = current === "light" ? "dark" : "light";
      setTheme(newTheme);
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