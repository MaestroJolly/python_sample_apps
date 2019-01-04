$(document).ready(function(){
    $('#list-all').click(function(){
        // var response = "{{res2}}"
        // $('#response').html(response);
        $.ajax({
            url: "/subscriptions",
            type: "GET",
            data: { csrfmiddlewaretoken: '{{ csrf_token }}' },
            success: function (data) {
                // something here on success
                $('#response').html("response");
            },
            error: function () {
               // something here on error
            }
        });
    })
    
});