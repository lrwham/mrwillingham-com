# Add Content

To make a new page `hugo new content music-technology/dayxx.md`. The archetype includes the front matter.

# Serve Local Development Site

`HUGO_ENV=dev hugo serve --buildFuture --buildDrafts` will serve the site locally and include any content with a future publish date or marked as a draft.

`HUGO_ENV=dev` simply displays a dev banner in the corner of the page to visually remind you that you are viewing the development version of the site. It is used in the Github action that deploys that development server.

# Install GIT Submodules for Themes

`git submodule update --init --recursive`

# Github Actions Setup

Generate keys on the server that will host the website. Then add the username, host IP, and SSH key as secrets in the Github action config.

### Generate New Keys

```bash
ssh-keygen -t ed25519 -f ~/.ssh/deploy_key -N ""
```

### Authorize Keys

```bash
cat ~/.ssh/deploy_key.pub >> ~/.ssh/authorized_keys
```

### Copy & Paste Secret Key

Manually and copy & paste

```bash
cat ~/.ssh/deploy_key
```