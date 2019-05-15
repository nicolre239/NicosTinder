$(document).ready(function () {
    var regForm = $('#register_form');
    var loginForm = $('#login_form');
    var changeForm = $('#change_form')


    $('#id_button_serch_pairs').click(function (e) {
        e.preventDefault();
        window.location.pathname="/search_pairs/" + $('#id_button_serch_pairs').attr('data-target') + "/"
    })

    $('#id_button_change').click(function(e){
        e.preventDefault();
        window.location.pathname="/profile_change/" + $('#id_button_change').attr('data-target') + "/";
    });

    $('#id_button_likes').click(function(e){
        e.preventDefault();
        window.location.pathname="/likes/" + $('#id_button_likes').attr('data-target') + "/";
    });

    $('#id_button_profile_back').click(function(e){
        e.preventDefault();
        window.location.pathname="../profile/" + $('#id_button_profile_back').attr('data-target') + "/";
    });

    $('#id_delete_button').click(function (e) {
        e.preventDefault();
        sendDeleteRequest($('#id_delete_button').attr('data-target'), $('#id_delete_button').attr('data-user'));
    })

    regForm.on('submit', function (e) {
        e.preventDefault();
        if($('#id_answer').val().toString().toUpperCase() === "ИЮНЬ" && parseInt($('#id_age').val().toString()) > 17){
            console.log("agever passed");
            sendRegisterRequest();
        }
        else{
            alert("Кажется вам нет 18ти...");
        }
    })

    loginForm.on('submit', function (e) {
        e.preventDefault();
        sendLoginRequest();
    })

    changeForm.on('submit', function (e) {
        e.preventDefault();

        if ($('#id_age_from').val() > $('#id_age_to').val()) {
            alert("Неверно введены возрастные границы")
        }
        else {
            sendSaveRequest();
        }
    })

    function getHashCode(s) {
        var hash = 0, i, chr;
      if (s.length === 0) return hash;
      for (i = 0; i < s.length; i++) {
        chr   = s.charCodeAt(i);
        hash  = ((hash << 5) - hash) + chr;
        hash |= 0; // Convert to 32bit integer
      }
      return hash;
    }

    function continueToProfile(flag, user_id) {
        if (flag) {
            alert("Неверный e-mail или пароль");
        }
        else {
            window.location.pathname="/profile/" + user_id + "/";
        }
    }

    function sendDeleteRequest(match_id, user_id) {
        var data = {};

        data.match_id=match_id;
        data.user_id=user_id;

        var url = $('#id_delete_button').attr("action");
        var csrf_token = $('#id_delete_button [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function(data){
                alert("Пользователь успешно удален")
                window.location.pathname="/likes/" + user_id + "/";
                console.log("OK");
            },
            error: function(){
                console.log("ERROR");
            }
        });
    }

    function sendRegisterRequest(){
        var data = {};
        var emailField = $('#id_email');
        var nameField = $('#id_name');
        var passwordField = $('#id_password');
        var sexField = $('input[name=gender]:checked');
        var ageField = $('#id_age');

        data.email=emailField.val();
        data.name=nameField.val();
        data.password=getHashCode(passwordField.val());
        data.sex = sexField.val();
        data.age = ageField.val();
        var url = regForm.attr("action");
        var csrf_token = $('#register_form [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var alreadyexsists = false;
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function(data){
                console.log("OK");
                alreadyexsists = data.already_exsists;
                console.log(alreadyexsists);
                continueToProfile(alreadyexsists, data.user_id)
            },
            error: function(){
                console.log("ERROR");
            }
        });
    }

    function sendLoginRequest(){
        var data = {};
        var emailField = $('#id_email');
        var passwordField = $('#id_password');
        data.email=emailField.val();
        data.password=getHashCode(passwordField.val());
        console.log(data.password);
        var url = loginForm.attr("action");
        var csrf_token = $('#login_form [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var login_pass = true;
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function(data){
                console.log("OKaaay");
                login_pass = data.login_pass;
                console.log(!login_pass);
                continueToProfile(!login_pass, data.user_id)
            },
            error: function(){
                console.log("ERROR");
            }
        });
    }

    function sendSaveRequest(){
        console.log("change");
        var data = {};
        var nameField = $('#id_name');
        var descriptionField = $('#id_description');
        var ageFromField = $('#id_age_from');
        var ageToField = $('#id_age_to');
        var sexFindField = $('#id_sex_find');

        data.name=nameField.val();
        data.description=descriptionField.val();
        data.ageFrom = ageFromField.val();
        data.ageTo = ageToField.val();
        data.sexFind = sexFindField.val();

        data.id = $('#id_button_profile_back').attr('data-target');
        var url = changeForm.attr("action");

        var csrf_token = $('#change_form [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        console.log("before request");
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function(data){
                alert("Успешно сохранено!");
                console.log("OK");
            },
            error: function(){
                alert("ЧТО-ТО ПОШЛО НЕ ТАК, КОГДА Я РЕШИЛ УЧИТЬСЯ НА ПРОГЕРА");
                console.log("ERROR");
            }
        });
    }

});