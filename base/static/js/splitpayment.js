$(document).ready(function () {
    var accountbank, accountnumber, amount, phonenumber, subaccounts, subaccountsInfo, errorOne, errorTwo;

    subaccountsInfo = [];
    errorOne = $('.errorOne');
    errorTwo = $('.errorTwo');

    $('#addSub').click(function (event) {
        event.preventDefault();
        var subId = $('#subId').val();
        var splitRatio = $('#splitRatio').val();
        var chargeType = $('#chargeType').val();
        var transCharge = $('#transCharge').val();

        if (subId === "") {
            errorOne.text("Input Cannot be empty");
            errorOne.toggleClass("hide");
        } else if (splitRatio === "") {
            subaccounts = {
                id: subId,
                transaction_charge_type: chargeType,
                transaction_charge: transCharge
            }
            subaccountsInfo.push(subaccounts);

            tr = $('<tr/>');
            $('<td />', { html: subId }).appendTo(tr);
            $('<td />', { html: splitRatio }).appendTo(tr);
            $('<td />', { html: chargeType }).appendTo(tr);
            $('<td />', { html: transCharge }).appendTo(tr);
            tr.appendTo('tbody');
        } else if (splitRatio === "" || chargeType === "" || transCharge === "") {
            subaccounts = {
                id: subId
            }
            subaccountsInfo.push(subaccounts);

            tr = $('<tr/>');
            $('<td />', { html: subId }).appendTo(tr);
            $('<td />', { html: splitRatio }).appendTo(tr);
            $('<td />', { html: chargeType }).appendTo(tr);
            $('<td />', { html: transCharge }).appendTo(tr);
            tr.appendTo('tbody');
        } else {
            subaccounts = {
                id: subId,
                transaction_split_ratio: splitRatio,
                transaction_charge_type: chargeType,
                transaction_charge: transCharge
            }
            subaccountsInfo.push(subaccounts);
            
            tr = $('<tr/>');
            $('<td />', { html: subId }).appendTo(tr);
            $('<td />', { html: splitRatio }).appendTo(tr);
            $('<td />', { html: chargeType }).appendTo(tr);
            $('<td />', { html: transCharge }).appendTo(tr);
            tr.appendTo('tbody');
        }
        console.log(subaccounts)
    })

    $('#pay').click(function (event) {
        event.preventDefault();
        accountbank = $('#select_bank').val();
        accountnumber = $('#accountnumber').val();
        amount = $('#amount').val();
        phonenumber = $('#phonenumber').val();

        if (accountbank === "Choose a Bank") {
            errorTwo.text("Choose Your Bank");
            errorTwo.toggleClass("hide");
        } else if (accountbank === "" || accountnumber === "" || amount === "" || phonenumber === "") {
            errorTwo.text("Input Cannot be empty");
            errorTwo.toggleClass("hide");
        } else {
            $.ajax({
                url: "/splitpayment/pay/",
                type: "POST",
                data: { 'accountbank': accountbank, 'accountnumber': accountnumber, 'amount': amount, 'subaccounts': JSON.stringify(subaccountsInfo), csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
                success: function (data) {
                    $('#response').html(JSON.stringify(data, undefined, 2));
                    console.log(data)
                },
                error: function (error) {
                    console.log(error)
                }
            });
        }
    })

});
