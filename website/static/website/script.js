// Typing Effect
const words = ["Modern Websites", "Django Applications", "Business Solutions"];
let i = 0;
let j = 0;
let currentWord = "";
let isDeleting = false;

function type() {
    if (i < words.length) {
        if (!isDeleting && j <= words[i].length) {
            currentWord = words[i].substring(0, j++);
        } else if (isDeleting && j >= 0) {
            currentWord = words[i].substring(0, j--);
        }

        document.querySelector(".typing").textContent = currentWord;

        if (j === words[i].length) isDeleting = true;
        if (j === 0 && isDeleting) {
            isDeleting = false;
            i++;
            if (i === words.length) i = 0;
        }
    }
    setTimeout(type, 100);
}
type();

// Counter Animation
const counters = document.querySelectorAll('.counter');
counters.forEach(counter => {
    const update = () => {
        const target = +counter.getAttribute('data-target');
        const count = +counter.innerText;
        const inc = target / 100;

        if (count < target) {
            counter.innerText = Math.ceil(count + inc);
            setTimeout(update, 20);
        } else {
            counter.innerText = target;
        }
    };
    update();
});