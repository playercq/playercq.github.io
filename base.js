// 新开传奇网站 - 交互脚本
(function(){
    "use strict";

    // 年份
    var yr = document.getElementById('cur-year');
    if(yr) yr.textContent = new Date().getFullYear();

    // 焦点图轮播
    var slides = document.querySelectorAll('.focus-slide');
    var dotsWrap = document.getElementById('focusDots');
    if(slides.length > 1){
        var cur = 0;
        // 生成圆点
        if(dotsWrap){
            for(var i=0;i<slides.length;i++){
                (function(idx){
                    var d = document.createElement('span');
                    d.className = 'focus-dot' + (idx===0?' active':'');
                    d.onclick = function(){go(idx)};
                    dotsWrap.appendChild(d);
                })(i);
            }
        }
        var dots = dotsWrap ? dotsWrap.querySelectorAll('.focus-dot') : [];
        function go(n){
            slides[cur].classList.remove('active');
            if(dots[cur]) dots[cur].classList.remove('active');
            cur = (n + slides.length) % slides.length;
            slides[cur].classList.add('active');
            if(dots[cur]) dots[cur].classList.add('active');
        }
        setInterval(function(){go(cur+1)}, 5000);
    }

    // 搜索验证
    window.chksearch = function(form){
        var q = form.q.value.trim();
        if(!q){alert('请输入搜索关键词');return false}
        return true;
    };

    // 平滑滚动
    document.addEventListener('click', function(e){
        var a = e.target.closest('a[href^="#"]');
        if(a && a.getAttribute('href') !== '#'){
            e.preventDefault();
            var t = document.querySelector(a.getAttribute('href'));
            if(t) t.scrollIntoView({behavior:'smooth'});
        }
    });
})();
