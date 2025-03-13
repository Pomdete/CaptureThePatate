FROM node:21-alpine3.18
WORKDIR /usr/src/app
ENV PNPM_HOME="/pnpm"
ENV COREPACK_HOME="/tmp"
ENV PATH="$PNPM_HOME:$PATH"
ENV COREPACK_ENABLE_DOWNLOAD_PROMPT=0
RUN corepack enable

COPY ./src/package.json ./src/pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile

COPY ./src/ ./

EXPOSE 3000

RUN pnpm build
ENTRYPOINT ["npm", "start"]
