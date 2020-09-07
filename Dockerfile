FROM alpine:3.12.0

RUN apk update
RUN apk add --no-cache bash shadow make build-base curl binutils \
        util-linux pciutils usbutils coreutils findutils grep
# RUN apk add --no-cache shadow
# RUN chsh -s /bin/bash
# RUN exec /bin/bash
RUN /bin/sh

WORKDIR sars

COPY opt ./
COPY data ./data
RUN pwd
RUN ls

# Build MAFFT executable
WORKDIR mafft-7.471/core/
RUN make clean
RUN make
RUN su
RUN make install

WORKDIR /sars/data 
RUN ls

# Create FASTA files to be aligneed
RUN cat sars_cov_2_e_prot.fasta mers_cov_e_prot.fasta > sars_cov_2_mers_cov_e_prot.fasta
RUN cat sars_cov_2_m_prot.fasta mers_cov_m_prot.fasta > sars_cov_2_mers_cov_m_prot.fasta
RUN cat sars_cov_2_n_prot.fasta mers_cov_n_prot.fasta > sars_cov_2_mers_cov_n_prot.fasta
RUN cat sars_cov_2_s_prot.fasta mers_cov_s_prot.fasta > sars_cov_2_mers_cov_s_prot.fasta

# RUN mafft
RUN mafft sars_cov_2_mers_cov_e_prot.fasta > sars_cov_2_mers_cov_e_prot.ali
RUN mafft sars_cov_2_mers_cov_m_prot.fasta > sars_cov_2_mers_cov_m_prot.al
RUN mafft sars_cov_2_mers_cov_n_prot.fasta > sars_cov_2_mers_cov_n_prot.al
RUN mafft sars_cov_2_mers_cov_s_prot.fasta > sars_cov_2_mers_cov_s_prot.al

RUN mafft sars_cov_2_mers_cov_e_prot.fasta > sars_cov_2_sars_cov_1_e_prot.ali
RUN mafft sars_cov_2_mers_cov_m_prot.fasta > sars_cov_2_sars_cov_1_m_prot.al
RUN mafft sars_cov_2_mers_cov_n_prot.fasta > sars_cov_2_sars_cov_1_n_prot.al
RUN mafft sars_cov_2_mers_cov_s_prot.fasta > sars_cov_2_sars_cov_1_s_prot.al

CMD ["sarscov2.py"]