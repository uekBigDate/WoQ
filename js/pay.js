//密码支付
$('.button').click(function () {
    $('.key').show();
    $('.button').hide();
});
let i = 0;
$(".keyboard .zf_ul li .zf_num").click(function(){
    if(i<6){
        $(".mm_box li").eq(i).addClass("point");
        $(".mm_box li").eq(i).attr("data",$(this).text());
        i++;
        if (i==6) {
            setTimeout(function(){
                let data = "";
                $(".mm_box li").each(function(){
                    data += $(this).attr("data");
                });
                window.open('yxj_success.html');
                console.log("支付成功"+data);
            },100);
        };
    }
});