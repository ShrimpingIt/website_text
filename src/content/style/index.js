require.config({
    paths: {
        jquery: 'jquery-1.11.1'
    }
});

require(['refills/navigation']);
require(['refills/accordion-tabs']);
require(['refills/vertical-tabs']);
require(['refills/scroll']);
require(['refills/sliding-panel']);
require(['refills/parallax']);

require(['highlight']);

require(['shrimpingit/hashhandler']);
require(['shrimpingit/codeblocks']);