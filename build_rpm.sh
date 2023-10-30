#!/bin/bash

# https://rpm-packaging-guide.github.io/

poetry install
poetry build
poetry run nvautoinstall --version

mkdir -p ~/rpmbuild/SOURCES/
cp dist/*gz ~/rpmbuild/SOURCES/
rpmbuild -bs ./nvautoinstall.spec
rpmbuild -bb ./nvautoinstall.spec
