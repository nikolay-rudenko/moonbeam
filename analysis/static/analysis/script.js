const btn_dark = document.querySelector(".btn-toggle-dark");
const btn_white = document.querySelector(".btn-toggle-white");


btn_white.addEventListener("click", function () {
  document.body.classList.toggle("white-theme");
});

btn_dark.addEventListener("click", function () {
  document.body.classList.toggle("dark-theme");
});