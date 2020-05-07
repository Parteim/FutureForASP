let signInBtn = document.getElementsByClassName('sign_in_btn')[0]
let studentLabel = document.getElementById('you_are_student_label')
let closeSignInFormBtn = document.getElementById('close_sign_in_form')
let toRegisterForm = document.getElementById('to_register')
let answer = true
let courseAnswer = true

signInBtn.onclick = function () {
    let registerForm = document.getElementById('Sign_in')

    registerForm.style.display = 'flex'
}
closeSignInFormBtn.onclick = function () {
    let registerForm = document.getElementById('Sign_in')

    registerForm.style.display = 'none'
}

toRegisterForm.onclick = function () {
    let formList = document.getElementsByClassName('sign_form')

    if (answer) {
        toRegisterForm.innerHTML = '<i class="fas fa-sign-in-alt"></i>'
        formList[0].style.transform = 'translate(-100%, 0)'
        formList[1].style.transform = 'translate(-100%, 0)'
        answer = false
    }
    else {
        toRegisterForm.innerHTML = '<i class="fas fa-user-plus"></i>'
        formList[0].style.transform = 'translate(0, 0)'
        formList[1].style.transform = 'translate(0, 0)'
        answer = true
    }

}

studentLabel.onclick = function () {
    let courseLabel = document.getElementById('label_course')

    if (courseAnswer) {
        courseLabel.style.display = 'flex'
        courseAnswer = false
    }
    else {
        courseLabel.style.display = 'none'
        courseAnswer = true
    }

}
