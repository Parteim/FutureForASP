let showCreatePostBtn = document.getElementById('create_post_btn')
let createPostForm = document.getElementById('Create_post')
let closeCreatePostFormBtn = document.getElementById('close_create_post_form')

showCreatePostBtn.onclick = function () {
    createPostForm.style.display = 'flex'
}

closeCreatePostFormBtn.onclick = function () {
    createPostForm.style.display = 'none'
}

