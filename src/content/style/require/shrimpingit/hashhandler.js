require(['jquery'], function($) {

    var hashprefix = "step";
    var tabprefix = "tab";

    var lasthash = null;

    $('a.tab-link, a.vertical-tab').click(function(e){
       window.location.hash = '#' + hashprefix + $(this).attr("rel").substring(tabprefix.length);
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
            var tabname = tabprefix + location.hash.substring(hashprefix.length + 1);
            loadTab(tabname);
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