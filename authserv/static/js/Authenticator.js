if (typeof String.prototype.endsWith !== 'function') {
    String.prototype.endsWith = function(suffix) {
        return this.indexOf(suffix, this.length - suffix.length) !== -1;
    };
}

if(!document.referrer || document.referrer.endsWith("register/")) {
    console.log("No Referrer Set! Disabling login button...");
    $("#loginBtn").attr("disabled", "");
} else {
    $("#referrer-label").text("You will be redirected back to your original page.").css({color: 'green'});
    $("#referrer-alert").addClass("alert").addClass("alert-info");
}

function interpretLogin(data) {
    console.log(data.message);
    if(data.message === "Authentication Successful.") {
        $.cookie("auth-token", data.auth_token, {domain: '.kronosad.com', path: '/'});
        $.cookie("auth-username", data.username, {domain: '.kronosad.com', path: '/', expires: 10});
        window.location = document.referrer;
    } else {
        $("#welcome-label").text("Authentication Failed!").css({color: 'red'});
        $("#alert-field").addClass("alert-danger");
    }
}

function interpretRegistration(data) {
    console.log(data);
    if(data.username) {
        $("#welcome-label").text("Registration complete.").css({color: 'green'});
        if(data.username !== $("#username").val()) {
            alert("Warning: The registered username was different than you typed.\nRegistered as: \"" + data.username + "\"\nSpaces are automatically removed from your username.");
        }
        window.location = document.referrer;
    } else {
        $("#welcome-label").text(data.message).css({color: 'red'});
        $("#alert-field").addClass("alert").addClass("alert-danger");
    }
}

function login() {
    $("#welcome-label").text("Logging in...");
    $.ajax({
        url: '../api/login/',
        data: {
            username: $("#username").val(),
            password: $("#password").val()
        },
        type: 'POST',
        crossDomain: true,
        success: function(data) { interpretLogin(data); },
        error: function() { alert("Error contacting authentication server!"); }
    });
}

function register() {
    console.log("Performing registration...");
    $("#welcome-label").text("Registering...");
    $.ajax({
        url: '../api/create_user/',
        data: {
            username: $("#username").val(),
            password: $("#password").val()
        },
        type: 'POST',
        crossDomain: true,
        success: function(data) { interpretRegistration(data); },
        error: function() { alert("Error contacting authentication server!"); }
    });
}

function logout() {
    $.removeCookie('auth-token', {domain: '.kronosad.com', path: '/'});
    $.removeCookie('auth-username', {domain: '.kronosad.com', path: '/', expires: 10});

    $("#welcome-label").text("All cookies cleared! You're now logged out.");
}
