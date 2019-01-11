$(document).ready(function(){
    var accountBankOptions, accountBankCode, accountNumber, accountName, singleTransferBtn, customerAccountNumber, singleAmount, accountNumberTwo, bulkLists, beneficiaryBtn, bulkTransferBtn, beneficiaryLists, accountNameTwo, bulkAmount, beneficiaryObjects, tr, accountBankOptionsTwo, accountBankCodeTwo, title, titleValue, errorOne, errorTwo, narration, narrationTwo;
    accountBankOptions = $('#accountBank');
    accountBankOptionsTwo = $('#accountBankTwo');
    accountNumber = $('#accountNumber');
    accountName = $('#accountName');
    accountNumberTwo = $('#accountNumberTwo');
    accountNameTwo = $('#accountNameTwo');
    bulkAmount = $('#bulkAmount');
    singleTransferBtn = $('#singleTransferBtn');
    bulkTransferBtn = $('#bulkTransferBtn');
    bulkLists = $('#bulkLists');
    narration = $('#narration');
    narrationTwo = $('#narrationTwo');
    beneficiaryLists = [];
    title = $('#title');
    beneficiaryBtn = $('#beneficiaryBtn');
    errorOne = $('.errorOne');
    errorTwo = $('.errorTwo');

    // single transfer beneficiary bank account on change event listener
    accountBankOptions.change(function(){
        if ($(this).val() === "Choose An Option"){
            return false;
        }else{
            accountBankCode = $(this).val();
        }
    });
    // bulk transfer beneficiaries bank account on change event listener
    accountBankOptionsTwo.change(function(){
        if ($(this).val() === "Choose An Option"){
            return false;
        }else{
            accountBankCodeTwo = $(this).val();
        }
    });
    // single transfer ajax request to resolve beneficiary account number on key event listener
    accountNumber.keyup(function(){
        var customerAccountNumber = $(this).val();
        $.ajax({
            url: "/transfer/resolve/",
            type: "POST",
            data: { 
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'recipientaccount': customerAccountNumber.toString(),
                'destbankcode': accountBankCode.toString(),
            },
            success: function (res) {
                // something here on success
                if (res.data.data.responsecode === "00"){
                    $('#resMessage').css({color: 'blue'}).html(res.data.data.responsemessage);
                    accountName.val(res.data.data.accountname);
                }else{
                    $('#resMessage').css({color: 'red'}).html(res.data.data.responsemessage);
                }
            },
            error: function (error) {
               // something here on error
               console.log("error" + error)
            }
        });
    })
    // single transfer ajax request to initiate single transfer on click event listener
    singleTransferBtn.click(function(e){
        e.preventDefault();
        customerAccountNumber = accountNumber.val();
        singleAmount = $("#singleAmount").val();
        if(accountBankOptions.val() === "Choose an Option"){
            errorOne.text("Choose Your Bank");
            errorOne.toggleClass("hide");
        }
        else if (customerAccountNumber === "" || accountName.val() === "" || singleAmount === ""){
            errorOne.text("Input Cannot be empty");
            errorOne.toggleClass("hide");
        }else{
            $.ajax({
                url: "/transfer/single-transfer/",
                type: "POST",
                data: { 
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                    "account_bank": customerAccountNumber.toString(),
                    "account_code": accountBankCode.toString(),
                    "account_name": accountName.val(),
                    "narration": narration.val(),
                    "reference": "Tr-"+Date.now(),
                    "single_amount": singleAmount
                },
                success: function (res) {
                    // something here on success
                    $('#response').html(JSON.stringify(res));
                },
                error: function (error) {
                // something here on error
                console.log("error" + error)
                }
            });
        }
    })
    // bulk transfer ajax request to resolve beneficiaries account number on key event listener
    accountNumberTwo.keyup(function(){
        customerValueTwo = accountNumberTwo.val();
        $.ajax({
            url: "/transfer/resolve/",
            type: "POST",
            data: { 
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'recipientaccount': customerValueTwo.toString(),
                'destbankcode': accountBankCodeTwo.toString(),
            },
            success: function (res) {
                // something here on success
                if (res.data.data.responsecode === "00"){
                    $('#resMessageTwo').css({color: 'blue'}).html(res.data.data.responsemessage);
                    accountNameTwo.val(res.data.data.accountname);
                }else{
                    $('#resMessageTwo').css({color: 'red'}).html(res.data.data.responsemessage);
                }
            },
            error: function (error) {
               // something here on error
               console.log("error" + error)
            }
        });
    })
    // bulk transfer ajax request to add list of beneficiaries on click event listener
    beneficiaryBtn.click(function(e){
        e.preventDefault();
        customerAccountNumber = accountNameTwo.val();
        bulkAmount = $('#bulkAmount').val(); 
        if(accountBankOptionsTwo.val() === "Choose an Option"){
            errorTwo.text("Choose Your Bank");
            errorTwo.toggleClass("hide");
        }
        else if (customerAccountNumber === "" || accountNumberTwo.val() === "" || title.val() === "" || bulkAmount === ""){
            errorTwo.text("Input Cannot be empty");
            errorTwo.toggleClass("hide");
        }else{
            var tbody = document.querySelector('tbody');
            beneficiaryObjects = {
                "Bank": accountBankCodeTwo.toString(),
                "Account Number": customerValueTwo,
                "Currency":"NGN",
                "Narration": narrationTwo.val(),
                "Amount": bulkAmount,
                "reference": "Tr-"+Date.now()
            }
            titleValue = title.val();
            beneficiaryLists.push(beneficiaryObjects);
            tr = $('<tr>');
            $('<td />', {html: customerValueTwo}).appendTo(tr);
            $('<td />', {html: customerAccountNumber}).appendTo(tr);
            $('<td />', {html: bulkAmount}).appendTo(tr);
            tr.appendTo(tbody);
            accountNumberTwo.val("");
            accountNameTwo.val("");
            narrationTwo.val("");
            $('#bulkAmount').val(""); 
        }
    })
    // bulk transfer ajax request to initiate bulk transfer on click event listener
    bulkTransferBtn.click(function(){
        console.log(beneficiaryLists);
        $.ajax({
            url: "/transfer/bulk-transfer/",
            type: "POST",
            data: { 
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                "recipientslist": JSON.stringify(beneficiaryLists),
                "title": titleValue,
            },
            success: function (res) {
                // something here on success
                $('#response').html(JSON.stringify(res));
                console.log(res);
            },
            error: function (error) {
            // something here on error
            console.log("error" + error)
            }
        });
    })
});