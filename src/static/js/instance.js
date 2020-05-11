let revealSection = document.getElementById('Reveal_img');
let revealImage = document.getElementById('reveal_image');
let imagesList = document.querySelectorAll('.instance_image');

imagesList.forEach(function(element, key) {
    element.onclick = function revealImageFunc() {

        revealSection.style.width = '100%';
        revealSection.style.height = '100%';

        revealImage.src = this.src;
    }

})

revealSection.onclick = function () {
    revealSection.style.width = '0';
    revealSection.style.height = '0';

    revealImage.src = '';
}
