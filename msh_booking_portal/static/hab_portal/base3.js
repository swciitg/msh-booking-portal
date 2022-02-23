var HostelVar = document.baseURI
var endpoint = HostelVar
var endpoint_again = 'download_excel/4/none/'
const forms_div = $('#replaceable-content')

var ajax_filter = function() {
    var user_input = $('#user-input').val();
    var sortid = $('#sort').val();
    var dateOfArrival = $('#date_of_arrival').val();
    $.ajax({
        url: endpoint,
        type: 'GET',
        data: {
            'user-input': user_input,
            'sortid': sortid,
            'dateOfArrival': dateOfArrival,
        },
        dataType: 'json',
        success: function(data) {
            forms_div.promise().then(()=>{
                forms_div.html(data['html_from_view'])
            })
        }
    });
};

var download_excel = function() {
    var roll = $('#user-input').val();
    var sort = $('#sort').val();
    var date = $('#date_of_arrival').val();
    if (roll){
        roll=roll;
    }else{
        roll='none';
    }

    if(date){
        date=date;
    }else{
        date='none';
    }

    location.href = "../download_excel/4/none/"+roll+"/"+sort+"/"+date+"/";
};

$('#sort').on('change', ajax_filter);
$('#user-input').on('keyup', ajax_filter);
$('#date_of_arrival').on('change', ajax_filter);
$('#download').on('click', download_excel);