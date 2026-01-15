MDBOOK_VERSION := 0.5.2
MDBOOK_TOC_VERSION := 0.15.3

BINARIES := mdbook mdbook-toc
SRC_DIR := src
SUMMARY_MDFILE := $(SRC_DIR)/SUMMARY.md
BUILD_DIR := book


# mdBook

.PHONY: build serve $(SUMMARY_MDFILE)

build: $(BINARIES) $(SUMMARY_MDFILE)
	./mdbook build

serve: $(BINARIES) $(SUMMARY_MDFILE)
	./mdbook serve -n 127.0.0.1 -p 8000

$(SUMMARY_MDFILE): $(SRC_DIR)/summary.py
	python3 $< > $@


# Download Tools

.PHONY: download-all-binaries

download-all-binaries: $(BINARIES)

mdbook:
	wget -O - https://github.com/rust-lang/mdBook/releases/download/v$(MDBOOK_VERSION)/mdbook-v$(MDBOOK_VERSION)-x86_64-unknown-linux-musl.tar.gz | tar xzf -

mdbook-toc:
	wget -O - https://github.com/badboy/mdbook-toc/releases/download/$(MDBOOK_TOC_VERSION)/mdbook-toc-$(MDBOOK_TOC_VERSION)-x86_64-unknown-linux-musl.tar.gz | tar xzf -


# Clean

.PHONY: clean dist-clean

clean:
	rm -rf $(BUILD_DIR) $(SUMMARY_MDFILE)

dist-clean: clean
	rm -rf $(BINARIES)
