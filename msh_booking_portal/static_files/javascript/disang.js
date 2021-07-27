const user_input = $("#user-input")
// const user_input_date = $("#user-input-date")
const forms_div = $('#replaceable-content')
const endpoint = '/hab/view/disang/'
const delay_by_in_ms = 0
let scheduled_function = false

let ajax_call = function (endpoint, request_parameters) {
    $.getJSON(endpoint, request_parameters)
        .done(response => {
            forms_div.promise().then(() => {    
                forms_div.html(response['html_from_view'])  
            })
        })
}


user_input.on('keyup', function () {

    const request_parameters = {
        q: $(this).val() 
    }

    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})

// user_input_date.on('keyup', function () {

//     const request_parameters = {
//         q: $(this).val() 
//     }

//     if (scheduled_function) {
//         clearTimeout(scheduled_function)
//     }

//     scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
// })