# Accessibility

enforce-rules is a Python library, and people who read its documentation or contribute to it may use screen readers, keyboards, magnifiers, translation tools, or other ways of reading and navigating. This document explains what we try to do, what we have not tested, and how to tell us when something gets in the way. It covers this repository's documentation (the README, the Code of Conduct, and the files in `docs/`) and the way people contribute to it.

## Priorities

* **Plain language.** We write documentation so that it can be read without special knowledge, and we explain notation where we use it.
* **Clear structure.** Documents use headings in order, and rules in the Code of Conduct have numbered sections that can be linked to.
* **Text, not images.** Code examples and error messages are written as text so they can be read aloud, copied, and translated.

We don't claim that the documentation meets any accessibility standard. Nobody has evaluated it against one.

## Contributor expectations

Changes to documentation should follow these points:

* Use headings in order and do not skip levels.
* Use link text that describes where the link goes, not "click here."
* Don't use color alone to carry meaning.
* Add a text description for any image.
* Put code and error output in text, not screenshots.

The project does not run automated accessibility checks. When you change something that readers see, describe how you looked at the rendered result in your pull request.

## Reporting accessibility issues

Open an issue with the **Accessibility problem** form: [open the form](https://github.com/Loepker-James/enforce-rules/issues/new?template=accessibility.yml). Tell us what you were trying to do and what got in the way. Links, browser, operating system, and assistive technology are optional. Screenshots and recordings are welcome but not required, and you never need to share anything about yourself or a disability.

If you cannot use GitHub issues, open the form's page and tell us what stopped you, or ask for another way to report in a short issue titled "Accessibility: need another way to report."

### How we respond

We aim to reply within 14 days. A reply will say whether we understand the problem, whether we can fix it, and what we plan to do. If there is a workaround, we will say what it is. We will ask you to confirm a fix when it is ready, and the issue stays open until you do or until we can no longer reach you.

## Ownership and maintenance

The maintainer, [Loepker-James](https://github.com/Loepker-James), is responsible for this document and for accessibility reports. This document is reviewed once a year, in January. If ownership changes, this section will be updated to name the new owner.

## Supported environments

The documentation is Markdown, shown by GitHub and by PyPI. How well it works with a screen reader, a magnifier, or voice control depends mostly on those sites. We have not tested the documentation with any assistive technology, and we do not claim support for any particular combination of browser and assistive technology.

## Known limitations

* **Not tested with assistive technology.** Some formatting may read awkwardly in a screen reader.
* **Notation in the Code of Conduct.** It uses section numbers, "(s)" and "a(n)" endings, and Latin abbreviations such as "e.g." Section 1.4 explains the notation, and some readers may still find it unfamiliar.
* **Small deep headings.** Subsections five levels deep display as small text on GitHub.
* **A table in `ENFORCEMENT.md`.** It lists appeal windows and counts. We have not checked how it reads in a screen reader.

If you have trouble with any of these, please tell us through the form above.

## Feedback and improvements

To suggest a change to this document or to how the project handles accessibility, open an issue or a pull request. Active barriers should go through the reporting process above.
