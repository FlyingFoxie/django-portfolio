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
