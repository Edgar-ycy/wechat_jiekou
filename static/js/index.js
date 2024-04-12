function click(){
    var name=register_form.name.value;
    var passwd=register_form.passwd.value;
    var number=register_form.number.value;

    if (name==""){
        alert("请输入用户名！");
        register_form.username.focus();
        return;
    }
    else if (passwd==""){
        alert("请输入密码！");
        register_form.passwd.focus();
        return;
    }
    else if (number==""){
        alert("请输入数字！");
        register_form.number.focus();
        return;
    }
    else{
        document.register_form.submit();
    }


}


