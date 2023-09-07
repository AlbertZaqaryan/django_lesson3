document.addEventListener('DOMContentLoaded', function () {
    const filterButtons = document.querySelectorAll('.filter button');
    const images = document.querySelectorAll('.image');

    filterButtons.forEach(button => {
        button.addEventListener('click', function () {
            const category = button.dataset.category;

       
            if (category === 'all') {
                images.forEach(image => {
                    image.style.display = 'block';
                });
            } else {
                images.forEach(image => {
                    const imageCategory = image.dataset.category;
                    if (imageCategory === category) {
                        image.style.display = 'block';
                       
                    } else {
                        image.style.display = 'none';
                       

                    }
                });
            }
        });
    });
});
