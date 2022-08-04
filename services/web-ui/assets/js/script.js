console.log('ok')
var register_name = document.getElementById('register_name')
var register_email_address = document.getElementById('register_email_address')
var register_password = document.getElementById('register_password')
var register_re_type = document.getElementById('register_re_type')
var button_register = document.getElementById('button_register')
var toast_register_container = document.getElementById('toast_register_container')

button_register.addEventListener('click', function() {
      console.log(register_name.value)

      // ajax object
      var xhr = new XMLHttpRequest()

      // check ajax ready
      xhr.onreadystatechange = function () {
            if( xhr.readyState == 4 && xhr.status == 200 ){
                  toast_register_container.innerHTML = xhr.responseText;
            }
      }

      // execute ajax
      xhr.open('GET', 'assets/ajax/toast-register.php', true)
      xhr.send();
})