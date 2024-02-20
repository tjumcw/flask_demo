$(document).ready(function (){

    $("#register_button").on('click', registerUser)
    function registerUser() {
        var username = $('#username').val();
        var password = $('#password').val();

        if (username.trim().length === 0 || password.trim().length === 0) {
            messageBox.showError("请输入必填参数");
            return;
        }

        var data = {
            'username': username,
            'password': password
        };

        $.ajax({
            type: 'POST',
            url: '/users/api/add',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function(response) {
                alert(response.message);  // or handle success in your preferred way
            },
            error: function(error) {
                var errorMessage = error.responseJSON ? error.responseJSON.error : 'Unknown error';
                $('#error-message').text(errorMessage);
            }
        });
    }
})