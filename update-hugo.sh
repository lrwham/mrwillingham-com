HUGO_VERSION=$(curl -s https://api.github.com/repos/gohugoio/hugo/releases/latest \
  | grep '"tag_name"' \
  | sed 's/.*"v\(.*\)".*/\1/')

if [ -z "$HUGO_VERSION" ]; then
  echo "ERROR: Could not fetch latest Hugo version."
  exit 1
fi
echo "Latest Hugo version: $HUGO_VERSION"

DEB_FILE="/tmp/hugo_extended_${HUGO_VERSION}_linux-arm64.deb"
wget -4 "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-arm64.deb" \
  -O "$DEB_FILE"

sudo apt-get install -y "$DEB_FILE"

hugo version
rm -f "$DEB_FILE"
