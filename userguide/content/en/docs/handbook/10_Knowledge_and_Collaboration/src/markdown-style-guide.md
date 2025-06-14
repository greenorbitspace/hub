---
title: Markdown Style Guide
linkTitle: Markdown style guide
date: '2025-05-10T22:54:00Z'
weight: 1
description: Comprehensive Markdown style guide for the GitLab Handbook, detailing
  usage, formatting rules, and best practices for headings, paragraphs, lists, links,
  images, and more to ensure consistency and accessibility in documentation.
draft: false
ref: markdown-style-guide
---
> This is a paragraph.
>
> > A nested blockquote.
>
> ### Headers work
>
> - lists too
>
> and all other block-level **elements**.
>
> Even code blocks:
>
> ```ruby
> def hello
>   puts "Hello world!"
> end
> ```

```

Output

> 

> 

## Comments

There are two types of comment which can be used. The first allows you to leave comments in a markdown file which can only be viewed in the repository and are not rendered to HTML or included in a pages source. The second type is a standard HTML comment which will be included in the pages source.

### Markdown comments

See comments shortcode.

### HTML Markup comments

It is also possible to use HTML comments. These differ in that they are also included in the rendered pages source.

Markdown

```plain text
This is a paragraph <!-- This is accepted as a comment too --> ... paragraph continues here.

```

Output

This is a paragraph  … paragraph continues here.

Output HTML

```plain text
<p>This is a paragraph <!-- This is accepted as a comment too -->…
paragraph continues here.</p>

```

## Anchors

Typically you shouldn’t need anchors as well structured documents with headings should prove a good route to linking to text you may want to reference on another page. All headings act as anchors on a page. However there maybe times when you need it, such as if you have an icon in the header.

There are multiple ways to add an anchor.

### Markdown Anchors

This is the preferred method of handling anchors in the handbook.

The extended markdown syntax includes anchors, or heading IDs.

Markdown

```plain text
## Anchors are invisible elements {#hello-world}

```

Output

## Anchors are invisible elements

Output HTML

```plain text
<h2 id="hello-world">Anchors are invisible elements</h2>

```

### Shortcode Anchors

This small shortcode will drop an anchor in a page which you can reference from the same page or another page. The text in quote marks is the name of anchor you’ll use when linking to it.

Markdown

```plain text
<!-- inline link or anchor removed --> Anchors are invisible elements

```

Output

Anchors are invisible elements

Output HTML

```plain text
<a name="hello-world"></a> Anchors are invisible elements

```

### HTML Anchors

One of the more powerful features of using Markdown is the ability to mix HTML and Markdown in the same document. With this in mind it is also possible to use normal HTML to create an anchor in a page. This is the method you need to use when adding anchors to markdown documents not in the GitLab Handbook.

Markdown

```plain text
<a name="goodbye-world"></a> Anchors are invisible elements

```

Output

Anchors are invisible elements

## Emoji and Font Awesome

Hugo and Docsy provide support for using both Emojis and Font Awesome to provide icons and simple graphics to spice up your content.

### Emojis

To insert emojis in to content you can use the same syntax as you find on GitLab and Slack. Use a : followed by the name of the emoji followed by another :. Its also possible to look up emojis on the ‘Emoji Cheat Sheet’.

Note: When copying from the cheatsheet it includes the colons for you.

Markdown

I :‌orange_heart: GitLab

Output

I :orange_heart: GitLab

### Font Awesome

Font Awesome is loaded indirectly through the Docsy theme. The icon library provides thousands of free to use and open source glyphs and icons which can be embedded into handbook content. The easiest way to use Font Awesome is to copy the HTML for the glyph directly from the Font Awesome Icon gallery and paste it directly in to your content.

It is recommended to use the review app to preview the changes. At times, the loaded version of Font Awesome is not the latest.

Markdown

```plain text
<i class="fa-regular fa-heart fa-2xl"></i>

```

Output

Note: The minimum requirement is one of the base classes (such as fas or fa-regular) and the icon class (such as fa-heart).

### Splash of color

It is possible to add a splash of color to Font Awesome icons by adding -text-<color> (for example -text-success) to the end of the class definition. Where it says color you can replace this with any of the available shortcode colors.

Markdown

```plain text
<i class="fa-brands fa-gitlab fa-2xl -text-primary"></i>

```

Output

## Colorful sections

See panels shortcode.

## Embed documents

It’s easy to embed Google Docs, Sheets, Slides, and pretty much everything that provides an iframe to use with. The only thing you need to do is use the following code inside your markdown file and replace the iframe from the document you want to embed:

```plain text
<iframe IFRAME CONTENT></iframe>

```

### Google products

For Google products, with your document opened, click File -> Publish to the web. For example, here’s what Google sheets will look like:

<!-- Unsupported block type: image -->

Google Sheets - File - Publish to the web

Choose Embed, check your settings, click on Publish and copy the <iframe>. Then go to your markdown file and wrap the iframe into a <!-- embedded Google Doc removed --> short code. The shortcode makes the iframes the right size on the page and allows them to be resized by the user.

### Google Sheets

Let’s exemplify with this [simple spreadsheet]. Follow the info above to find the iframe:

<!-- Unsupported block type: image -->

Google Sheets - Embed iframe

Copy the code below and paste to your markdown file (leave a blank line above and below it). Then replace the <iframe> with your own:

Markdown

```plain text
<!-- embedded Google Doc removed -->
<iframe src="https://docs.google.com/spreadsheets/d/1jAnvYpRmNu8BISIrkYGTLolOTmlCoKLbuHVWzCXJSY4/pubhtml?widget=true&amp;headers=false"></iframe>


