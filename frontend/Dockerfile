FROM node:20.12.2-alpine3.19 AS build

WORKDIR /app

# Install dependencies first so this layer can be cached when only source files change.
COPY package*.json ./
RUN npm install --no-audit --no-fund

# Copy the rest of the application and build the static assets.
COPY . .
RUN npm run build


FROM nginx:1.27.4-alpine AS runtime

WORKDIR /usr/share/nginx/html

# Replace the default nginx config with an unprivileged, production-ready config.
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy the built app and make sure the runtime user can read it.
COPY --from=build --chown=nginx:nginx /app/dist ./

# Nginx needs writable temp directories even when it runs as a non-root user.
RUN mkdir -p /var/cache/nginx /tmp/nginx && \
    chown -R nginx:nginx /var/cache/nginx /tmp/nginx /usr/share/nginx/html

USER nginx

EXPOSE 8080

STOPSIGNAL SIGQUIT

CMD ["nginx", "-g", "daemon off;"]
