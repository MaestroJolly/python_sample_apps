$(document).ready(function () {
    var cardNo, exMonth, exYear, cvv, pin, cardAmount, errorOne, errorTwo, inputToken, tokenAmount ;




    $('#card_charge').click(function (event) {
        event.preventDefault();

        cardNo = $('#cardNo').val();
        exMonth = $('#exMonth').val();
        exYear = $('#exYear').val();
        cvv = $('#cvv').val();
        pin = $('#pin').val();
        cardAmount = $('#cardAmount').val();
        errorOne = $('.errorOne');
        errorTwo = $('.errorTwo');

        cardNo = cardNo.replace(/\s/g, '');
        exMonthVal = (exMonth) == '1' ? '01' : (exMonth) == '2' ? '02' : (exMonth) == '3' ? '03' : (exMonth) == '4' ? '04' : (exMonth) == '5' ? '05' : (exMonth) == '6' ? '06' : (exMonth) == '7' ? '07' : (exMonth) == '8' ? '08' : (exMonth) == '9' ? '09' : exMonth;

        if (cardNo.length < 1 || exMonthVal.length < 1 || exYear.length < 1 || cvv.length < 1 || pin.length < 1 || cardAmount.length < 1) {
            errorOne.text("Input Cannot be empty");
            errorOne.toggleClass("hide");
        } else {
            $.ajax({
                url: "/preauth/card_charge/",
                type: "POST",
                data: { 'cardNo': cardNo, 'exMonth': exMonth, 'exYear': exYear, 'cvv': cvv, 'pin': pin, 'cardAmount': cardAmount, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
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

    $('#preauth_charge').click(function (event) {
        event.preventDefault();

        inputToken = $('#inputToken').val();
        tokenAmount = $('#tokenAmount').val();

        if (inputToken.length < 1 || tokenAmount.length < 1) {
            errorTwo.text("Input Cannot be empty");
            errorTwo.toggleClass("hide");
        } else {
            $.ajax({
                url: "/preauth/preauth_charge/",
                type: "POST",
                data: { 'inputToken': inputToken, 'tokenAmount': tokenAmount, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
                success: function (data) {
                    $('#response').html(JSON.stringify(data, undefined, 2))
                },
                error: function (error) {
                    console.log(error)
                }
            });
        }
    })

    $('#preauth_capture').click(function (event) {
        event.preventDefault();

        flwRef = $('#flwRef').val();

        if (inputToken.length < 1) {
            errorThree.text("Input Cannot be empty");
            errorThree.toggleClass("hide");
        } else {
            $.ajax({
                url: "/preauth/preauth_capture/",
                type: "POST",
                data: { 'flwRef': flwRef, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
                success: function (data) {
                    $('#response').html(JSON.stringify(data, undefined, 2))
                },
                error: function (error) {
                    console.log(error)
                }
            });
        }
    })
    
});
