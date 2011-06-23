# -*- coding: utf8 -*-
source = u"""= Title 1 = this should be dropped
Normal paragraph.

This
and this
should be in the same paragraph.

Next paragraph is blank:


Next two paragraphs are blank:




A normal paragraph.

== Lists ==

* list item 1
* list item 2
** list item 2.1
** list item 2.2
*** list item 2.2.1
*** list item 2.2.2
**** list item 2.2.2.1
*** list item 2.2.3
** list item 2.3
* list item 3
# list item 3
## list item 3.1
### list item 3.1.1
# list item 4

A discussion
:With some replies
:: Another one
:::Some depth
: One more

A discussion in bold (rarely used):
; test
;; test
;;; test
; test

A mix of different list types:
;* point 1
:** point 1.1
*:*: Strange syntax
*::*#;##*:*;; Weird but correct
*:*#*: First item
*:*#*: Second item of the same list

== Unicode support ==

This sentence "你好" is in Chinese and means "Hello!".

== Preformatted text ==
 Source code
 Some text ''in italic''

== [[Links]] and ''apostrophes'' ==
=== Apostrophes jungle ===

This should be in ''italic'', '''bold'''.

And this is '''''bold and italic'''''...

Here, it's ''italic and '''bold and italic'''''!

Here, it's '''bold and ''bold and italic'''''!

Mabye more complicated: ''italic and '''bold and italic''' and italic only''!

Mabye more complicated: '''bold and ''bold and italic'' and bold only'''!

=== Verification === ...
This: is Peter's test for { the "apostrophe" and } several # other [[characters]].

This is [correct] text.

=== Links ===
An URL: ftp://mozilla.org inside a paragraph.

This paragraph contains an first [[internal]] link and a [[internal link|second one]].

This one an [http://www.mozilla.org external] link.

This should [[be plain text

HTML links <a href="http://some.url">such as this one</a> are NOT allowed and should be treated as text and URL.

== Templates ==
Here, we insert a simple {{template}}.

Here, we insert a {{template|with|some=3|parameters|color = #0000ff|formattedText=''test''}}.

{{Template which
 | is = test
 | multi = test
 | lines = test
}}

Here, we put ''italic around a {{template|2}}...'' (fails)

== Markup ==
<test> this should be normal text since ''test'' is not a valid markup;

This: < and this: > should be replaced by &lt; and &gt;...

<nowiki>This http://fr.wikipedia.org/ is not an URL</nowiki>

<nowiki>this '''should''' be treated as ''unformatted'' text, not as {{templates}}, [[links]] http://url.url etc.</nowiki>

== Tables ==
; Form 1
{|
| cell 1 || cell 2
|-
| cell 3 || cell 4
|}

; Form 2
{|
! cellA
! cellB
|- style="color:red"
| cell C
| cell D
|}

; Form 3
{| class="wikitable"
|-
|
! scope=col | Title A
! scope=col | Title B
|-
! scope=row | Line 1
|data L1-A
|data L1-B
|- style="color:red"
! scope=row | Line 2
|data L2-A
|data L2-B
|}

== Others ==
---- the above line is an '''horizonal rule'''
"""

from mediawiki_parser import wikitextParser
mediawikiParser = wikitextParser

mediawikiParser.url.findAll(source)

mediawikiParser.internalLink.findAll(source)

mediawikiParser.templateName.findAll(source)