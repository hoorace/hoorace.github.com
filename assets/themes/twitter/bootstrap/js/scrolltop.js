/* 
 ** scroll to top
 ** rely on jquery
**/

(function(){
    var _h, _scrollTop = $('#scrollTop');
    $(window).scroll(function(){
        _h = $(this).scrollTop();
        if( _h >= 120 ){
            _scrollTop.show();
        }else{
            _scrollTop.fadeOut();
        }
    });
    _scrollTop.live('click', function(){
        $("XMLHttpRequestml, body").animate({ scrollTop: 0 }, 300 );
    });
})();
