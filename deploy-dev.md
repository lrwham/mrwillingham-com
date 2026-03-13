# To Deploy the Development Version of the Site

## __optional cleanup__
```bash
sudo rm -r /var/www/dev.mrwillingham.com/
```

## Clone the repo to the server
```bash
sudo git clone https://github.com/lrwham/mrwillingham-com.git /var/www/dev.mrwillingham.com
```

## File ownership for serving the site

Change the user as needed.

```bash
sudo chown -R ubuntu /var/www/dev.mrwillingham.com/
```

## Checkout the dev branch and init submodules

The hard reset is not necessary if the repo is clean, but it is used in the Github action to ensure that the server is always in a clean state before building the site. If you did the optional cleanup step above, then you could simply `git checkout dev && git submodule update --init --recursive`.

```bash
cd /var/www/dev.mrwillingham.com
git fetch origin dev
git checkout dev
git reset --hard origin/dev
git submodule update --init --recursive
```

## Install Hugo

```bash
HUGO_VERSION=$(curl -s https://api.github.com/repos/gohugoio/hugo/releases/latest | grep '"tag_name"' | sed 's/.*"v\(.*\)".*/\1/')
echo $HUGO_VERSION
wget -4 https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-arm64.deb
sudo dpkg -i hugo_extended_${HUGO_VERSION}_linux-arm64.deb
```

## Build the site

The site will be built in the `public` directory. The `--minify` flag will minify the HTML, CSS, and JavaScript files for faster loading. The `--buildFuture` and `--buildDrafts` flags will include any content with a future publish date or marked as a draft. The `--baseURL` flag will set the base URL for the site, which is important for the development version to ensure that all links and assets are correctly referenced.

```bash
HUGO_ENV=dev hugo --minify --buildFuture --buildDrafts --baseURL "https://dev.mrwillingham.com/"
```

## Serve the site

Use your preferred method to serve the site. Point the site root at the `public` directory. For example, if using nginx, the config would look something like this:

```nginx
server {
    listen 80;
    server_name dev.mrwillingham.com;

    root /var/www/dev.mrwillingham.com/public;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```