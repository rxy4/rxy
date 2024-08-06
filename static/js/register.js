$(function() {
    function bindCaptchaBtnClick() {
        $("#captcha-btn").click(function(event) {
            let $this = $(this);
            let email = $("input[name='email']").val();
            if (!email) {
                alert("请先输入邮箱!");
                return;
            }
            $this.off('click'); // 正确地解除点击事件的绑定
            $.ajax('/zlauth/captcha?email='+email,{
                method:'GET',
                success:function (result){
                    if(result['code']==200){alert("验证码发送成功!");}
                    else{alert(result['message']);}
                },
                fail:function (error){console.log(error);}
            })
            let countdown = 60;
            let timer = setInterval(function() {
                if (countdown <= 0) {
                    $this.text('获取验证码');
                    clearInterval(timer);
                    bindCaptchaBtnClick(); // 重新绑定点击事件
                } else {
                    $this.text(countdown + "s");
                    countdown--;
                }
            }, 1000);
        });
    }

    bindCaptchaBtnClick();
});
