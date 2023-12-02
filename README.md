# imagexd-2019

Source of the ImageXD 2019 website.

## Installing Hugo

This site is built using Hugo.  Please download the latest binary from

https://github.com/gohugoio/hugo/releases

and place it somewhere on your path.

## Building the website
- `git submodule update --init` : get the hugo template
- `make html` : Build the static website
- `make serve` : Serve the website locally and monitor for changes.
- `make github` : Upload the website to GitHub Pages (https://xd-con.github.io/tensor-2020)
