Documentation is for my own sanity, so that I know what I'm doing when I need to add more projects or course notes to the site down the road.

Projects and notes are stored as XML files.

To create a new project:

  python newproject.py [project name]

A file containing project data starts with <project>. Files with data about a particular course starts with <course>.

PROJECT FILES:
The 'projects' folder must only contain XML files that are correctly 
Data about the project is contained within <project></project>.

Some tags are:
<meta> - data for the list view of all projects
  <title> - the title to be displayed
  <desc> - project desc (VERY IMPORTANT: don't make this more than 4 lines long or the formatting gets janky!)
  <thumb> - the image file for the thumbnail

<title> - the title block. this should probably be the first thing after the initial <project> tag, but the program can theoretically put big header text anywhere.

<subtitle align="[l/c/r]"> - a smaller title for some subsection. align parameter is optional (left by default).

<text> - a block of text with nothing else.
  !lb href="link_url.com"!rb blah !cl - a link somewhere
  !br for linebreak

<img cfg="[s/p]" i="filename.png|filename2.jpeg"> - either single images (s) or pairs of images (p) with optional headers displayed on the page.
  <h n="[1/2]" (for pairs only)> - image header
  <cap n="[1/2]" (for pairs only)> - image caption

<vid v="filename.mkv"> - videos with optional headers displayed on the page.
  <h> - video header
  <cap> - video caption

<block arr="[p/q]"> - a block of either a pair (p) or quad (q) of paragraphs, optionally with headers, centered on the page.
  <h n="[1, 2, 3, 4]"> - paragraph header (optional)
  <cap n="[1, 2, 3, 4]"> - paragraph body

<carousel> - a slide show of images
  <slide i="filename.png"> - container for a carousel slide with data about the slide
    <h> (optional) - a header-style caption below the image
    <cap> (optional) - a block of text
