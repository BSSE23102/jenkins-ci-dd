# Use the official NGINX image as the base
FROM nginx:stable-alpine

# Copy your index.html file into the NGINX web root
# The '.' refers to the current directory (where the Dockerfile is)
COPY index.html /usr/share/nginx/html/index.html

# The container runs NGINX by default (CMD is already set by base image)
EXPOSE 80