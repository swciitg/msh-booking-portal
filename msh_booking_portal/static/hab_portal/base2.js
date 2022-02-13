var HostelVar = document.baseURI
var endpoint = HostelVar
const forms_div = $('#replaceable-content')

var ajax_filter = function() {
    var user_input = $('#user-input').val();
    var sortid = $('#sort').val();
    $.ajax({
        url: endpoint,
        type: 'GET',
        data: {
            'user-input': user_input,
            'sortid': sortid,
        },
        dataType: 'json',
        success: function(data) {
            forms_div.promise().then(()=>{
                forms_div.html(data['html_from_view'])
            })
        }
    });
};

$('#sort').on('change', ajax_filter);
$('#user-input').on('keyup', ajax_filter);