$(document).ready(function () {
    var errorOne, errorTwo, errorThree;

    errorOne = $('.errorOne');
    errorTwo = $('.errorTwo');
    errorThree = $('.errorThree');

    // lists all subscriptions
    $('#list').click(function () {
        $.ajax({
            url: "/subscriptions/list_all/",
            type: "GET",
            data: { csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
            success: function (data) {
                // something here on success
                $('#response').text(JSON.stringify(data, undefined, 2));
            },
            error: function (error) {
                // something here on error
                console.log(error)
            }
        });
    })

    // fetches a particular (set of) subscriptions by id or user email
    $('#fetch_sub').click(function (event) {
        event.preventDefault();

        var subid = $('#sub_id').val();
        var subemail = $('#sub_email').val();

        if (subid === "" || subemail === "") {
            errorOne.text("Input Cannot be empty");
            errorOne.toggleClass("hide");
        } else {
            $.ajax({
                url: "/subscriptions/fetch_sub/",
                type: "POST",
                data: { 'subid': subid, 'subemail': subemail, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
                success: function (data) {
                    $('#response').html(JSON.stringify(data, undefined, 2));
                },
                error: function (error) {
                    console.log(error)
                }
            });
        }
    })

    // cancels a subscription
    $('#cancel_sub').click(function (event) {
        event.preventDefault();

        var subid = $('#cancel_id').val();

        if (subid === "") {
            errorTwo.text("Input Cannot be empty");
            errorTwo.toggleClass("hide");
        } else {
            $.ajax({
                url: "/subscriptions/cancel_sub/",
                type: "POST",
                data: { 'subid': subid, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
                success: function (data) {
                    $('#response').html(JSON.stringify(data, undefined, 2));
                },
                error: function (error) {
                    console.log(error)
                }
            });
        }
    })

    // activates a subscription
    $('#activate_sub').click(function (event) {
        event.preventDefault();
        var subid = $('#activate_id').val();

        if (subid === "") {
            errorThree.text("Input Cannot be empty");
            errorThree.toggleClass("hide");
        } else {
            $.ajax({
                url: "/subscriptions/activate_sub/",
                type: "POST",
                data: { 'subid': subid, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
                success: function (data) {
                    $('#response').html(JSON.stringify(data, undefined, 2));
                    console.log(data);
                },
                error: function (error) {
                    console.log(error)
                }
            });
        }
    })

});
