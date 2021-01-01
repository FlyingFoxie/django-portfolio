/*
let birdForm = document.querySelectorAll(".bird-form")
let container = document.querySelector("#form-container")
let addButton = document.querySelector("#add-form")
let totalForms = document.querySelector("#id_form-TOTAL_FORMS")

let formNum = birdForm.length-1 //Get the number of the last form on the page with zero-based indexing
var blankform = formNum
addButton.addEventListener('click', addForm)

function addForm(e){
    e.preventDefault()

    let newForm = birdForm[blankform].cloneNode(true) //Clone the bird form
    let formRegex = RegExp(`form-(\\d){1}-`,'g') //Regex to find all instances of the form number

    formNum++ //Increment the form number
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`) //Update the new form to have the correct form number
    container.insertBefore(newForm, addButton) //Insert the new form at the end of the list of forms
    
    totalForms.setAttribute('value', `${formNum+1}`) //Increment the number of total forms in the form management
}*/

$('#add_more').click(function() {
    var form_idx = $('#id_education-TOTAL_FORMS').val();
    $('#form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx));
    $('#id_education-TOTAL_FORMS').val(parseInt(form_idx) + 1);
})

$('#add_more_skill').click(function() {
    var form_idx_skill = $('#id_skill-TOTAL_FORMS').val();
    $('#form_set_skill').append($('#empty_form_skill').html().replace(/__prefix__/g, form_idx_skill));
    $('#id_skill-TOTAL_FORMS').val(parseInt(form_idx_skill) + 1);
})

$('#add_more_exp').click(function() {
    var form_idx_exp = $('#id_experience-TOTAL_FORMS').val();
    $('#form_set_experience').append($('#empty_form_exp').html().replace(/__prefix__/g, form_idx_exp));
    $('#id_experience-TOTAL_FORMS').val(parseInt(form_idx_exp) + 1);
})
