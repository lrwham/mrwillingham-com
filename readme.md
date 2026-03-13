# Add Content

To make a new page `hugo new content music-technology/dayxx.md`. The archetype includes the front matter.

# Serve Local Development Site

`HUGO_ENV=dev hugo serve --buildFuture --buildDrafts` will serve the site locally and include any content with a future publish date or marked as a draft.

`HUGO_ENV=dev` simply displays a dev banner in the corner of the page to visually remind you that you are viewing the development version of the site. It is used in the Github action that deploys that development server.

# Install GIT Submodules for Themes

`git submodule update --init --recursive`