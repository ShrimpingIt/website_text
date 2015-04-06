require(['jquery', 'animateScroll'], function($) {

    //prevent page from scrolling unnecessarily to the anchor for hashes corresponding to tabs
    /*
    $( 'a[href^="#"]' ).click( function(e) {
        e.preventDefault();
        location.hash = "#" + id;
        var rel = $(this).attr("href").substring(1);
        $('a[rel="' + rel + '"]"').click();
        //$(this).closest("section").animateScroll({scrollSpeed:4000});
    } );
    */

    $('a.tab-link, a.vertical-tab').click(function(e){
       window.location.hash = '#' + $(this).attr("rel");
    });

    function loadTab(tabname){
        var relselector = '[rel="' + tabname + '"]';
        var matchq = $('a.tab-link' + relselector + ',' + 'a.vertical-tab' + relselector).first();
        matchq.click();
    }

    var lasthash = null;
    function hashLoaded(){
        var hash = location.hash;
        if(hash != lasthash){
            loadTab(location.hash.substring(1));
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