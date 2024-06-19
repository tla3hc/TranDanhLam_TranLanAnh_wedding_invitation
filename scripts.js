document.addEventListener('DOMContentLoaded', () => {
    const rsvpButton = document.querySelector('.rsvp-button');

    rsvpButton.addEventListener('click', () => {
        rsvpButton.style.animation = 'bounce 0.5s';
        setTimeout(() => {
            alert('Thank you for your RSVP!');
            rsvpButton.style.animation = '';
        }, 500);
    });
});

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
    40% {transform: translateY(-30px);}
    60% {transform: translateY(-15px);}
}
