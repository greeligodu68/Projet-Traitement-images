const slider = document.querySelector('.slideshow-container');
let holding = false;
let startX;
let scrollLeft;

slider.addEventListener('mousedown', e => {
    if (e.button !== 0) return; 
    if (isTextSelected()) return; 

    holding = true;
    slider.classList.add('active');
    startX = e.pageX - slider.offsetLeft;
    scrollLeft = slider.scrollLeft;
});

slider.addEventListener('mousemove', e => {
    if (!holding) return;
    e.preventDefault();
    const x = e.pageX - slider.offsetLeft;
    const walk = (x - startX) ; 
    slider.scrollLeft = scrollLeft - walk;
});

slider.addEventListener('mouseup', () => {
    holding = false;
});

slider.addEventListener('mouseleave', () => {
    holding = false;
});

function isTextSelected() {
    const selection = window.getSelection();
    return selection.type === "Range"; // Vérifie si du texte est sélectionné
}




