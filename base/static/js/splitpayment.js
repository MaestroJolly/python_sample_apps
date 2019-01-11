$(document).ready(function () {
    var subaccounts = [];
    // $('#select_bank').click(function () {
    //     $.ajax({
    //         url: "/splitpayment/list_banks/",
    //         type: "GET",
    //         data: { csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
    //         success: function (data) {
    //             // something here on success
    //             $('#response').html(JSON.stringify(data));
    //             console.log(data)
    //         },
    //         error: function (error) {
    //             // something here on error
    //             console.log(error)
    //         }
    //     });
    // })

    // $('#select_bank').on('change', function () {
    //     var accountbank = $('#select_bank').val();
    //     console.log(accountbank)
    //     if(this.value == '044') {
    //         alert('yass');
    //     }else {
    //         alert('oops')
    //     }
    // })

    $('#addSub').click(function () {
        
        var subId = $('#subId').val();
        var splitRatio = $('#splitRatio').val();
        var chargeType = $('#chargeType').val();
        var transCharge = $('#transCharge').val();

        
        subaccounts.push({ id: subId, transaction_split_ratio: splitRatio, transaction_charge_type: chargeType, transaction_charge: transCharge})
        
        tr = $('<tr/>');
        $('<td />', {html: subId}).appendTo(tr);
        $('<td />', {html: splitRatio}).appendTo(tr);
        $('<td />', {html: chargeType}).appendTo(tr);
        $('<td />', {html: transCharge}).appendTo(tr);
        tr.appendTo('tbody');

    })

    $('#pay').click(function () {
        var accountbank = $('#select_bank').val();
        var accountnumber = $('#accountnumber').val(); 
        // var cuurency = "NGN"; //$('#sub_email').val();
        // var amount = $('#amount').val();
        // var email = "test@test.com"; //$('#sub_email').val();
         
        $('#accountnumber').val('');
        console.log(subaccounts)
        $.ajax({
            url: "/splitpayment/pay/",
            type: "POST",
            data: { 'accountbank': accountbank, 'accountnumber': accountnumber, 'subaccounts': subaccounts, csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() },
            success: function (data) {
                $('#response').html(JSON.stringify(data));
                console.log(data)
            },
            error: function (error) {
                console.log(error)
            }
        });
    })

});

// csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),

// subaccounts:[
//     {
//     id:'RS_A5F40ED75898F4DCD04726EA52F1E1C1',
//     transaction_charge:"0.02",
//     transaction_charge_type:"percentage"
//     },
//     {
//     id:'RS_851DC6141A1EE19EB15D698D7850900F',
//     transaction_charge:"1500",
//     transaction_charge_type:"flat_subaccount"
//     },
//     {
//     id:'RS_120D3B88D9CE82CB1A599D610542EDFF',
//     transaction_charge:"3000",
//     subaccount_charge_type:"flat_subaccount"
//     }
//     ],