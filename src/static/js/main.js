// let signInBtn = document.getElementsByClassName('sign_in_btn')[0];
// let studentLabel = document.getElementById('you_are_student_label');
// let closeSignInFormBtn = document.getElementById('close_sign_in_form');
// let toRegisterForm = document.getElementById('to_register');
// let answer = true;
// let courseAnswer = true;

// signInBtn.onclick = function () {
//     let registerForm = document.getElementById('Sign_in');

//     registerForm.style.display = 'flex';
// }
// closeSignInFormBtn.onclick = function () {
//     let registerForm = document.getElementById('Sign_in');

//     registerForm.style.display = 'none';
// }

// toRegisterForm.onclick = function () {
//     let formList = document.getElementsByClassName('sign_form');

//     if (answer) {
//         toRegisterForm.innerHTML = '<i class="fas fa-sign-in-alt"></i>';
//         formList[0].style.transform = 'translate(-100%, 0)';
//         formList[1].style.transform = 'translate(-100%, 0)';
//         answer = false;
//     }
//     else {
//         toRegisterForm.innerHTML = '<i class="fas fa-user-plus"></i>';
//         formList[0].style.transform = 'translate(0, 0)';
//         formList[1].style.transform = 'translate(0, 0)';
//         answer = true;
//     }

// }

// studentLabel.onclick = function () {
//     let courseLabel = document.getElementById('label_course');

//     if (courseAnswer) {
//         courseLabel.style.display = 'flex';
//         courseAnswer = false;
//     }
//     else {
//         courseLabel.style.display = 'none';
//         courseAnswer = true;
//     }

// }

window.addEventListener('scroll', function() {
    let topMenu = document.getElementsByClassName('top_menu')[0];
    let menuLink = document.getElementsByClassName('menu_link');
    let signInBtn = document.getElementsByClassName('sign_in_btn')[0];

    if (window.scrollY >= 50){
        topMenu.style.height = '50px';
        topMenu.style.background = '#252424';

        signInBtn.style.padding = '8px 15px';
        signInBtn.style.fontSize = '14px';

        for (let i = 0; i < menuLink.length; i++) {
            menuLink[i].style.color = '#f8f8f8';
            menuLink[i].style.fontSize = '13px';
        };
    }
    else {
        topMenu.style.height = '80px';
        topMenu.style.background = '#f8f8f8';
        
        signInBtn.style.padding = '10px 15px';
        signInBtn.style.fontSize = '16px';

        for (let i = 0; i < menuLink.length; i++) {
            menuLink[i].style.color = '#252424';
            menuLink[i].style.fontSize = '14px';
        };
    }
})