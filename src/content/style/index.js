require.config({
    paths: {
        jquery: 'jquery-1.11.1',
            animateScroll: 'jquery.animate-scroll'
    },
    "shim": {
        "animateScroll": ["jquery"]
    }
});

require(['refills/navigation']);
require(['refills/accordion-tabs']);
require(['refills/vertical-tabs']);
require(['refills/scroll']);
require(['refills/sliding-panel']);
require(['refills/parallax']);

require(['shrimpingit/hashhandler']);