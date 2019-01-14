$(document).ready(function(){
    $('#list').click(function(){
        $.ajax({
            url: "/subscriptions/list_all/",
            type: "GET",
            data: { list: 'hello' },
            success: function (data) {
                // something here on success
                $('#response').text(JSON.stringify(data));
            },
            error: function (error) {
               // something here on error
               console.log(error)
            }
        });
    })

    $('#fetch_sub').click(function(){
        var subid = $('#sub_id').val();
        var subemail = $('#sub_email').val();
        $('#sub_id').val('');
        $('#sub_email').val('');
        $.ajax({
            url: "/subscriptions/fetch_sub/",
            type: "POST",
            data: { 'subid': subid, 'subemail': subemail, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()},
            success: function (data) {
                $('#response').html(JSON.stringify(data));
            },
            error: function (error) {
               console.log(error)
            }
        });
    })

    $('#cancel_sub').click(function(){
        var subid = $('#cancel_id').val();
        $('#cancel_id').val('');
        $.ajax({
            url: "/subscriptions/cancel_sub/",
            type: "POST",
            data: { 'subid': subid, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()},
            success: function (data) {
                $('#response').html(JSON.stringify(data));
                console.log(data);
            },
            error: function (error) {
               console.log(error)
            }
        });
    })

    $('#activate_sub').click(function(){
        var subid = $('#activate_id').val();
        $('#activate_id').val('');
        $.ajax({
            url: "/subscriptions/activate_sub/",
            type: "POST",
            data: { 'subid': subid, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()},
            success: function (data) {
                $('#response').html(JSON.stringify(data));
                console.log(data);
            },
            error: function (error) {
               console.log(error)
            }
        });
    })
    
});

// csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),