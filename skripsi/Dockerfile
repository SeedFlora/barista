# Toolchain LaTeX tetap: image Debian dikunci dengan digest, paket dari snapshot.
FROM debian:bookworm-20250203-slim@sha256:40b107342c492725bc7aacbe93a49945445191ae364184a6d24fedb28172f6f7

ARG DEBIAN_SNAPSHOT=20250901T000000Z
ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Asia/Bangkok \
    SOURCE_DATE_EPOCH=1790899200 \
    FORCE_SOURCE_DATE=1

RUN rm -f /etc/apt/sources.list.d/debian.sources \
    && printf 'deb [check-valid-until=no] http://snapshot.debian.org/archive/debian/%s/ bookworm main\n' "$DEBIAN_SNAPSHOT" > /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
       latexmk texlive-latex-extra texlive-fonts-recommended \
       texlive-lang-other texlive-science poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# apacite.sty dan apacite.bst untuk sitasi APA/BibTeX pada naskah.
RUN apt-get update \
    && apt-get install -y --no-install-recommends texlive-bibtex-extra \
    && rm -rf /var/lib/apt/lists/*

# ulem.sty merupakan bagian paket plain/generic pada distribusi Debian.
RUN apt-get update \
    && apt-get install -y --no-install-recommends texlive-plain-generic \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /work
COPY . /work/
RUN chmod +x /work/tools/build-docker.sh
ENTRYPOINT ["/bin/sh", "/work/tools/build-docker.sh"]
