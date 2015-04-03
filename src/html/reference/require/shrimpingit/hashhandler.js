require(['jquery'], function($) {

    var lasthash = null;

    function getScrollXY() {
        var scrOfX = 0, scrOfY = 0;
        if( typeof( window.pageYOffset ) == 'number' ) {
            //Netscape compliant
            scrOfY = window.pageYOffset;
            scrOfX = window.pageXOffset;
        } else if( document.body && ( document.body.scrollLeft || document.body.scrollTop ) ) {
            //DOM compliant
            scrOfY = document.body.scrollTop;
            scrOfX = document.body.scrollLeft;
        } else if( document.documentElement && ( document.documentElement.scrollLeft || document.documentElement.scrollTop ) ) {
            //IE6 standards compliant mode
            scrOfY = document.documentElement.scrollTop;
            scrOfX = document.documentElement.scrollLeft;
        }
        return [ scrOfX, scrOfY ];
    }

    function hashLoaded(){

        var hash = location.hash;

        var matchq = $(hash);
        if(hash != lasthash){
            //emulate click if the id matches to a tab (causes it to open)
            if( matchq.is("a.tab")  //corresponds with refill's vertical-tab
                ||
                matchq.is("a.tab-link") //corresponds with refill's accordion-tab
            ){
                matchq.click();
                var from = $(document).scrollTop();
                var to = matchq.offset().top;
                $('html,body').css({scrollTop:from});
                $('html,body').animate( {scrollTop:to}, 'slow' );
            }
            lasthash = hash;
        }

    };

    $(document).ready(function () {

        //set up event handling for hashchange
        window.onhashchange = hashLoaded;

        //trigger hashchange when loaded, in case the page was loaded with a hash
        window.onhashchange();

    });

});