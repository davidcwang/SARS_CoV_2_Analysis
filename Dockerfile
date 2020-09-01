FROM alpine:3.12.0

RUN apk update
RUN apk add --no-cache bash shadow make build-base curl binutils
# RUN apk add --no-cache shadow
# RUN chsh -s /bin/bash
# RUN exec /bin/bash
RUN /bin/sh

WORKDIR sars

# Build MAFFT executable
COPY opt ./
WORKDIR mafft-7.471/core/
RUN make clean
RUN make
RUN su
RUN make install

# RUN mafft

ENTRYPOINT ["executable"]