    var $j = jQuery.noConflict();
    $j(document).ready(function(){
        $j('.user-block-hide').hide();
        $j('.user-block1 a').click(
            function() {
                $j(this).toggleClass("active");
                $j(".user-block-hide").slideToggle(300);
            }
        );
        $j('.tabs1').click(function(){
            $j('.tabs').find('.active').removeClass('active');
            $j(this).addClass('active');
            $j('.content-block-content').find('.active').removeClass('active');
            $j('.tabs-1').addClass('active').show(300);
            $j('.tabs-2').hide(200);
            $j('.tabs-3').hide(200);
        });
        $j('.tabs2').click(function(){
            $j('.tabs').find('.active').removeClass('active');
            $j(this).addClass('active');
            $j('.content-block-content').find('.active').removeClass('active');
            $j('.tabs-2').addClass('active').show(300);
            $j('.tabs-1').hide(200);
            $j('.tabs-3').hide(200);
        });
        $j('.tabs3').click(function(){
            $j('.tabs').find('.active').removeClass('active');
            $j(this).addClass('active');
            $j('.content-block-content').find('.active').removeClass('active');
            $j('.tabs-3').addClass('active').show(300);
            $j('.tabs-2').hide(200);
            $j('.tabs-1').hide(200);
            });
        $j('.empty-wishlist span.bounce-search').click(function(){
            $j('div.js-search-inner').effect("bounce", 500, function() {
                $j('div.js-search-inner input[type="text"]').focus();
            });
        });
    });