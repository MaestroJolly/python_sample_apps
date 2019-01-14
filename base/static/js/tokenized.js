$(document).ready(function () {

    $('#card_charge').click(function (event) {
        event.preventDefault();
        var cardNo = $('#cardNo').val();
        var exMonth = $('#exMonth').val();
        var exYear = $('#exYear').val();
        var cvv = $('#cvv').val();
        var pin = $('#pin').val();
        var cardAmount = $('#cardAmount').val();
        console.log("weyo")
        $.ajax({
            url: "/tokenized/card_charge/",
            type: "POST",
            data: { 'cardNo': cardNo, 'exMonth': exMonth, 'exYear': exYear, 'cvv': cvv, 'pin': pin, 'cardAmount': cardAmount, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
            success: function (data) {
                $('#response').html(JSON.stringify(data));
                console.log(data);
            },
            error: function (error) {
                console.log(error)
            }
        });
    })

    $('#token_charge').click(function (event) {
        event.preventDefault();
        var inputToken = $('#inputToken').val();
        var tokenAmount = $('#tokenAmount').val();

        $.ajax({
            url: "/tokenized/token_charge/",
            type: "POST",
            data: { 'inputToken': inputToken, 'tokenAmount': tokenAmount, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
            success: function (res) {
                $('#response').html(JSON.stringify(res));
                console.log(res);
            },
            error: function (error) {
                console.log(error)
            }
        });
    })
});
