declare default element namespace "http://www.w3.org/1999/xhtml";
declare namespace html="http://www.w3.org/1999/xhtml";

declare variable $serverroot external;
declare variable $inputpaths external;

declare function local:rewrite-head($head){
    (: Note original head is ignored :)
    local:filter-items(
        <head>
            <meta charset="utf-8"/>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <script type="text/javascript" data-main="{$serverroot}js/lib/requireconfig" src="{$serverroot}js/lib/require.js" >{comment {'prevent self-closing'}}</script>
            <link href="{$serverroot}index.css" rel="stylesheet" type="text/css"/>
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

declare function local:rewrite-body($body){
    element body {
        <div class="menu">
            <h1>Projects</h1>
            <ul>
                <li><a href="{$serverroot}project/blink/build.html">Blink</a></li>
                <li><a href="{$serverroot}project/pov/build.html">Persistence of Vision</a></li>
                <li><a href="{$serverroot}project/alarmclock/build.html">Alarm Clock</a></li>
                <li><a href="{$serverroot}project/ledclock/build.html">LED Clock</a></li>
                <li><a href="{$serverroot}project/keyboard/build.html">Conductive Keyboard</a></li>
            </ul>
        </div>,
        for $headtag in $body/*
        let $sectiontags := local:sectionafter($headtag),
            $sectionimage := ($sectiontags//img)[1],
            $filteredimage :=
            if ($sectionimage) then
                <a href="{$sectionimage/@src}" target="_animation"><img src="{$sectionimage/@src}" /></a>
            else (),
            $filteredtags := ($sectiontags except $sectionimage/ancestor::*)
        where local:is-header($headtag)
        return local:filter-items(
                (
                    $headtag,
                    <table class="section">
                        <tr>
                            <td class="text">{$filteredtags}</td>
                            {if($filteredimage) then <td class="image">{$filteredimage}</td> else ()}
                        </tr>
                    </table>
                )
        )
    }
};

declare function local:filter-items($items as node()*) as node()* {
    for $item in $items return
        typeswitch($item)
            case element() return (
                let $name := local-name($item)
                return
                    if($name='html') then
                        element html {
                            local:rewrite-head($item/head),
                            local:rewrite-body($item/body)
                        }
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