```

Output

<!-- Unsupported block type: unsupported -->

<!-- Unsupported block type: divider -->

### Google Slides

Let’s exemplify with this GitLab slide deck. Follow the steps above to find the iframe:

<!-- Unsupported block type: image -->

Google Slides - Embed iframe

Copy the code below and paste to your markdown file (leave a blank line above and below it). Then replace the <iframe> with your own:

Markdown

```plain text
<!-- embedded Google Doc removed -->
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vS_iuMXnp61wlo4amm5nvHr4Ir8VUzisJSBsr7YEL7fKWAiT-9bmehyngtb9TYaFEsFnRokCyIXwsvY/embed?start=false&loop=false&delayms=3000"
frameborder="0" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>


```

Output

### Google Docs

### Warning

Embedding Google Docs is not a recommended practice. Prefer converting your document content to markdown instead.

If you need to embed it anyway, follow the same instructions and the same logic as we presented for Google Sheets and Slides, wrapping the <iframe> with a <!-- embedded Google Doc removed --> shortcode:

Markdown

```plain text
<!-- embedded Google Doc removed -->
<iframe src="https://docs.google.com/document/d/1mHhOhvvrz7xgUPyn5VWCNuKgew5MRRGZp761B9prPqs/pub?embedded=true"></iframe>


```

Output

## Embed Tweets

X/Twitter changed its usage policy, and might add rate limits. Sometimes, tweets cannot be loaded when embedded, and fail CI/CD builds or the deployed handbook (see the issue discussion). Create a screenshot of the tweet instead, and upload the image into the handbook.

## Embed GitLab Snippets

To embed GitLab Snippets to a markdown file, copy the embed code from your public snippet and paste it in the file.

Markdown

```plain text
<!-- leave a blank line here -->
<script src="https://gitlab.com/gitlab-org/gitlab-ce/snippets/1717978.js"></script>
<!-- leave a blank line here -->

```

Output

  hello-world.html    195 B

12345678910

```plain text
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Hello World</title>
</head>
<body style="background-color: black; color: white">
  <h1>HELLO WORLD!</h1>
</body>
</html>
```

## Other Embeds

Other embeds can be included in the handbook, as outlined in Embed documents. However, due to privacy (especially cookie) concerns, we recommend only embedding from sites outlined in our tech stack, or where “no cookies” can be specified.

## Math

Mathematical and other formulae are supported through the use of LaTeX markup. The Hugo implementation uses the MathJax engine.

The frontmatter parameters must have math: set to true.

```plain text
This is an inline \\(a^\*=x-b^\*\\) equation.
These are block equations:
\\[a^\*=x-b^\*\\]
\\[ a^\*=x-b^\* \\]
\\[
a^\*=x-b^\*
\\]

```

This is an inline a∗=x−b∗a∗=x−b∗ equation.

These are block equations:

a∗=x−b∗a∗=x−b∗

a∗=x−b∗a∗=x−b∗

a∗=x−b∗a∗=x−b∗

## Line length

We do not enforce a line length (MD013).

## Markdown Editors

Please use the editors available on GitLab.com, one of the following code editors, or your preferred code editor to write in markdown.

It is not recommended writing your document in a regular text editor like Google Docs, Microsoft Word, or macOS’ Pages, then copy-pasting to markdown, as it most likely will bring some characters with a different encoding (non UTF-8), which will cause the markdown to not render correctly.

In case you don’t have a choice and need to import a text already written in a text editor, paste it to your markdown file using command+shift+V on a Mac, or control+shift+V on Windows or Linux. You might minimize the cause of trouble by pasting without format. But yet, is not guaranteed it is going to work, so double check your output.

If the document was in Google Docs, you can install the Docs to Markdown add-on, which helps convert the Google Docs to markdown. You’ll likely need to make minor updates or edits to the markdown that the add-on generates.

### Editors Available on GitLab.com

- Web IDE

- Web Editor

### Regular Code Editors

- Visual Studio Code

- Sublime Text

- Vim

- NeoVim

### Markdown editors (type and preview simultaneously)

- Markdown editors for Mac: [MacDown], [iA Writer], [Ulysses]

- In-browser markdown editor: [StackEdit]

- Markdown Tables Generator

If you’re not used to writing markdown, these editors can be helpful. Many editors offer real time previews and while these previews may not be exactly the same as the final result they can be a very good approximation, which gives you a good idea of what the output will be while you type.

[StackEdit] is awesome too, you can work on a markdown file even if you’re away from your computer, or out of resources. It works from every major browser and automatically saves your work to Google Drive.

Do you want a simple way of copying a hyperlink title and address in markdown? The Format Link extension offers a quick and easy way to do this, along with allowing you to customize any number of other formats. View detailed instructions and examples.

If you’re looking for just the ability to copy something as markdown, try these Firefox add-ons or Chrome extensions.

## Complementary Notes

- 

- 

- 

- 

- 

- 

- 

- 

- 

## More

Anything else you know of and is not described here? Any new magic? Any trick? Please contribute!