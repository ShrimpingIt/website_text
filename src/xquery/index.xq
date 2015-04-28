declare default element namespace "http://www.w3.org/1999/xhtml";
declare namespace html="http://www.w3.org/1999/xhtml";

declare variable $sourcepath external;
declare variable $allsourcepaths external;
declare variable $serverroot external;

declare function local:body-classes(){
    tokenize($sourcepath, '([/\\\.])|(\.html)')[not(.='')]
};

declare function local:rewrite-head($head){
    (: Note original head is ignored :)
    local:filter-items(
        <head>
            <title>{string((root($head)//*[local:is-header(.)])[1])}&#160;</title>
            <meta charset="utf-8"/>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <script type="text/javascript" src="{$serverroot}style/require/require.js" >&#160;</script>
            <script>
                require.config({{
                    baseUrl: '{$serverroot}style/require',
                }});
            </script>
            <script type="text/javascript" src="{$serverroot}style/index.js" >&#160;</script>
            <link href="http://fonts.googleapis.com/css?family=Oswald:400,300,700|Lusitana:400,700|Open+Sans:400,800" rel='stylesheet' type='text/css' />
            <link href='http://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic,900,900italic' rel='stylesheet' type='text/css'/>
            <link href='http://fonts.googleapis.com/css?family=Merriweather+Sans:400,300,300italic,400italic,700italic,700,800,800italic' rel='stylesheet' type='text/css'/>
            <link rel="stylesheet" type="text/css" href="{$serverroot}style/normalize.css" />
            <link rel="stylesheet" type="text/css" href="{$serverroot}style/index.css" />
        </head>
    )
};

declare function local:is-header($item){
    local-name($item)=('h1','h2')
};

declare function local:sectionafter($item){
    let $contentsibling := $item/following-sibling::*[1][not(local:is-header(.))]
    return if ($contentsibling) then (
        $contentsibling, local:sectionafter($contentsibling)
    ) else ()
};

declare function local:write-hero(){
    <section>
        <div class="hero">
            <div class="hero-inner">
                <a href="" class="hero-logo"><img src="style/brand/logo.png" alt="Logo Image"/></a>
                <div class="hero-copy">
                    <h1>@ShrimpingIt : Programmable Electronics</h1>
                </div>
                <p>
                    We document free project designs using prototyping materials<br/>
                    supporting STEM teachers and hobbyists in the UK and worldwide.
                </p>
                <a class="button scroll-on-page-link" href="#what">Find Out More</a>
            </div>
        </div>
    </section>
};

declare function local:relativedoc($node, $path){
    doc(replace(string(document-uri(root($node))), '[^/]*.html', $path))
};

declare function local:rewrite-body($body){
    let $classes := local:body-classes(),
        $projectpage := 'project'=$classes and count($classes) = 3 (: corresponds to e.g. ('project','alarmclock','index'):)
    return
    <body class="{fn:normalize-space(string-join($classes,' '))}">
        {
            if(count($classes)=1 and 'index'=$classes) then local:write-hero() else ()
        }
        <header class="navigation" role="banner">
            <div class="navigation-wrapper">
                <a href="/" class="logo">
                    <img src="{$serverroot}style/brand/logomenu.png" alt="Logo Image"/>
                </a>
                <a href="javascript:void(0)" class="navigation-menu-button" id="js-mobile-menu">MENU</a>
                <nav role="navigation">
                    <ul id="js-navigation-menu" class="navigation-menu show">
                        {
                            if($projectpage) then
                                let $introdoc := local:relativedoc($body, 'index.html'),
                                    $introtitle := string($introdoc//h1)
                                return
                                    <li class="nav-link more"><a href="./">{$introtitle} Project</a>
                                        <ul class="submenu">
                                            <li><a href="index.html">Introducing It</a></li>
                                            <li><a href="build.html">Wiring It</a></li>
                                            <li><a href="program.html">Programming It</a></li>
                                            <li><a href="debug.html">Debugging It</a></li>
                                            <li><a href="teach.html">Teaching It</a></li>
                                            <li><a href="buy.html">Buying It</a></li>
                                        </ul>
                                    </li>
                            else ()
                        }
                        <li class="nav-link more">
                            <a href="{$serverroot}index.html#project">{if($projectpage) then 'Other Projects' else 'Projects' }</a>
                            <ul class="submenu wide">
                                <li><a href="{$serverroot}index.html#project-blink">...blink an LED</a></li>
                                <li><a href="{$serverroot}index.html#project-pov">...paint with light</a></li>
                                <li><a href="{$serverroot}index.html#project-blink">...make a Banana Piano</a></li>
                                <li><a href="{$serverroot}index.html#project-memory">...test your melody memory</a></li>
                                <li><a href="{$serverroot}index.html#project-alarmclock">...invent a new Clock</a></li>
                                <!-- <li><a href="{$serverroot}index.html#project-ledclock">...build a Word Clock</a></li> -->
                            </ul>
                        </li>
                        <li class="nav-link more">
                            <a href="{$serverroot}kit/">Kits</a>
                            <ul class="submenu">
                                <li><a class="scroll-on-page-link" href="#kit">How to Choose</a></li>
                                <li class="more">
                                    <a href="javascript:void(0)">Product List</a>
                                    <ul class="submenu wide">
                                        <li><a href="{$serverroot}kit/shrimp.html">Shrimp Bundle</a></li>
                                        <li><a href="{$serverroot}kit/pov.html">Persistence of Vision</a></li>
                                        <li><a href="{$serverroot}kit/keyboard.html">Conductive Keyboard</a></li>
                                        <li><a href="{$serverroot}kit/memory.html">'Simon' Memory Game</a></li>
                                        <li><a href="{$serverroot}kit/alarmclock.html">Alarm Clock</a></li>
                                        <!-- <li><a href="{$serverroot}project/ledclock/">Word Clock</a></li> -->
                                    </ul>
                                </li>
                            </ul>
                        </li>
                        <li class="nav-link more">
                            <a href="javascript:void(0)">Teaching</a>
                            <ul class="submenu">
                                <li class="nav-link"><a href="{$serverroot}workshop/">Workshops</a></li>
                                <li class="nav-link"><a href="{$serverroot}about.html">Resources</a></li>
                                <li class="nav-link"><a href="{$serverroot}index.html#testimonials" class="scroll-on-page-link" >Testimonials</a></li>
                                <li class="nav-link"><a href="{$serverroot}offer.html" >Special Offers</a></li>
                            </ul>
                        </li>
                        <li class="nav-link more">
                            <a href="javascript:void(0)">More</a>
                            <ul class="submenu">
                                <li class="nav-link"><a href="{$serverroot}index.html#about" class="scroll-on-page-link" >About Us</a></li>
                                <li class="nav-link"><a href="{$serverroot}contribute.html">Contributing</a></li>
                                <li class="nav-link"><a href="{$serverroot}license.html">Licensing</a></li>
                                <li class="nav-link"><a href="{$serverroot}feedback.html" target="_blank" >Feedback</a></li>
                                <li class="nav-link"><a href="{$serverroot}contact.html">Contact</a></li>
                            </ul>
                        </li>
                    </ul>
                </nav>
                <div class="navigation-tools">
                    <div class="search-bar">
                        <form role="search" action="http://duckduckgo.com/" method="get">
                            <input type="hidden" value="start.shrimping.it" name="sites"></input>
                            <input type="hidden" value="1" name="kh"></input>
                            <input type="hidden" value="1" name="kn"></input>
                            <input type="hidden" value="1" name="kac"></input>
                            <input type="search" placeholder="Enter Search" name="q"></input>
                            <button type="submit">
                                <img src="{$serverroot}style/brand/search-icon.png" alt="Search Icon"/>
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </header>
        <section class="content">
            {
                if(('project'=$classes) and ('build'=$classes)) then (
                    local:filter-project-body($body)
                )
                else (
                    local:filter-descendants($body)
                )
            }
        </section>
        <footer class="footer" role="contentinfo">
            <div class="footer-logo">
                <img src="{$serverroot}style/brand/logomenu.png" alt="Logo image" />
            </div>
            <div class="footer-links">
                <ul>
                    <li><h3>Community</h3></li>
                    <li><a href="{$serverroot}project/">Projects</a></li>
                    <li><a href="{$serverroot}support.html">Support</a></li>
                    <li><a href="{$serverroot}license.html">Licensing</a></li>
                </ul>
                <ul>
                    <li><h3>Commercial</h3></li>
                    <li><a href="{$serverroot}kit/">Kits</a></li>
                    <li><a href="{$serverroot}workshop/">Workshops</a></li>
                    <li><a href="{$serverroot}workshop/cpd.html">Training</a></li>
                </ul>
                <ul>
                    <li><h3>More</h3></li>
                    <li><a href="{$serverroot}contact.html">Contact Us</a></li>
                    <li><a href="{$serverroot}social.html">Follow Us</a></li>
                    <li><a href="{$serverroot}">About Us</a></li>
                </ul>
            </div>
            <hr/>
            <p>
                Thanks to the <a href="http://arduino.cc">Arduino</a> community for the amazing foundations on which the Shrimp and @ShrimpingIt projects are based.
                Thanks to <a href="http://fritzing.org">Fritzing</a> for vector graphics elements. Flickr user <a href="https://www.flickr.com/photos/randomskk/">Adam Greig</a> for cover image.
            </p>
        </footer>
    </body>
};

declare function local:project-tabname($headtags, $headindex){
    concat('tab', $headindex)
};

declare function local:project-tablink($headtags, $headindex){
    concat('#step', $headindex)
};

declare function local:filter-project-body($body){
    let $headtags := $body/*[local:is-header(.)]
    return local:filter-items(
        <section>
            <div class="pagination">
                <ul>
                    <li class="page-prev"><a href="javascript:void(0)">Prev</a></li>
                    <li>
                        <ul>
                            {
                                for $headtag at $headindex in $headtags
                                return
                                    <li><a href="{local:project-tablink($headtags,$headindex)}">{$headindex}</a></li>
                            }
                        </ul>
                    </li>
                    <li class="page-next"><a href="javascript:void(0)">Next</a></li>
                </ul>
            </div>
            <div class="vertical-tabs-container">
                <div class="vertical-tabs">
                    {
                        for $headtag at $headindex in $headtags
                            let $tabname := local:project-tabname($headtags,$headindex)
                        return
                            <a href="javascript:void(0);"
                                class="js-vertical-tab vertical-tab {if ($headindex=1) then 'is-active' else ''}"
                                rel="{$tabname}">
                                {string($headtag)}
                            </a>
                    }
                </div>
                <div class="vertical-tab-content-container">
                    {
                        for $headtag at $headindex in $headtags
                        let $sectiontags := local:sectionafter($headtag),
                            $sectionimage := ($sectiontags//img)[1],
                            $remainingtags := ($sectiontags except $sectionimage/ancestor::*),
                            $tabname := local:project-tabname($headtags,$headindex)
                        return
                            <div>
                                <a href="" class="js-vertical-tab-accordion-heading vertical-tab-accordion-heading is-active" rel="{$tabname}">{string($headtag)}</a>
                                <div id="{$tabname}" class="js-vertical-tab-content vertical-tab-content">
                                    <a href="{$sectionimage/@src}" target="_animation"><img src="{$sectionimage/@src}"/></a>
                                    <aside>{$remainingtags}</aside>
                                </div>
                            </div>/*
                    }
                </div>
            </div>
        </section>
    )
};

declare function local:filter-items($items as node()*) as node()* {
    for $item in $items return
        typeswitch($item)
            case element() return (
                let $name := local-name($item)
                return
                    if($name='html') then (
                        processing-instruction {"DOCTYPE"} {"html"},
                        <html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
                            {
                                local:rewrite-head($item/head),
                                local:rewrite-body($item/body)
                            }
                        </html>
                    )
                    else
                        element {$name} {
                            local:filter-descendants($item) (: duplicate, filtering descendants :)
                        }
            )
            case attribute() return
                let $name := local-name($item),
                    $value := string($item)
                return
                    attribute {QName('', $name)} { $value } (: duplicate :)
            case text() return
                text {$item}
            case processing-instruction() return
                $item
            case comment() return
                $item
            default return
                local:filter-descendants($item) (: Just passes back children if any - handles case of root/doc node? :)
};

declare function local:filter-descendants($item as node()) as node()* {
    local:filter-items(local:get-descendants($item))
};

declare function local:get-descendants($item as node()) as node()*{
    let $attributes := $item/@*,
        $children := $item/node()
    return ($attributes,$children)
};

local:filter-items(.)